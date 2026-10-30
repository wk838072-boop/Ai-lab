from lab3_bfs_dfs import graph
def dls(g,start,goal,limit):
    log=[]
    def rec(node,path,depth):
        log.append(node)
        if node==goal:return "FOUND",path
        nexts=[n for n in g[node] if n not in path]
        if depth==limit:
            return ("CUTOFF",None) if nexts else ("FAILURE",None)
        cut=False
        for n in nexts:
            s,p=rec(n,path+[n],depth+1)
            if s=="FOUND":return s,p
            if s=="CUTOFF":cut=True
        return ("CUTOFF",None) if cut else ("FAILURE",None)
    s,p=rec(start,[start],0)
    return s,p,log
def iddfs(g,start,goal,max_depth):
    attempts=[];total=0
    status="FAILURE"
    for limit in range(max_depth+1):
        s,p,log=dls(g,start,goal,limit)
        total+=len(log)
        attempts.append((limit,s,len(log)))
        status=s
        if s=="FOUND":return s,p,attempts,total
        if s=="FAILURE":break
    return status,None,attempts,total
if __name__=="__main__":
    print("Task 2: DLS on the original graph, start A, goal G, root depth 0")
    for limit in [1,2,3,4]:
        s,p,log=dls(graph,"A","G",limit)
        print("DLS limit",limit,"| status",s,"| path",p,"| nodes processed",len(log),log)
    print("Task 2: IDDFS on the original graph")
    for m in [1,2,3,4]:
        s,p,att,total=iddfs(graph,"A","G",m)
        print("IDDFS max depth",m,"| status",s,"| path",p,"| limits attempted",[a[0] for a in att],"| total nodes processed",total)
        for a in att:print("   limit",a[0],a[1],"nodes processed",a[2])
