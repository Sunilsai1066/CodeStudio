class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.Equals = 0
        self.StartWith = 0

class Trie:
    def __init__(self):
        self.Main = Node()
        self.Root = self.Main
        self.RtCopy = self.Main

    def insert(self, word):
        self.Root = self.Main
        for letter in word:
            if(self.Root.NodeLinks[ord(letter)-97] == 0):
                self.NewLink = Node()
                self.NewLink.StartWith += 1
                self.Root.NodeLinks[ord(letter)-97] = self.NewLink
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                self.Root.NodeLinks[ord(letter)-97].StartWith += 1
                self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Equals += 1

    def countWordsEqualTo(self, word):
        self.Root = self.Main
        for letter in word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return 0
        return self.Root.Equals

    def countWordsStartingWith(self, word):
        self.Root = self.Main
        for letter in word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return 0
        return self.Root.StartWith

    def erase(self, word):
        self.Root = self.Main
        for letter in word:
            self.Root.NodeLinks[ord(letter)-97].StartWith -= 1
            self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Equals -= 1

