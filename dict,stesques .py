my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)
my_dict.update({'profession':'doctor'})
print(my_dict)
my_dict.update({'age': 40})
print(my_dict)

#ques2
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York' ,'profession':'doctor'}
print(my_dict)
my_dict.pop('profession', None)
print(my_dict)
print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'city'])
if 'age' in my_dict:
           print ("true")
else:
           print("Key 'age' does not exist in the dictionary.")


#ques3
my_dict1 = {'name': 'Alice', 'age': 30, }
my_dict2 = {'city': 'New York', 'profession': 'doctor'}
merged_dict = {**my_dict1, **my_dict2}
print(merged_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'profession': 'doctor'}

#ques4
nums = [1, 2, 1, 4, 5]
print(nums)
print(set(nums))  # Output: {1, 2, 4, 5} (removes duplicates)
print(list(set(nums)))  # Output: [1, 2, 4, 5] (converts set back to list)

#ques5
students = ['Megha', 'Aman']
subjects = ['Python', 'Java']
marks = [
        {"python": [85, 90]},
        {"java": [78, 88]},
]

result = {student: {subject: mark for subject, mark in zip(subjects, marks[i].values())} for i, student in enumerate(students)}
print(result)
