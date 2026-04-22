class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for st in strs:
            key = ''.join(sorted(st))
            groups[key].append(st)
        
        return list(groups.values())

        