class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numb=list(nums)
        for n in nums:
            numb.append(n)
        return numb
        