#python language

def push(data):
    stack_list.append(data)
  
def pop():
    data=stack_list[-1]
    del stack_list[-1]
    return data
    
def append(data):
    

def recursize(data): #recursive function
    if data<0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned", data)
    
data_stack=list() #using the python method / append(push), pop
data_stack.append(1)
data_stack.append(2)
data_stack.pop(2)



stack_list=list() # Made stack function


