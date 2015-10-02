
# coding: utf-8

# In[2]:

import json
import pprint

# In[3]:

def convert_str_to_json(json_string):
    _json = json.loads(json_string)
    return _json


# In[15]:

class Bar:
    def __init__(self,_json,x_axis,y_axis):
        self.op_dict={}
        data={}
        data['values']=_json
        encoding={}
        self.op_dict["marktype"]="bar"
        encoding["x"]={}
        encoding["y"]={}
        encoding["x"]["type"]="Q"
        encoding["x"]["name"]=x_axis
        encoding["y"]["type"]="O"
        encoding["y"]["name"]=y_axis
        self.op_dict["encoding"]=encoding
        self.op_dict["data"]=data


# In[16]:
pp = pprint.PrettyPrinter(indent=4)


# In[16]:
#***********************************************example******************************************************
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
],"area","sales")


pp.pprint(my_graph.op_dict)

