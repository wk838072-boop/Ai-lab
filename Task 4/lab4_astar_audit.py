import heapq
import sys
graph={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
h={"S":5,"A":4,"B":4,"C":2,"G":0}
zero={n:0 for n in graph}
def astar(g,hv,start,goal,show=False):
    for u in g:
        for v,w in g[u]:
            if w<0:raise ValueError("negative edge cost")
    pq=[(hv[start],0,start,[start])];best={start:0};processed=[];expanded=[];stale=0
    if show:print("start frontier",[(start,"g=0","h="+str(hv[start]),"f="+str(hv[start]))])
    while pq:
        f,gc,node,path=heapq.heappop(pq)
        if gc!=best[node]:
            stale+=1
            if show:print("stale entry ignored:",node,"with g",gc)
            continue
        processed.append(node)
        if show:print("Processed",node,"| g =",gc,"| h =",hv[node],"| f = g + h =",gc,"+",hv[node],"=",gc+hv[node],"| path",path)
        if node==goal:
            if show:print("   goal processed, logged but not counted as expanded")
            return gc,path,processed,expanded,stale
        expanded.append(node)
        for nxt,w in g.get(node,[]):
            ng=gc+w
            if ng<best.get(nxt,float("inf")):
                best[nxt]=ng
                heapq.heappush(pq,(ng+hv[nxt],ng,nxt,path+[nxt]))
                if show:print("   ",node,"->",nxt,"| g =",gc,"+",w,"=",ng,"| h =",hv[nxt],"| f =",ng,"+",hv[nxt],"=",ng+hv[nxt],"| pushed")
            elif show:print("   ",node,"->",nxt,"| g =",gc,"+",w,"=",ng,"| not better than",best[nxt],"| skipped")
        if show:print("   frontier after expanding",node,sorted([(ff,gg,nn) for ff,gg,nn,_ in pq]),"as (f, g, node)")
    return None,None,processed,expanded,stale
def supplied_astar(g,hv,start,goal):
    pq=[(hv[start],0,start,[start])];best={start:0}
    while pq:
        f,gc,node,path=heapq.heappop(pq)
        if node==goal:return gc,path
        if gc!=best[node]:continue
        for nxt,w in g.get(node,[]):
            ng=gc+w
            if ng<best.get(nxt,float("inf")):
                best[nxt]=ng
                heapq.heappush(pq,(ng+hv[nxt],ng,nxt,path+[nxt]))
def path_cost(g,path):
    total=0
    for a,b in zip(path,path[1:]):
        total+=dict(g[a])[b]
    return total
def true_remaining(g,goal):
    return {n:astar(g,{x:0 for x in g},n,goal)[0] for n in g}
def inconsistent_edges(g,hv):
    bad=[]
    for u in g:
        for v,w in g[u]:
            if hv[u]>w+hv[v]:bad.append((u,v))
    return bad
def audit(g,hv,goal,label):
    print("Heuristic audit for",label)
    tr=true_remaining(g,goal)
    for n in g:print("   ",n,"h =",hv[n],"true remaining =",tr[n],"admissible:",hv[n]<=tr[n])
    for u in g:
        for v,w in g[u]:
            print("    edge",u,"->",v,"| h(u) =",hv[u],"<= cost + h(v) =",w,"+",hv[v],"=",w+hv[v],":",hv[u]<=w+hv[v])
    print("    inconsistent edges:",inconsistent_edges(g,hv))
def summary(label,res,g):
    cost,path,processed,expanded,stale=res
    print(label)
    print("   returned path:",path)
    print("   returned cost:",cost)
    print("   independently summed cost:",path_cost(g,path))
    print("   processed order (goal included):",processed)
    print("   expanded nodes (goal excluded):",expanded)
    print("   expansion count:",len(expanded))
    print("   stale entries ignored:",stale)
def task1():
    print("Task 1: hand calculation check, supplied graph and heuristic, start S, goal G")
    print("Tie break: the queue orders by f, then g, then node name")
    astar(graph,h,"S","G",True)
def task2():
    print("Task 2: A* with supplied h compared with UCS control (h = 0 for every node)")
    audit(graph,h,"G","supplied heuristic")
    ra=astar(graph,h,"S","G",True)
    summary("A* result",ra,graph)
    print("UCS control trace")
    ru=astar(graph,zero,"S","G",True)
    summary("UCS result",ru,graph)
    print("Comparison table")
    print("   method | path | cost | expansions | processed")
    print("   A*  |",ra[1],"|",ra[0],"|",len(ra[3]),"|",ra[2])
    print("   UCS |",ru[1],"|",ru[0],"|",len(ru[3]),"|",ru[2])
    print("Supplied astar function agrees:",supplied_astar(graph,h,"S","G")==(ra[0],ra[1]))
def task3():
    print("Task 3: overestimate experiment, only h(C) changes")
    h2=dict(h);h2["C"]=10
    tr=true_remaining(graph,"G")
    print("h(C) original:",h["C"],"| modified:",h2["C"],"| true remaining cost of C:",tr["C"])
    print("Overestimate:",h2["C"]>tr["C"])
    audit(graph,h2,"G","modified heuristic h(C)=10")
    rb=astar(graph,h,"S","G")
    print("Modified run trace")
    rm=astar(graph,h2,"S","G",True)
    summary("Original h result",rb,graph)
    summary("Modified h result",rm,graph)
    print("Path changed:",rb[1]!=rm[1])
    print("Cost changed:",rb[0]!=rm[0])
    print("Expansion count changed:",len(rb[3])!=len(rm[3]))
    print("Node C was expanded in the modified run:","C" in rm[3])
if __name__=="__main__":
    which=sys.argv[1] if len(sys.argv)>1 else "all"
    if which in("1","all"):task1()
    if which in("2","all"):task2()
    if which in("3","all"):task3()
