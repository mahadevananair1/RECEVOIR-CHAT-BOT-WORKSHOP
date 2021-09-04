# -->comments in python,interpreter wont read those lines
""" 
 Multiline comments in 
 python 
"""
# we need python list,dictionaries,strings as datatypes
# It is good to understand about functions,specifically user defined functions

# LIST
# declaration
# indexing of list starts from 0
sample_list = [1, 2, 3, 4]

sample_type_casted_list = list()
# manipulation
print(f"max value is {max(sample_list)}")  # to find the maximum value
sample_list[0] = "sooraj"
len(sample_list)  # returns the length of the list
sample_type_casted_list.append('RECEVOIR')
print(sample_list, sample_type_casted_list)

# DICTIONARY
# declaration
# indexing of dictionary starts from 0
sample_dict = {1: "one", 2: "two"}
sample_dict_type_cast = dict()
print(sample_dict, sample_dict_type_cast)
# manipulation
sample_dict[1] = "zero"
print(f'value at key 1 {sample_dict[1]}')

# STRING
# indexing of string starts from 0
name = "Hi"
declaration = "There"
print(name+" "+declaration)  # string cooncatination

# USER DEFINED FUNCTIONS
test = "Hello"


def sample(test):
    test += " There"
    return test


# --->Hi There--> here the value of test only lives inside the function 'sample'
print(sample("Hi"))
print(test)  # --->Hello-->the value of the test remains same as initiated
