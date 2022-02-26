class Node:
    def __init__(self):
        self.NodeLinks = [0]*26
        
def countDistinctSubstrings(s):
    Count = 0
    Root = Node()
    RtCopy = Root
    for MainL in range(len(s)):
        Root = RtCopy
        for SubL in range(MainL,len(s)):
            if(Root.NodeLinks[ord(s[SubL])-97] == 0):
                NewLink = Node()
                Root.NodeLinks[ord(s[SubL])-97] = NewLink
                Root = Root.NodeLinks[ord(s[SubL])-97]
                Count += 1
            else:
                Root = Root.NodeLinks[ord(s[SubL])-97]
    return Count+1
