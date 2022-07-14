class Solution:
    def search(self, nums, target) -> int:
        num_lst = len(nums)
        if num_lst % 2 == 0:
            mid_point = num_lst//2
        else:
            mid_point = (num_lst-1)//2
        print(mid_point)
        if target < nums[mid_point]:
            self.search(nums[0:mid_point], target)
        elif target > nums[mid_point]:
            self.search(nums[mid_point:num_lst], target)
        
        if target == nums[mid_point]:
            print('found the element')
            
        
        