class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        s = []
        mat = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b / a),
        }

        while i < len(tokens):
            if (n := tokens[i]).isnumeric() or len(n) > 1: # account for negatives
                s.append(int(n))
            else:
                # print(s, n)
                x = (mat[n](s.pop(), s.pop()))
                # print(x)
                s.append(x)

            i += 1
        
        return s[0]

                

