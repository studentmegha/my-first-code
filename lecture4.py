info = {
      "name": "apna college",
      "subject":[ "python", "java", "c++"],
      'topics':("dict","set"),
       "age":18,
      "is _adult" : True,
      "marks":94.5, #can be floating value ,cab be key , can be string,can be tuple
}


print(info)
print(type(info))
print(info["name"])
print(info["subject"])
print(info["age"])
print(info["is _adult"])

null_dict ={}
null_dict["name"] = "megha"
print(null_dict)
print(type(null_dict))


info["name"] = "megha" #overwriting the value of key "name"
info["sur naame"] = "yadav"
print(info)



student = {    "name": "megha",
    "subject" :{
        "physics": 90,
        "chemistry": 95,
            "maths": 85
    }
} 
#nested ductionary
print(student)
print(student["subject"])# Accessing nested dictionary value
print(student["subject"]["physics"]) # Accessing nested dictionary value using key




student = {    "name": "megha",
    "subject" :{
        "physics": 90,
        "chemistry": 95,
            "maths": 85
    }
} 
print(list(student.keys()))   #nested keys dont come in the output
print(student.keys())  #nested keys come in the output
print(list(student.values())) #nested values dont come in the output
print(student.values()) #nested values come in the output
print(student.items())  #nested keys and values come in the output

print(student.get("name"))  # Accessing value using get method

print(len(list(student.keys())) ) # Length of the dictionary
#or of 57
print(len(student))  # Length of the dictionary


print(student["name"])  # Accessing value using key
print(student.get("name"))  # Accessing value using get method

#print(student["name2"]) # Accessing value using key (will raise KeyError if key doesn't exist)
print(student.get("name2"))  # Accessing value using get method (will return None if key doesn't exist)


student = {    "name": "megha",
    "subject" :{
        "physics": 90,
        "chemistry": 95,
            "maths": 85
    }
} 

student.update({"city" : "Delhi"})  # Adding a new key-value pair
student.update({"name":"megha yadav"})  # Updating an existing key-value pair
#or of 80
new_dict = {"city" : "Delhi"}
print(student)


#student.popitem()  # Removes the last inserted key-value pair
#student.fromkeys({"name", "age", "city"})  # Creates a new dictionary with specified keys and None as values













