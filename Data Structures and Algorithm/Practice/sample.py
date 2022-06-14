# # Heap Sort in python


# def heapify(arr, n, i):
#     # Find largest among root and children
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2

#     if l < n and arr[i] < arr[l]:
#         largest = l

#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     # If root is not largest, swap with largest and continue heapifying
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)


# def heapSort(arr):
#     n = len(arr)

#     # Build max heap
#     for i in range(n//2-1, -1, -1):
#         print(i)
#         heapify(arr, n, i)

#     for i in range(n-1, 0, -1):
#         # Swap
#         arr[i], arr[0] = arr[0], arr[i]

#         # Heapify root element
#         heapify(arr, i, 0)


# arr = [1, 12, 9, 5, 6, 10]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d " % arr[i], end='')
  
  
  
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         self.nums = nums
#         self.target = target
#         count = 0
#         ind_ary = []
#         for item in self.nums:
#             second_num = target - item
#             left_arr = self.nums[0:count]
#             right_arr = self.nums[count+1:len(self.nums)]
#             if second_num in left_arr or second_num in right_arr :
#                 ind_ary.append(count)
#                 second_indx = left_arr.index(second_num) if second_num in left_arr else right_arr.index(second_num)
#                 ind_ary.append(second_indx)
#                 break;
#             count += 1
#         return ind_ary
        
        
# obj = Solution()        
# print(Solution.twoSum(obj,[2,7,11,15], 9))


# from msilib import init_database


# def myAtoi(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     revised_ary = [x for x in s if x.isdigit() or x in ('+','-','.')]
#     print(revised_ary)
#     # return int(''.join(revised_ary))

# print(myAtoi('4193 with words'))


def sorter(arry, strt_idx, no_idx, endpoint):
    end = strt_idx + no_idx + 1
    if end < len(arry) :
        for i in range(strt_idx, end):
            tmp = arry[endpoint]
            arry[endpoint] = arry[i]
            arry[i] = tmp
            endpoint -= 1
    return arry, endpoint


def duplicate_sort(arr):
    # here the given array is sorted
    # in place sorting so the space complexity would be O(1)
    end_pointer = len(arr)-1
    inital_pointer = 0
    while inital_pointer < end_pointer:
        counter = 0
        flag = False
        snd_p = inital_pointer+1
        while snd_p < len(arr)-1: 
            if arr[inital_pointer] == arr[snd_p]:
                counter +=1
                flag = True
            elif arr[inital_pointer]!= arr[snd_p]:
                break 
            snd_p += 1
        if flag:
            arr, end_pointer = sorter(arr, inital_pointer, counter, end_pointer)
        inital_pointer += 1
    return arr

print(duplicate_sort([1,2,2,2,3]))