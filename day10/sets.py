from operator import add


fruits= {"Apple","Banana","Mango"}
print(fruits)

numbers= {1,2,2,3,4,4,5}
print(numbers)

# empty set 
empty=set()
print(type(empty))

# add
skills= {"Python","HTML"}
skills.add("CSS")
print(skills)

# add multiple data 
skills= {"Python"}
skills.update(["HTML","CSS","JavaScript"])
print(skills)

# Deleting data from set 
# remove
skills= {"Python","HTML","CSS"}
skills.remove("HTML")
print(skills)

# discard 
skills= {"Python","HTML"}
skills.discard("Java")

#pop
skills= {"Python","HTML","CSS"}
removed=skills.pop()
print(removed)
print(skills)

#clear
skills= {"Python","HTML"}
skills.clear()
print(skills)

#membership operator
languages= {"Python","Java","C++"}
print("Python" in languages)
print("HTML" in languages)

#union
set1= {1,2,3}
set2= {3,4,5}
print(set1|set2)

#intersection
set1= {1,2,3}
set2= {2,3,4}
print(set1&set2)

#difference
set1= {1,2,3}
set2= {2,3,4}
print(set1-set2)

# Symmetric Difference
set1= {1,2,3}
set2= {2,3,4}
print(set1^set2)

#converting a list to a set
marks= [90,85,90,78,85,100]
unique_marks=set(marks)
print(unique_marks)

#frozenset
numbers=frozenset([1,2,3,4])
print(numbers)