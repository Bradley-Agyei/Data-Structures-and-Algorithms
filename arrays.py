# Working with arrays(lists) in Python

new_list = [1,2,3]

# Get first value 
result = new_list[0]
print(result)

#Search for an item in list
if 10 in new_list:
    print(True)
else:
    print(False)

#Iterate over list manually and do comparisons
for n in new_list:
    if n == 1:
        print(True)

        break

#Inserting in a list 

numbers = []
numbers.append(2)
numbers.insert(0,12)
numbers1 = []
numbers1.extend([4,5,6])

print(numbers)
print(numbers1)

#Delete operation 
numbers1.remove(5)
print(numbers1)