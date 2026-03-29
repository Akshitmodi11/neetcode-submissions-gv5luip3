class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index=[]
        for i in range(len(nums)):
            nums_with_index.append([nums[i],i])

        nums_with_index.sort()
        sum=0
        l=0
        r=len(nums)-1
        while l<r:
            sum=nums_with_index[l][0]+nums_with_index[r][0]
            if sum==target:
                return sorted([nums_with_index[l][1], nums_with_index[r][1]])
            elif sum<target:
                l+=1
            else:
                r-=1
      