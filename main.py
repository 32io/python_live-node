import re

import pickle
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
def save(m):
    with open("Manager.m","wb") as f:
        pickle.dump(m,f)
def load():
    with open("Manager.m","rb") as f:
        return pickle.load(f)
def main():
    m=Manager()
    with open(r"test.py","r") as f:
        file_read=f.read()
    
    tab="   "
    module_list=[]
    function=False
    functions_in_script=[]
    function_list=[]
    variables={}
    lines=file_read.split("\n")
    lines.append("#commment to add extra loop run")
    for i in lines:
        tab_count=i.count(tab,0,len(i))
        if tab_count==0:
            if function:
                functions_in_script.append("\n".join(function_list))
                function_list.clear()
            function=False  
            if i.__contains__("def"):
                function_list.append(i)
                function=True
                continue
            elif i.__contains__("="):
                var_split=i.split("=")
                variables[var_split[0]]=var_split[1]
                continue
        if function:
            function_list.append(i)
    print(functions_in_script)
    print(variables)
    for x,y in variables.items():
        Var(m,x,y)
    for i in functions_in_script:
        result = re.search('def (.*)', i)
        r=result.group(1)
        r=r.split("(")[0]
        print(r)
        Func(manager=m, name=r,function=i,ret_type="<list>" )#name #function

            

        
        

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