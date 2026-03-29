class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result={}
        for num in nums:
            if num in result:
                result[num]+=1
            else:
                result[num]=1
            
        for key, value in result.items():
            if value==1:
                return key
