import ast
import importlib
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
            print("x already existed as s ")
            self.variables[x]=y
        else:
            if x in keys:
                
            
                return self.variables[x]
            else:
                print("only this values exists as variables ",keys)
    def function(self,name,arguments,func=None):
            # importing the module
        if func:
        # function at run-time
            f_code = compile(*func)
            self.variables[name] = FunctionType(f_code.co_consts[0], globals(), "name")
        else:
            # calliong the function
            print(self.variables[name](*arguments))

class Module():
    def __init__(self,manager,dep) -> None:
        manager.dependecies.append(dep)
        print(dep)
class Var():
    def __init__(self,manager,name,value) -> None:
        
        manager.variable(name,value)  
class Func():     
    def __init__(self,manager,name,arguments,function,ret_type) -> None:
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
    with open(r"C:\Users\ADMIN\OneDrive\Desktop\amani\node based live sys\test.py","r") as f:
        p=ast.parse(f.read())
    for i in ast.walk(p):
        print(i)
        print(i.__dict__)

    print(m.dependecies)
    print(m.variables)
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
#run and save code
    

main()