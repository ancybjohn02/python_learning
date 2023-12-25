# docstrings != comments
#  they're not ignored but rather given especial treatment

# it's always given right above the f(x) definition, right below f(x) name
#  or else it's not a docstring 
def cube(x):

    '''input a number and get its cube using this function'''
    # used right above the function definition 
    print("x***3 = ")
    y=x**3

    print(y)
    print(cube.__doc__)


    #  Python performance ehancement :  PEP-8
print(cube(4))
