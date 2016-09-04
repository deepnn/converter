import sys
import os, inspect
import keras
import json
from collections import OrderedDict

#!/usr/bin/env python
# parse classes, methods and functions in a module.
# Works with user-defined modules, all Python library
# modules, including built-in modules.

import inspect
import os, sys
   
def parse_func(obj, method=False, class_dict={}):
   """ parse the function object passed as argument.
   If this is a method object, the second argument will
   be passed as True """
   # for each method attribute, either put it in to 
   # methods (setters) for now this is list of methods
   # or params (constructor params) or args of the __init__
   # for each param: put their list as 'params'
   # put their default args as 'defaults'
   # and their types as 'types'
   # params (constructor params) or args of the __init__
   # for each param: put their list as 'params'
   # put their default args as 'defaults'
   # and their types as 'types'
   
   #if method:
      #class_dict['methods'][obj.__name__] = {}
      
   try:
       arginfo = inspect.getargspec(obj)
   except TypeError:
      print 
      return
   
   args = arginfo[0]
   argsvar = arginfo[1]

   if args:
       if args[0] == 'self':
           args.pop(0)

       #class_dict['methods'][obj.__name__]['params'] = args
       #class_dict['methods'][obj.__name__]['types'] = {}
       #class_dict['methods'][obj.__name__]['defaults'] = {}
       if obj.__name__ == '__init__':
           class_dict['attrs'] = args
       if arginfo[3]:
           dl = len(arginfo[3])
           al = len(args)
           defargs = args[al-dl:al]
           
           for key, val in zip(defargs, arginfo[3]):
               #class_dict['methods'][obj.__name__]['defaults'][key] = val
               #class_dict['methods'][obj.__name__]['types'][key] = type(val).__name__
               if obj.__name__ == '__init__':
                   #class_dict['defaults'][key] = val
                   #class_dict['types'][key] = type(val).__name__
                   pass

def parse_class(obj, class_dict={}):
   """ parse the class object passed as argument,
   including its methods """
   print(obj)
   # name
   class_dict['name'] = obj.__name__
   class_dict['attrs'] = {}
   # base type
   #class_dict['baseType'] = obj.__base__.__name__
   # type
   #class_dict['type'] = obj.__module__
   # methods
   #class_dict['methods'] = {}
   #class_dict['defaults'] = {}
   #class_dict['types'] = {}
   
   count = 0
   
   for name in obj.__dict__:
       item = getattr(obj, name)
       if inspect.ismethod(item) or inspect.isfunction(item):
           count += 1
           parse_func(item, True, class_dict)

   return class_dict

def parse_module(module, layers_dict=[]):
   """ parse the module object passed as argument
   including its classes and functions """
   print(module)
   
   count = 0
   
   for name in dir(module):
       obj = getattr(module, name)
       if inspect.isclass(obj):
          count += 1 
          class_dict = parse_class(obj)
          layers_dict.append(class_dict)
   
   return layers_dict

def parse_layers(module):
    layers_dict = []
    classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
        	class_dict = {}
        	class_dict = parse_class(obj, class_dict)
        	layers_dict.append(class_dict)
        	classes.append(obj.__name__)
	
	#sort_order = ['name', 'baseType', 'params', 'types', 'defaults', 'type'] # 'methods',
	sort_order = ['name', 'attrs']
	
	layers = [OrderedDict(sorted(item.iteritems(), key=lambda (k, v): sort_order.index(k)))
               for item in layers_dict]
    #json_layers_dict = json.dumps(layers, ensure_ascii=False, indent=4, sort_keys=True)
    #print(json_layers_dict)
    
    with open('keras_layers.json', 'w') as outfile:
        json.dump(layers, outfile, ensure_ascii=False, indent=4)#, sort_keys=True)
    with open('keras_layer_names.json', 'w') as outfile:
        json.dump(classes, outfile, ensure_ascii=False, indent=4)#, sort_keys=True)
            
            
if __name__=='__main__':
	parse_layers(keras.layers)
	#parse_module(keras.layers.core)
	#parse_class(keras.layers.core.Activation)


