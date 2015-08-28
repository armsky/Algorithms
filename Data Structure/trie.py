class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if word:
            node = self.root
            for char in word:
                child = node.children.get(char)
                if not child:
                    child = TrieNode()
                    node.children[char] = child
                node = child
            node.is_word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        if word:
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_word
        else:
            return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        if prefix:
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True
        return False

trie = Trie()
trie.insert("a")
trie.insert("ab")
print trie.search("a")
print trie.search("ab")
