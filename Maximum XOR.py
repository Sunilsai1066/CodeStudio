class Node:
    def __init__(self):
        self.NodeLinks = [-1,-1]
        
def maxXOR(n, m, arr1, arr2):
    Root = Node()
    RtCopy = Root
    BinArrayLis = [format(i,'032b') for i in arr1]
    for num in BinArrayLis:
        Root = RtCopy
        for Strbit in num:
            bit = int(Strbit)
            if(Root.NodeLinks[bit] == -1):
                NewLink = Node()
                Root.NodeLinks[bit] = NewLink
                Root = Root.NodeLinks[bit]
            else:
                Root = Root.NodeLinks[bit]
    Res = 0
    def FindRes(X):
        MaxBits = ""
        XBits = format(X,'032b')
        Root = RtCopy
        for Xbit in XBits:
            XbitInt = int(Xbit)
            Taken = 0
            if(XbitInt == 1 and Root.NodeLinks[0] != -1):
                MaxBits += '1'
            elif(XbitInt == 1 and Root.NodeLinks[1] != -1):
                MaxBits += '0'
                Taken = 1
            elif(XbitInt == 0 and Root.NodeLinks[1] != -1):
                MaxBits += '1'
                Taken = 1
            else:
                MaxBits += '0'
            Root = Root.NodeLinks[Taken]
        return int(MaxBits,2)
    for num in arr2:
        Val = FindRes(num)
        if(Val > Res):
            Res = Val
    return Res

