def FindAllSubsets(n, arr):
    FinRes = []
    Start,End = 0,n-1
    def subSets(Lis,Res,Start,End,FinRes):
        if(Start > End):
            FinRes.append(Res[:])
            return
        Res.append(Lis[Start])
        subSets(Lis,Res,Start+1,End,FinRes)
        Res.pop()
        subSets(Lis,Res,Start+1,End,FinRes)
    
    subSets(arr,[],Start,End,FinRes)
    return FinRes
