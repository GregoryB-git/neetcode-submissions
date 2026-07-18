from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        for i in range(len(strs)):
            sortedS = ''.join(sorted(strs[i]))
            dicts[sortedS].append(strs[i])
        return list(dicts.values())