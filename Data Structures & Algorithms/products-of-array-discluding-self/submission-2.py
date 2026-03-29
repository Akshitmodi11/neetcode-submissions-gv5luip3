class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        pre=[1]*(len(nums))
        post=[1]*(len(nums))
        prefix,postfix=1,1

        for i in range(len(nums)):
            pre[i]=prefix
            prefix*=nums[i]

        for j in range(len(nums)-1,-1,-1):
            post[j]=postfix
            postfix*=nums[j]

        for i in range(len(nums)):
            res[i]=pre[i]*post[i]
        return res

