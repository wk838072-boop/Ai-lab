from math import log2
def minimax(depth,index,max_turn,scores,target,counter):
    if depth==target:
        counter[0]+=1
        return scores[index]
    left=minimax(depth+1,index*2,not max_turn,scores,target,counter)
    right=minimax(depth+1,index*2+1,not max_turn,scores,target,counter)
    return max(left,right) if max_turn else min(left,right)
def alphabeta(depth,index,max_turn,scores,target,alpha,beta,counter):
    if depth==target:
        counter[0]+=1
        return scores[index]
    if max_turn:
        value=float("-inf")
        for i in range(2):
            value=max(value,alphabeta(depth+1,index*2+i,False,scores,target,alpha,beta,counter))
            alpha=max(alpha,value)
            if alpha>=beta:
                break
        return value
    value=float("inf")
    for i in range(2):
        value=min(value,alphabeta(depth+1,index*2+i,True,scores,target,alpha,beta,counter))
        beta=min(beta,value)
        if alpha>=beta:
            break
    return value
def run_test(label,scores):
    target=int(log2(len(scores)))
    minimax_count=[0]
    alphabeta_count=[0]
    minimax_value=minimax(0,0,True,scores,target,minimax_count)
    alphabeta_value=alphabeta(0,0,True,scores,target,float("-inf"),float("inf"),alphabeta_count)
    print(label)
    print("Scores:",scores)
    print("Minimax value:",minimax_value)
    print("Minimax leaves evaluated:",minimax_count[0])
    print("Alpha-Beta value:",alphabeta_value)
    print("Alpha-Beta leaves evaluated:",alphabeta_count[0])
    print("Values match:",minimax_value==alphabeta_value)
    print()
run_test("Test 1: Original branch order",[3,5,2,9,3,5,2,9])
run_test("Test 2: Reordered branches",[9,2,5,3,9,2,5,3])
run_test("Test 3: Edge case with equal leaf values",[4,4,4,4,4,4,4,4])
