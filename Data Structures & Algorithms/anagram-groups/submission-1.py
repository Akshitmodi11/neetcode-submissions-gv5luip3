class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. Use defaultdict so we don't have to check "if key in ansMap"

        ans_map = defaultdict(list)
        if len(strs)==0:
            return [[""]]
        
        for s in strs:
            # 2. Create the 26-count array (equivalent to int[] count in Java)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # 3. Use the count as the key. 
            # In Python, lists are "mutable" (can change), so they can't be keys.
            # Tuples are "immutable," so we convert the list to a tuple.
            key = tuple(count)
            
            # 4. Add the original string to the list for that key
            ans_map[key].append(s)
            
        # 5. Return only the groups (values)
        return list(ans_map.values())