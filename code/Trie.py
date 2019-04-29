class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # leaf is True if node represent the end of the word
        self.leaf = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        if len(key) > 2 and key.isalpha():
            pCrawl = self.root
            length = len(key)
            for level in range(length):
                index = self.charToIndex(key[level])

                # if current character is not present
                if pCrawl.children[index] is None:
                    pCrawl.children[index] = self.getNode()
                pCrawl = pCrawl.children[index]

            # mark last node as leaf
            pCrawl.leaf = True