class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        for s in strs:
            if (c := "".join(sorted(s))) not in seen.keys():
                seen[c] = [s]
            else:
                seen[c].append(s)

        return [seen[s] for s in seen]

            
