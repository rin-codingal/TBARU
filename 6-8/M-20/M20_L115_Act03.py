L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)
  
count = 0
  
for i in L:
    count += i
      
avg = count/len(L)
  
print("sum = ", count)
print("average = ", avg)

# Sorting the elements of the list
L.sort()
 
# printing the first element
print("Smallest element is:", L[0])

# printing the last element
print("Largest element is:", L[-1])