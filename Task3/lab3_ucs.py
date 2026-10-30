import heapq
from lab3_bfs_dfs import bfs
wgraph={"A":[("B",1),("C",5)],"B":[("D",4),("E",1)],"C":[("F",2),("G",7)],"D":[],"E":[("G",1)],"F":[],"G":[]}
def ucs(g,start,goal,show=False):
    for u in g:
        for v,w in g[u]:
            if w<0:raise ValueError("negative edge cost")
    count=0
    heap=[(0,count,start,[start])];best={start:0};done=set();order=[]
    while heap:
        cost,_,node,path=heapq.heappop(heap)
        if node in done:continue
        done.add(node);order.append((node,cost))
        if show:print("UCS step",len(order),"| processed",node,"| cost",cost,"| path",path)
        if node==goal:
            if show:print("   frontier after step",sorted([(c,n) for c,_,n,_ in heap]))
            return path,cost,order
        for v,w in g[node]:
            nc=cost+w
            if v not in done and nc<best.get(v,float("inf")):
                best[v]=nc;count+=1
                heapq.heappush(heap,(nc,count,v,path+[v]))
        if show:print("   frontier after step",sorted([(c,n) for c,_,n,_ in heap]))
    return None,None,order
def path_cost(g,path):
    total=0
    for a,b in zip(path,path[1:]):
        total+=dict(g[a])[b]
    return total
if __name__=="__main__":
    print("Task 3: weighted graph (C to G is the added corridor)")
    for u in wgraph:
        for v,w in wgraph[u]:print("  ",u,"->",v,"cost",w)
    p,c,o=ucs(wgraph,"A","G",True)
    print("UCS path:",p)
    print("UCS reported cost:",c)
    print("UCS hops:",len(p)-1)
    print("UCS processing order:",[n for n,_ in o])
    print("UCS independently summed cost:",path_cost(wgraph,p))
    topo={u:[v for v,w in wgraph[u]] for u in wgraph}
    bp,bo=bfs(topo,"A","G")
    print("BFS path on same topology:",bp)
    print("BFS hops:",len(bp)-1)
    print("BFS independently summed cost:",path_cost(wgraph,bp))
    print("BFS processing order:",bo)
    print("Fewest hops route is BFS:",len(bp)-1,"hops, cost",path_cost(wgraph,bp))
    print("Cheapest route is UCS:",len(p)-1,"hops, cost",path_cost(wgraph,p))
