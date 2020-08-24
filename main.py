# we are going to obtain a request from a website to see if the code we use will get back the price of the chair from the webpage. 

# Now i have done this on Pycharm, however im just going to go on this for repetition and practice.abs

def age_program():
  user_age = input("Enter your age: ")
  age_seconds = int(user_age)*365 * 24 * 60 * 60
  print("your age in seconds is {}".format(age_seconds))

# age_program()

# so now we are going to do use a jsondata, its a type of data. They are all structured with an open/close curly brace. We can use them to create lists. 
 
# {} within these are called dictionaries( a key value pair ie one value and one key like the example below) and [] are lists

# data.json 

{
  "students":[
    {
      "name": "Boris",
      "score": 100,
      "ID": "786786"
    },
    {
      "name": "tas",
      "score": 104,
      "ID": "786100"
    },
    {
      "name": "cats",
      "score": 10,
      "ID": "786510"
    }
  ]
}

# we need import some python files now so we need to open an requirements.txt files


import requests

requests = requests.get("http://www.google.com")

print(request.content)

