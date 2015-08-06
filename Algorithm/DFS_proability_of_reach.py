# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# globals
input_list = []
ptr = 0

def path_exists(s,d,graph,visited):
    if s == d: 
        return True
    visited.append(s)
    adj=graph[s]
    for i in adj:
        if i not in visited and path_exists(i,d,graph,visited):
            return True
    return False

def find_probability(N,graph,probs):
    probability = 0.0
    target = str(N+1)
    sorted_list = sorted(graph.keys(),key=int)
    for p in sorted_list:
        visited = []
        if p == target:
            continue
        if path_exists(p,target,graph,visited):
            probability += probs[p]
        else:
            probability = 0
            break
    print str(int(probability))

def driver():
    global ptr
    T = int(input_list.pop(0))
    
    while ptr < len(input_list)-1:
        MAIN_GRAPH = {}
        probabilities = {}
        N = int(input_list[ptr])
        for i in range(N+1):
            ptr += 1
            key = str(ptr)
            paths = input_list[ptr].split(' ')[1:]
            MAIN_GRAPH[str(i+1)] = paths
        ptr += 1
        prob_list = input_list[ptr].split(' ')
        for idx,val in enumerate(prob_list):
            probabilities[str(idx+1)] = float(val)

        find_probability(N,MAIN_GRAPH,probabilities)
        ptr += 1
    return MAIN_GRAPH

# main
for line in sys.stdin:
    input_list.append(line.strip())
driver()
