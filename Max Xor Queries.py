class TrieNode:
    def __init__(self):
        self.NodeLinks = [-1,-1]

class Trie:
    def __init__(self):
        self.Root = TrieNode()
        
    def Insert(self,Num):
        Node = self.Root
        for i in range(31,-1,-1):
            Bit = (Num >> i)&1
            if(Node.NodeLinks[Bit] == -1):
                NewLink = TrieNode()
                Node.NodeLinks[Bit] = NewLink
            Node = Node.NodeLinks[Bit]
            
    def findMax(self,Num):
        Node = self.Root
        SubMax = 0
        for i in range(31,-1,-1):
            Bit = (Num >> i) & 1
            if(Node.NodeLinks[1-Bit] != -1):
                SubMax = SubMax | (1<<i)
                Node = Node.NodeLinks[1-Bit]
            else:
                Node = Node.NodeLinks[Bit]
        return SubMax
    
def maxXorQueries(nums, queries):
    QLen,NLen,Ind = len(queries),len(nums),0
    Res = [0]*QLen
    Tr = Trie()
    for query in range(QLen):queries[query].append(query)
    queries.sort(key = lambda x:x[1])
    nums.sort()
    for query in queries:
        if(query[1] < nums[0]):
            Res[query[2]] = -1
        else:
            while(Ind < NLen and nums[Ind] <= query[1]):
                Tr.Insert(nums[Ind])
                Ind += 1
            Res[query[2]] = Tr.findMax(query[0])
     
    return Res
