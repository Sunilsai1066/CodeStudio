from typing import *
class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        self.End = False
        
def completeString(n,a):
    Root = Node()
    RtCopy = Root
    Res = ""
    ResMaxVal = 0
    for word in a:
        Root = RtCopy
        for letter in word:
            if(Root.NodeLinks[ord(letter)-97] == 0):
                NewNode = Node()
                Root.NodeLinks[ord(letter)-97] = NewNode
                Root = Root.NodeLinks[ord(letter)-97]
            else:
                Root = Root.NodeLinks[ord(letter)-97]
        Root.End = True
    
    for word in a:
        Root = RtCopy
        WordLen = len(word)
        TrueCount = 0
        if(len(word) >= ResMaxVal):
            for letter in word:
                if(Root.NodeLinks[ord(letter)-97] != 0):
                    Root = Root.NodeLinks[ord(letter)-97]
                    if(Root.End == True):
                        TrueCount += 1
                    else:
                        break
            if(WordLen == TrueCount and WordLen >= ResMaxVal):
                if(Res != None and word<Res):
                    Res = word
                    ResMaxVal = WordLen
                else:
                    Res = word
                    ResMaxVal = WordLen
    return Res if Res else None
