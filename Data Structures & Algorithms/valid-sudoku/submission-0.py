class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        seen_row = [set() for i in range(n)]
        seen_col = [set() for i in range(m)]
        seen_box = [set() for i in range(9)]

        for i in range(n):
            for j in range(m):
                k = board[i][j]
                if k == '.': continue
                # check row and col
                for check, idx in [(seen_row, i), (seen_col, j)]:
                    if k in check[idx]: return False
                    else: check[idx].add(k)
                    
                r = i // 3
                c = j // 3

                if k in seen_box[3*r + c]:
                    return False
                else:
                    seen_box[3*r + c].add(k)

        return True
        
                






        # for a in range(3):
        #     for b in range(3):
        #         for i in range(3):
        #             row = board[a * 3 + i]
        #             col = b * 3
        #             items = row[col:col+3]
        #             print(items)

        return False

