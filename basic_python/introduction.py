# For our course we are using python 3.12


########## python3 version check
# python3 --version
########## pip version check
# pip3 --version
########## How to Run Python in terminal
#### you need to go to the main directory then run
# python3 <filename>.py


str_d = 'hello world' # how to define string
bool_d = False # how to define boolean ( True or False)
number_int =  123 # how to define integer 
number_float = 123.34 # how to define floating number


list_d = [1,2,3,4,5,6,7,8,9,10] # how to define list
tuple_d = (1,2,3,4,5,6,7,8,9,10) # how to define tuple
dict_d = {
    'hello': 'world',
    'name': {
        'first': 'Abhijit',
        'last': 'Gayen',
    }
} # how to define dictionary

print("hello world") # to print in output
data_input = input("Enter Number: ") # we take input and store in data_input veriable 
#and keep in mind that the stored value is a string.
print(type(data_input)) # mainly we use 'type' to see the data type of veriable

number_str ='123' # this is number we want to conver this in number. that is known as type custing.
number_int = int(number_str) # we use 'int' to convert string to integer. 
#keep in mind if number_str ='123wert' then there will be error in type custing.

def hello_function(): # how to define function 
    print("hello function")

hello_function() # how to call a function

    