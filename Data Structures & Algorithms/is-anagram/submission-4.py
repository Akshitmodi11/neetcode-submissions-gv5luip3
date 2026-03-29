class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
        
        for j in range(len(t)):
            if t[j] not in count:
                return False
            count[t[j]]-=1
            if count[t[j]]<0:
                return False
        return True





        