class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(row, column, node, word):
            if (row < 0 or column < 0
                or row == ROWS or column == COLS or
                (row, column) in visit or board[row][column] not in node.children):
                return
            visit.add((row, column))
            node = node.children[board[row][column]]
            word += board[row][column]
            if node.end:
                res.add(word)
            
            dfs(row - 1, column, node, word)
            dfs(row + 1, column, node, word)
            dfs(row, column - 1, node, word)
            dfs(row, column + 1, node, word)
            visit.remove((row, column))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)