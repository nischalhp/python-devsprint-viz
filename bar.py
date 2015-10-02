
import json
import pprint
import pandas as pd


def convert_str_to_json(json_string):
    _json = json.loads(json_string)
    return _json


class Bar:
    def __init__(self,dataFrame,x_axis,y_axis):

        jsonString = dataFrame.to_json(orient="records")
        self.data= json.loads(jsonString)
        self.xAxis = x_axis
        self.yAxis = y_axis


    def getSpec(self):
        data = {}
        data['values']=self.data

        encoding={}
        op_dict = {}

        op_dict["marktype"]="bar"

        encoding["x"]={}
        encoding["y"]={}
        encoding["x"]["type"]="O"
        encoding["x"]["name"]=self.xAxis
        encoding["y"]["type"]="Q"
        encoding["y"]["name"]=self.yAxis

        op_dict["encoding"]=encoding
        op_dict["data"]=data

        spec = json.dumps(op_dict)

        return spec


'''
pp = pprint.PrettyPrinter(indent=4)


my_graph = Bar([
  {
    "areas": "north",
    "sales": '5'
  },
  {
    "areas": "east",
    "sales": '25'
  },
  {
    "areas": "west",
    "sales": '15'
  },
  {
    "areas": "south",
    "sales": '20'
  },
  {
    "areas": "central",
    "sales": '10'
  }
],"areas","sales")


pp.pprint(my_graph.spec)
'''
