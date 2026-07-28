class Solution(object):
    def searchInsert(self, nums, target):
        s=0
        e=len(nums)-1
        while s<=e:
            m=(s+e)//2
            if nums[m]==target:
                return m
            elif target>nums[m]:
                s=m+1
            else:
                e=m-1
        if target>nums[m]:
            return m+1
        else:
            return m