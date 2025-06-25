collection={1,2,3,4}

print(collection)
print(type(collection))

collection={1,2,2,3,3,3,3,4,"hello world"}

print(collection)
print(type(collection))

collection={}  #empty dictonary

collection = set() #empty set ;syntax
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)
collection.remove(2)

collection.add("apna college")
collection.add((1,2,3))
#collection.add([1,2,3])  #list me errorj



print(collection)
print(type(collection))
print(len(collection))
collection.clear()

print(len(collection))

collection = {"hello", "world", "coding", "python"}

print(collection.pop())  #removes and returns an arbitrary element
print(collection.pop())  #removes and returns an arbitrary element

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))  # Union of two sets
print(set1.intersection(set2))  # Intersection of two sets
print(set1.difference(set2))  # Difference of two sets
print(set1.symmetric_difference(set2))  # Symmetric difference of two sets
print(set1.issubset(set2))  # Check if set1 is a subset of set2
print(set1.issuperset(set2))  # Check if set1 is a superset of set2


info ={
           "cat" :"a small animal",
           "table" :["a piece of furniture", "list of facts and figure"]

}

print(info)

#ques
subjects={
    "python", "java", "c++", "javascript", "c","python","java","python","java","c++"
}
print(subjects)
print(len(subjects))  # Length of the set

#ques
marks={}

x = int(input("Enter phy : "))
marks.update({"phy": x})

x = int(input("Enter chem : "))
marks.update({"chem": x})

x = int(input("Enter math: "))
marks.update({"math": x})

print(marks)


#ques

value = {9,9.0}
print(value)
value = {9,9.4}
print(value)

value = {
    ("float", 9.0), 
    ("int", 9), 
    

}

print(value)
