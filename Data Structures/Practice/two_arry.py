"""Given are two arrays. Find the existance of any element of array 1 in array2. If we find the
the element in the array return true or else false"""

arry1 = ['a', 's', 'j', 'b']
arry2 = ['x', 'a', 'v']

# Brute Force
# time-complexity --- O(m * n) & space-complexity --- O(1)
def compare_array_one(arry1, arry2):
    for i in range(0, len(arry1)):
        for j in range(0, len(arry2)):
            if arry1[i] == arry2[j]:
                return True           
    return False

# To have less time complexity we can implement a datastructure(dictionary)
# this below method has increased the space complexity - O(n)
# but brought down the time complexity to O (m + n) 
def compare_array_two(arry1, arry2):
    arry1_dict = {}
    for i in range(0, len(arry1)):
        if arry1[i] not in arry1_dict.keys():
            arry1_dict[arry1[i]] = True
    for j in range(0, len(arry2)):
        if arry2[j] in arry1_dict.keys():
            return True           
    return False
            
# this method is more readable using the built in methods
def compare_array_three(arry1, arry2):
    for item in arry2:
        if item in arry1:
            return True           
    return False

print(compare_array_one(arry1, arry2))
print(compare_array_two(arry1, arry2))
print(compare_array_three(arry1, arry2))