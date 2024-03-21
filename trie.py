# https://www.codingninjas.com/studio/problems/implement-trie_631356?leftPanelTabValue=PROBLEM
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
# Recursion limit is given in the question mentioned above nothing to do with the implementation

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        node = self.root
        for char in string:
            pos = ord(char) - ord('a')
            if not node.links[pos]:
                node.links[pos] = Node()
            node = node.links[pos]
        node.end_of_word = True

    
    def search(self, word):
        node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if not node.links[pos]:
                return False
            node = node.links[pos]
            
        return node.end_of_word

        
    def startWith(self, prefix):
        node = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if not node.links[pos]:
                return False
            node = node.links[pos]
        return True


    def allWordsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if not node.links[pos]:
                return []  # If the prefix does not exist in the Trie, return an empty list
            node = node.links[pos]

        words = []
        self._collectWordsWithPrefix(node, prefix, words)
        return words

    def _collectWordsWithPrefix(self, node, prefix, words):
        if node.end_of_word:
            words.append(prefix)

        for i, child in enumerate(node.links):
            if child:
                self._collectWordsWithPrefix(child, prefix + chr(i + ord('a')), words)

def main():
    # Create a Trie instance
    trie = Trie()

    # Insert some words into the Trie
    words = ["apple", "banana", "orange", "pear"]
    for word in words:
        trie.insert(word)

    # Test search function
    search_words = ["apple", "banana", "peach", "grape"]
    for word in search_words:
        if trie.search(word):
            print(word, "is present in the Trie")
        else:
            print(word, "is not present in the Trie")

    # Test startWith function
    prefixes = ["app", "ban", "pea", "gr"]
    for prefix in prefixes:
        if trie.startWith(prefix):
            print("Some word in the Trie starts with", prefix)
        else:
            print("No word in the Trie starts with", prefix)

# Test allWordsWithPrefix function
    prefixes = ["app", "ban", "pea", "gr"]
    for prefix in prefixes:
        words = trie.allWordsWithPrefix(prefix)
        if words:
            print(prefix, "has words starting with it:", words)
        else:
            print(prefix, "does not have words starting with it")

if __name__ == "__main__":
    main()
