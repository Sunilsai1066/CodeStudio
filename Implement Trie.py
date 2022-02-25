from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.Flag = False

Root = Node()
RtCopy = Root

class Trie :
    def __init__(self) :
        self.Root = Root
        self.RtCopy = Root
    
    def insert(self, Word) :
        self.Root = Root
        self.RtCopy = Root
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] == 0):
                self.NextLink = Node()
                self.Root.NodeLinks[ord(letter)-97] = self.NextLink
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                self.Root = self.Root.NodeLinks[ord(letter)-97]
        self.Root.Flag = True

    
    def search(self, Word) :
        self.Root = Root
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                return False
        return self.Root.Flag == True

    def startWith(self, Word) :
        self.Root = Root
        SWith = True
        for letter in Word:
            if(self.Root.NodeLinks[ord(letter)-97] != 0):
                self.Root = self.Root.NodeLinks[ord(letter)-97]
            else:
                SWith = False
                break
        return SWith


# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")
