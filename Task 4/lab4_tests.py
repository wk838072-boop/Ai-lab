from lab4_astar_audit import graph,h,zero,astar,supplied_astar,inconsistent_edges,true_remaining
def check(name,got,expected):
    print("PASS" if got==expected else "FAIL",name,"| got",got,"| expected",expected)
unreach=dict(graph);unreach["H"]=[]
hu=dict(h);hu["H"]=0
stale={"S":[("A",1),("B",2)],"A":[("C",5)],"B":[("C",1)],"C":[("G",10)],"G":[]}
zs={n:0 for n in stale}
print("Start equals goal")
r=astar(graph,h,"S","S")
check("A* cost and path",(r[0],r[1]),(0,["S"]))
check("A* expansions",len(r[3]),0)
print("Unreachable goal H")
r=astar(unreach,hu,"S","H")
check("A* cost and path",(r[0],r[1]),(None,None))
check("A* expanded every reachable node",sorted(r[3]),["A","B","C","G","S"])
print("Stale entry case")
r=astar(stale,zs,"S","G")
check("cost and path",(r[0],r[1]),(13,["S","B","C","G"]))
check("stale entries ignored",r[4],1)
check("expanded order",r[3],["S","A","B","C"])
print("Heuristic quality")
check("supplied h has no inconsistent edges",inconsistent_edges(graph,h),[])
h2=dict(h);h2["C"]=10
check("h(C)=10 breaks edge",inconsistent_edges(graph,h2),[("C","G")])
check("true remaining costs",true_remaining(graph,"G"),{"S":6,"A":5,"B":5,"C":3,"G":0})
print("Comparison checks")
check("supplied code matches astar",supplied_astar(graph,h,"S","G"),(6,["S","A","C","G"]))
check("A* expansions",len(astar(graph,h,"S","G")[3]),3)
check("UCS control expansions",len(astar(graph,zero,"S","G")[3]),4)
r=astar(graph,h2,"S","G")
check("overestimate result",(r[0],r[1]),(9,["S","B","G"]))
print("Negative edge cost is rejected")
try:
    astar({"S":[("G",-1)],"G":[]},{"S":0,"G":0},"S","G")
    print("FAIL no error raised")
except ValueError as e:
    print("PASS ValueError:",e)
