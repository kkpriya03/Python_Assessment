"""
1. Write a Python program to create a list of integers and print its elements.
li=[5,6,8,9,4,5]
print("Element is:")
for i in li:
    print(i)

2. Write a program to find the sum and average of all elements in a list.
    
sum=0
li=[5,6,8,9,4,5]
print("List is:")
print(li)
for i in li:
    sum=sum+i
    average = sum / len(li)

print("sum is:",sum)
print("average is:",average)

3. Write a program to find the largest and smallest element in a list.
li=[10,20,30,40,50]
print("List is:")
print(li)
print("maximum number is:",max(li))
print("smallest number is:",min(li))

4. Write a Python program to count the number of elements in a list without using len().
count=0
li=[10,20,30,40,50]
print("List is:")
print(li)
for i in li:
    count=count+1
print("number of element are:",count)

5. Write a program to reverse a list without using built-in functions.
li = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(li)-1, -1, -1):
    reversed_list.append(li[i])

print("Original list:", li)
print("Reversed list:", reversed_list)

6. Write a program to check if an element exists in a list.

li = [10, 20, 30, 40, 50]
element = int(input("Enter element: "))
if element in li:
    print("Element found")
else:
    print("Element not found")

7. Write a Python program to remove duplicate elements from a list.
li = [10, 20, 30, 20, 40, 10, 50]
unique_list = []
for i in li:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
    
8. Write a program to sort a list in ascending and descending order.
# Ascending order
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]

print("Ascending order:", li)

# Descending order
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]
print("Descending order:", li)


Intermediate Level
9. Write a program to merge two lists and remove duplicates.
li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]

merged_list = li1 + li2
unique_list = []
for i in merged_list:
    if i not in unique_list:
        unique_list.append(i)
print("Merged list:", merged_list)
print("After removing duplicates:", unique_list)

10. Write a program to find common elements between two lists.
li1 = [10, 20, 30, 40, 50]
li2 = [30, 40, 60, 70]

common = []
for i in li1:
    if i in li2:
        if i not in common:
            common.append(i)
print("Common elements:", common)

11. Write a program to split a list into even and odd numbers.
li = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)

12. Write a program to rotate a list by n positions.
li=[1,2,3,4,5,6,7,8,9,10]
print(li)
n=int(input("No of Right Rotation:"))
for i in range(n):
      val=li.pop(len(li)-1)
      li.insert(0,val)
print(li)

13. Write a Python program to find the second largest number in a list.
li = [10, 20, 40, 30, 50]

largest = li[0]
second_largest = li[0]

for i in li:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest number:", second_largest)

14. Write a program to flatten a nested list.

li = [1, 2, [3, 4], 5, [6, 7]]
flat_list = []
for i in li:
    if type(i) == list:
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)
print("Flattened list:", flat_list)

15. Write a program to count frequency of each element in a list.
li = [10, 20, 10, 30, 20, 10, 40]
visited = []

for i in range(len(li)):
    if li[i] in visited:
        continue
        
    count = 1
    for j in range(i + 1, len(li)):
        if li[i] == li[j]:
            count += 1
    
    visited.append(li[i])
    print(li[i], "occurs", count, "times")
    
16. Write a program to replace all negative numbers with zero in a list.
li = [10, -5, 20, -3, 30, -1]

for i in range(len(li)):
    if li[i] < 0:
        li[i] = 0

print("Updated list:", li)

17. Write a program to remove all occurrences of a given element from a list.
li = [10, 20, 30, 20, 40, 20, 50]

element = int(input("Enter element to remove: "))

while element in li:
    li.remove(element)

print("Updated list:", li)

18. Write a program to check if a list is a palindrome.

my_list = [1, 2, 3, 2, 1]

is_palindrome = True

for i in range(len(my_list)//2):
    if my_list[i] != my_list[-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

19. Write a Python program to find missing numbers in a given list of consecutive
integers.
li = [1, 2, 4, 6, 7]
missing = []

for i in range(li[0], li[-1] + 1):
    if i not in li:
        missing.append(i)

print("Missing numbers:", missing)

20. Write a program to perform element-wise addition of two lists.

li1 = [10, 20, 30, 40]
li2 = [1, 2, 3, 4]

result = []

for i in range(len(li1)):
    result.append(li1[i] + li2[i])

print("Result:", result)

21. Write a Python program to find the longest increasing subsequence in a list.

li=[21,78,89,765,23,23,35,39,45,667,8,9,635,58]
longest_sub_seq=[]
temp=[]
for i in range(0,len(li)-1):
    if li[i]<li[i+1]:
        temp.append(li[i])
    else:
        temp.append(li[i])
        if len(temp)>len(longest_sub_seq):
            longest_sub_seq=temp
        temp=[]
print(longest_sub_seq)

22. Write a program to group elements based on frequency.
li=[1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
group_list=[]

for x in set(li):
    group_list.append((x,li.count(x)))
print(group_list)

23. Write a Python program to create a tuple and print its elements.

tuple = (10, 20, 30, 40, 50)
for item in tuple:
    print(item)
    
24. Write a program to find the length of a tuple.

tuple = (10, 20, 30, 40, 50)
length = len(tuple)
print("Length of tuple is:", length)

25. Write a program to find the maximum and minimum element in a tuple.
tuple = (10, 5, 20, 8, 15)
maximum = max(tuple)
minimum = min(tuple)

print("Maximum element:", maximum)
print("Minimum element:", minimum)

26. Write a program to convert a tuple into a list.
tuple = (10, 20, 30, 40)
list = list(tuple)
print("Tuple:", tuple)
print("List:", list)

27. Write a program to check if an element exists in a tuple.
tuple = (10, 20, 30, 40, 50)
element = 30
if element in tuple:
    print("Element exists in tuple")
else:
    print("Element does not exist in tuple")

28. Write a program to count occurrences of an element in a tuple.
my_tuple = (10, 20, 30, 20, 40, 20, 50)
element = 20
count = my_tuple.count(element)
print("Element appears", count, "times")

29. Write a program to slice a tuple and display the result.
tuple = (10, 20, 30, 40, 50, 60)
sliced_tuple = tuple[1:5]
print("Original Tuple:", tuple)
print("Sliced Tuple:", sliced_tuple)

30. Write a program to find repeated elements in a tuple.
my_tuple = (10, 20, 30, 20, 40, 30, 50)
repeated = set()

for item in my_tuple:
    if my_tuple.count(item) > 1:
        repeated.add(item)
print("Repeated elements:", repeated)

31. Write a program to merge two tuples.

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

merged_tuple = tuple1 + tuple2
print("Merged Tuple:", merged_tuple)

32. Write a program to unpack elements of a tuple into variables.

my_tuple = (10, 20, 30)
a, b, c = my_tuple
print("a =", a)
print("b =", b)
print("c =", c)

33. Write a Python program to sort a tuple.

my_tuple = (50, 20, 40, 10, 30)
temp_list = list(my_tuple)
temp_list.sort()
sorted_tuple = tuple(temp_list)
print("Sorted Tuple:", sorted_tuple)

34. Write a program to convert a list of tuples into a dictionary.
n = int(input("Enter number of tuples: "))
my_list = []

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_list.append((key, value))

my_dict = dict(my_list)
print("Dictionary:", my_dict)

35. Write a program to find the index of an element in a tuple.
my_tuple = (10, 20, 30, 40, 50)
element = 30

index = my_tuple.index(element)
print("Index of element:", index)

36. Write a program to remove an element from a tuple (without directly modifying it).
my_tuple = (10, 20, 30, 40, 30)
element = 30
temp_list = list(my_tuple)

if element in temp_list:
    temp_list.remove(element)

new_tuple = tuple(temp_list)
print(new_tuple)

37. Write a program to find common elements between two tuples.
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)
common = tuple(x for x in tuple1 if x in tuple2)
print("Common elements:", common)

38. Write a Python program to check if a tuple is a palindrome.
my_tuple = (1, 2, 3, 2, 1)

is_palindrome = True

for i in range(len(my_tuple)//2):
    if my_tuple[i] != my_tuple[-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

39. Write a program to find the element with maximum frequency in a tuple.
 my_tuple = (10, 20, 30, 20, 40, 20, 30)

freq = {}

for item in my_tuple:
    freq[item] = freq.get(item, 0) + 1

max_element = max(freq, key=freq.get)
print("Element:", max_element)
print("Frequency:", freq[max_element])   

40. Write a program to create a nested tuple and access its elements.
nested_tuple = (1, (2, 3), (4, 5, 6))

print("First element:", nested_tuple[0])
print("Second element (tuple):", nested_tuple[1])
print("Element inside nested tuple:", nested_tuple[1][0])
print("Another element:", nested_tuple[2][2])

"""

nested_tuple = (1, (2, 3), (4, 5, 6))

print("First element:", nested_tuple[0])
print("Second element (tuple):", nested_tuple[1])
print("Element inside nested tuple:", nested_tuple[1][0])
print("Another element:", nested_tuple[2][2])




