import requests  # to import request library in our code
import json  # to import json library in our code

# REQUESTS
""" Making the requests library to do a GET request from the google url 
    get requet is used to recieve information it could be json or html
"""


r = requests.get('https://www.google.com/')
print(r)  # prints the response of the server
print(r.content)  # returns the output by the server in string format

# converts the string into utf8 format-->python represent the string in utf8 format
print(r.content.decode('utf8'))


# JSON

# Example
""" 
{"employees":[  
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},  
    {"name":"Bob", "email":"bob32@gmail.com"},  
    {"name":"Jai", "email":"jai87@gmail.com"}  
]}  

"""

# type function returns the datatype of the argument--->here it will be string
print(type(r.content.decode('utf8')))

# this converts string into python dictionary
print(json.loads(r.content.decode('utf8')))

# returns the datatype-->here it is dictionary
print(type(json.loads(r.content.decode('utf8'))))
