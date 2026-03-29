class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for r in strs:
            s=''.join(sorted(r))
            res[s].append(r)
        return list(res.values())