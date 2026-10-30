from lab3_bfs_dfs import graph,bfs,dfs
from lab3_depth_search import dls,iddfs
from lab3_ucs import wgraph,ucs
cyc={"A":["B"],"B":["C"],"C":["A","D"],"D":[]}
unreach=dict(graph);unreach["H"]=[]
wunreach=dict(wgraph);wunreach["H"]=[]
wcyc={"A":[("B",1)],"B":[("C",1)],"C":[("A",1),("D",1)],"D":[]}
def check(name,got,expected):
    print("PASS" if got==expected else "FAIL",name,"| got",got,"| expected",expected)
print("Start equals goal")
check("BFS",bfs(graph,"A","A")[0],["A"])
check("DFS",dfs(graph,"A","A")[0],["A"])
check("DLS limit 0",dls(graph,"A","A",0)[:2],("FOUND",["A"]))
check("IDDFS",iddfs(graph,"A","A",3)[:2],("FOUND",["A"]))
check("UCS",ucs(wgraph,"A","A")[:2],(["A"],0))
print("Unreachable goal H")
check("BFS",bfs(unreach,"A","H")[0],None)
check("DFS",dfs(unreach,"A","H")[0],None)
check("DLS limit 2 is only CUTOFF",dls(unreach,"A","H",2)[:2],("CUTOFF",None))
check("DLS limit 4 is FAILURE",dls(unreach,"A","H",4)[:2],("FAILURE",None))
check("IDDFS max depth 5",iddfs(unreach,"A","H",5)[:2],("FAILURE",None))
check("UCS",ucs(wunreach,"A","H")[:2],(None,None))
print("Graph with cycle A-B-C-A, goal D")
check("BFS",bfs(cyc,"A","D")[0],["A","B","C","D"])
check("DFS",dfs(cyc,"A","D")[0],["A","B","C","D"])
check("DLS limit 3",dls(cyc,"A","D",3)[:2],("FOUND",["A","B","C","D"]))
check("DLS limit 2",dls(cyc,"A","D",2)[:2],("CUTOFF",None))
check("IDDFS",iddfs(cyc,"A","D",5)[:2],("FOUND",["A","B","C","D"]))
check("UCS",ucs(wcyc,"A","D")[:2],(["A","B","C","D"],3))
print("Negative edge cost is rejected by UCS")
try:
    ucs({"A":[("B",-1)],"B":[]},"A","B")
    print("FAIL no error raised")
except ValueError as e:
    print("PASS ValueError:",e)
