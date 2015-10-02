###Author: Sumit Raj###

import pandas
class Bar:
   'Common base class for bar chart'
   dictt = {}
   def __init__(self, data=None, xAxis=None, yAxis=None):
      self.data = data
      #self.encoding_dict = encoding_dict
      self.xAxis = xAxis
      self.yAxis = yAxis
      self.final_json = None
      self.csv = None 

   def vega_encoding(self, encoding_dict):
      self.final_json['encoding'] = encoding_dict
      print self.final_json


   def vega(self):
      # self.csv.apply(self.readDataEx, axis=1)
      # data_values = {}
      # data_values["values"] = []
      # for each in Bar.dictt:
      #    data_values["values"].append({"a":each, "b":Bar.dictt[each]})
      #print Bar.dictt
      self.final_json = {}
      self.final_json["data"] = self.data
      #print self.csv.columns[0], self.csv.columns[1]
      #final_json["encoding"] = self.encoding_dict
      # print """call method vega_encoding passing dict as 
      # encoding_dict = {
      # "x": {"type": "O","name": "a"},
      # "y": {"type": "Q","name": "b"}
      # }"""
      # print "Choose any two columns for x and y names"
      # print self.csv.columns[0], self.csv.columns[1]

      self.final_json['encoding'] = {"x":{"type":"O", self.xAxis:"a"}, "y":{"type":"Q", self.yAxis:"b"}}
      print self.final_json

      #print self.final_json

   def vega_spec(self):
      csv = pandas.read_csv(self.data)
      self.csv = csv
      self.vega()

   def readDataEx(self, row):
      Bar.dictt[row[0]] = row[1]


# encoding_dict = {
#     "x": {"type": "O","name": "a"},
#     "y": {"type": "Q","name": "b"}
# }


 # encoding_dict = {
 #      "x": {"type": "O","area": "a"},
 #      "y": {"type": "Q","sales": "b"}
 #      }

# b1 = Bar('./data/simple.csv', encoding_dict)
# b1.vega_spec()

# from bar import Bar  
# b= Bar('./data/simple.csv', encoding_dict)
# b.vega_spec()