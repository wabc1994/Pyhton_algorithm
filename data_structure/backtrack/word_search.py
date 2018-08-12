'''
Given a matrix of words and a list of words to search, return a list of words that exists in the board
This is Word Search II on LeetCode
board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']
         ]
words = ["oath","pea","eat","rain"]
'''
import unittest

def find_words(board, words):
    trie ={}
    for word in words:
        curr_trie =  trie
        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
        curr_trie['#'] = '#'

    "构造一个空的集合操作"
    result = set()
    "构造二维数组"
    used = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board(0))):
            backtracking(board, i,j, trie, '', result)

    return list(result)

"""

"""

def backtracking(board, i ,j, trie, pre, used, result):
    if '#' in trie:
        result.add(pre)

    if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
        return

    if not used[i][j]  and board[i][j] in trie:
        used[i][j] = True
        backtracking(board,i+1,j,trie[board[i][j]],pre+board[i][j],used,result)
        backtracking(board,i,j+1,trie[board[i][j]],pre+board[i][j],used,result)
        backtracking(board,i-1,j,trie[board[i][j]],pre+board[i][j],used,result)
        backtracking(board,i,j-1,trie[board[i][j]],pre+board[i][j],used,result)
        used[i][j] = False


class MyTests(unittest.TestCase):
    def test_normal(self):
        board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']
         ]

        words = ["oath","pea","eat","rain"]
        self.assertEqual(find_words(board, words), ['oath', 'eat'])

    def test_none(self):
        board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']
         ]

        words = ["chicken", "nugget", "hello", "world"]
        self.assertEqual(find_words(board, words), [])

    def test_empty(self):
        board = []
        words = []
        self.assertEqual(find_words(board, words), [])

    def test_uneven(self):
        board = [
         ['o','a','a','n'],
         ['e','t','a','e']
        ]
        words = ["oath","pea","eat","rain"]
        self.assertEqual(find_words(board, words), ['eat'])

    def test_repeat(self):
        board = [
        ['a','a','a'],
        ['a','a','a'],
        ['a','a','a']
        ]
        words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        self.assertTrue(len(find_words(board, words))==5)

if __name__=="__main__":
    unittest.main()




