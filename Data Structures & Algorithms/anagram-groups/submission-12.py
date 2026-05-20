class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            r=' '.join(sorted(i))
            res[r].append(i)
        return list(res.values())