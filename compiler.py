import re
from parsers import *

from types import FunctionType
from pprint import pprint
class Manager():
    def __init__(self) -> None:
        self.variables={}
        self.dependecies=[]
    def variable(self,x,y=None):
        keys=self.variables.keys()
        if y:
            self.variables[x]=y
        else:
            if x in keys:
                
            
                return self.variables[x]
            else:
                print("only this values exists as variables ",keys)
    def function(self,name,arguments,func=None ):
            # importing the module
        if func:
        # function at run-time
            f_code = compile(*func)
            self.variables[name] = FunctionType(f_code.co_consts[0], globals(), "name")
        else:
            # calliong the function
            print(self.variables[name](*arguments))


def Var(manager,name,value): 
        manager.variable(name,value)  
def Func(manager,name,function,ret_type,arguments=None) -> None:
        manager.function(name,arguments,func=[function, ret_type, "exec"])
        

    #functions
    #variables
    #classes
    #specify type and run

def main(file="test.py"):
    m=Manager()
    variables=All[file]["variables"]
    functions_in_script=All[file]["function"]       
    for x,y in variables.items():
        Var(m,x,y)
    for i in functions_in_script:
        result = re.search('def (.*)', i)
        r=result.group(1)
        r=r.split("(")[0]
        print(r)
        Func(manager=m, name=r,function=i,ret_type="<list>" )#name #function
        print(m.variables["n1"])
        
        

"""
if type(k)=="module":
Module(m,k)
else:
Var(m,k,k)
print(m.variables)
"""
   #store manager object
   #give manager object

# to do 
# generate variable modules and dependecies from code
#run newly found code
main()

