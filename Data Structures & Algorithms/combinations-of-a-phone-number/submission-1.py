class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtc = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "prqs",
            8: "tuv",
            9: "wxyz",
        }

        if len(digits) < 1:
            return []

        dtoc = [dtc[int(i)] for i in digits]
        res = set()

        def backtrack(i, st):
            if len(st) == len(digits):
                return res.add(st)
            
            for c in dtoc[i]:
                backtrack(i+1, st + c)
        
        backtrack(0, "")
            
        return list(res)





                
