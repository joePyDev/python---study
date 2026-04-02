


name = input("What is your name?")
print("Hello",name)



print(int(3.14))
print(int("42"))
print(int(True))
print(int(False))



def hello():
    print("Hello Word")
    
def calculate_sum(a,b):
    print(a + b)

calculate_sum(3,1)

my_sum = calculate_sum(3, 1)
print(my_sum) # none




def calculate_sum2(a,b):
    return a + b

my_sum = calculate_sum2(3, 1)
print(my_sum)





#------------------------------------    
#           scope LEGB              |                   
#------------------------------------    


# L = Local scope
def my_func():
    my_var = 10
    print(my_var)
    
my_func()

# print(my_var) nameError, not define   


#------------------------------------    
# E = enclosing scope 
def outer_func():
    msg ="hellow there!"
    def inner_func():
        print(msg)
        
    inner_func()


outer_func()    
    
    
"""    
def outer_func2():
    msg = "hello!"
    print(res)
    def inner_func2():
        res = "haw are you?"
        print(msg)
    inner_func2()
"""

def outer_func3():
    msg="Hello PY"
    res = "" # Declare res in the enclosing scope
    
    def inner_func3():
        nonlocal res
        res = "hw are you?"
        print(msg)
        
    inner_func3()
    print(res)
        
outer_func3()       
    
    
    
#------------------------------------    
 # G = Global
    
my_var = 100

def show_var():
    print(my_var)
    
show_var()
print(my_var)    
    
    
    
my_var_1 = 200

def show_vars():
    global my_var_2    
    my_var_2 = 250
    print(my_var_1)
    print(my_var_2)

show_vars()    
    
print(my_var_2,"out of function print")
    



my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20
    
    
#------------------------------------    


# B = Built-in scope 

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


