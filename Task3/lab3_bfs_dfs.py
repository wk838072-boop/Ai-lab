from collections import deque
graph={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
def bfs(g,start,goal,show=False):
    q=deque([(start,[start])]);seen={start};order=[]
    while q:
        node,path=q.popleft()
        order.append(node)
        if show:print("BFS step",len(order),"| processed",node,"| path",path)
        if node==goal:
            if show:print("   frontier after step",[x[0] for x in q])
            return path,order
        for n in g[node]:
            if n not in seen:
                seen.add(n);q.append((n,path+[n]))
        if show:print("   frontier after step",[x[0] for x in q])
    return None,order
def dfs(g,start,goal,show=False):
    stack=[(start,[start])];seen=set();order=[]
    while stack:
        node,path=stack.pop()
        if node in seen:
            if show:print("DFS skipped duplicate",node)
            continue
        order.append(node)
        if show:print("DFS step",len(order),"| processed",node,"| path",path)
        if node==goal:
            if show:print("   stack after step (top is last)",[x[0] for x in stack])
            return path,order
        seen.add(node)
        for n in reversed(g[node]):stack.append((n,path+[n]))
        if show:print("   stack after step (top is last)",[x[0] for x in stack])
    return None,order
def supplied_bfs(start,goal):
    q=deque([(start,[start])]);seen={start}
    while q:
        node,path=q.popleft()
        if node==goal:return path
        for n in graph[node]:
            if n not in seen:
                seen.add(n);q.append((n,path+[n]))
def supplied_dfs(start,goal):
    stack=[(start,[start])];seen=set()
    while stack:
        node,path=stack.pop()
        if node==goal:return path
        if node in seen:continue
        seen.add(node)
        for n in reversed(graph[node]):stack.append((n,path+[n]))
if __name__=="__main__":
    print("Task 1: manual trace check on the original A-G graph, start A, goal G")
    bp,bo=bfs(graph,"A","G",True)
    print("BFS final path:",bp)
    print("BFS visit order:",bo)
    dp,do=dfs(graph,"A","G",True)
    print("DFS final path:",dp)
    print("DFS visit order:",do)
    print("Supplied BFS code path:",supplied_bfs("A","G"))
    print("Supplied DFS code path:",supplied_dfs("A","G"))
    print("Paths match supplied code:",bp==supplied_bfs("A","G") and dp==supplied_dfs("A","G"))
    print("Visit counts including goal: BFS",len(bo),"DFS",len(do))
