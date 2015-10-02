def _repr_html_(self):
        """Build the HTML representation for IPython."""
        vis_id = str(uuid4()).replace("-", "")
        html = """<div id="vis%s"></div>
<script>
   ( function() {
     var _do_plot = function() {
       if (typeof vg === 'undefined') {
         window.addEventListener('vincent_libs_loaded', _do_plot)
         return;
       }
       vg.parse.spec(%s, function(chart) {
         chart({el: "#vis%s"}).update();
       });
     };
     _do_plot();
   })();
</script>
<style>.vega canvas {width: 100%%;}</style>
        """ % (vis_id, self.to_json(pretty_print=False), vis_id)
        return html

def display(self):
    """Display the visualization inline in the IPython notebook.
    This is deprecated, use the following instead::
        from IPython.display import display
        display(viz)
    """
    from IPython.core.display import display, HTML
    display(HTML(self._repr_html_()))


def initialize_notebook():
    """Initialize the IPython notebook display elements"""
    try:
        from IPython.core.display import display, HTML
    except ImportError:
        print("IPython Notebook could not be loaded.")

    # Thanks to @jakevdp:
    # https://github.com/jakevdp/mpld3/blob/master/mpld3/_display.py#L85
    load_lib = """
                function vct_load_lib(url, callback){
                      if(
                typeof d3 !== 'undefined' &&
                url === '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js'){
                        callback()
                      }
                      var s = document.createElement('script');
                      s.src = url;
                      s.async = true;
                      s.onreadystatechange = s.onload = callback;
                      s.onerror = function(){
                        console.warn("failed to load library " + url);
                        };
                      document.getElementsByTagName("head")[0].appendChild(s);
                };
                var vincent_event = new CustomEvent(
                  "vincent_libs_loaded",
                  {bubbles: true, cancelable: true}
                );
                """
    lib_urls = [
        "'//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js'",
        ("'//cdnjs.cloudflare.com/ajax/libs/d3-geo-projection/0.2.9/"
         "d3.geo.projection.min.js'"),
        "'//wrobstory.github.io/d3-cloud/d3.layout.cloud.js'",
        "'//wrobstory.github.io/vega/vega.v1.3.3.js'"
    ]
    get_lib = """vct_load_lib(%s, function(){
                  %s
                  });"""
    load_js = get_lib
    ipy_trigger = "window.dispatchEvent(vincent_event);"
    for elem in lib_urls[:-1]:
        load_js = load_js % (elem, get_lib)
    load_js = load_js % (lib_urls[-1], ipy_trigger)
    html = """
           <script>
               %s
               function load_all_libs(){
                  console.log('Loading Vincent libs...')
                  %s
               };
               if(typeof define === "function" && define.amd){
                    if (window['d3'] === undefined ||
                        window['topojson'] === undefined){
                        require.config(
                            {paths: {
    d3: '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min',
    topojson: '//cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min'
                              }
                            }
                          );
                        require(["d3"], function(d3){
                            console.log('Loading Vincent from require.js...')
                            window.d3 = d3;
                            require(["topojson"], function(topojson){
                                window.topojson = topojson;
                                load_all_libs();
                            });
                        });
                    } else {
                        load_all_libs();
                    };
               }else{
                    console.log('Require.js not found, loading manually...')
                    load_all_libs();
               };
           </script>""" % (load_lib, load_js,)
    return display(HTML(html))