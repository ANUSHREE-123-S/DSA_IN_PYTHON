class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        empty=[]
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    empty.append((r,c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3+(c//3)].add(val)
        def backtrack(idx=0):
            if idx==len(empty):
                return True
            r,c = empty[idx]
            box_index=(r//3)*3+(c//3)
            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_index]:
                    board[r][c]=ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_index].add(ch)

                    if backtrack(idx+1):
                        return True

                    board[r][c]='.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_index].remove(ch)

            return False
        backtrack()
