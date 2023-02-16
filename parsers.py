import re
from fire import *
from types import FunctionType
from pprint import pprint
 
#functions
#variables
#classes
#specify type and run
def main(file="test.py"):
    with open(file,"r") as f:
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
    All[file]={}
    All[file]["variables"]=variables
    All[file]["function"]=functions_in_script       

        
        

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