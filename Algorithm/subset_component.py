from sys import stderr
from copy import copy
N = 64

#Handy debug function
def err(items):
    string = ""
    for item in items: string += str(item) + " "
    string += "\n"
    stderr.write(string)
    return

def buildSet(num):
    #Decompose num into binary and store where there are 1s
    #According to the problem statement, the set s contains
    #  the vertices of a graph that are connected to one another
    #That is, the largest connected component of the 64-node graph
    (s,i) = (set(),0)
    while num > 0:
        if num % 2: s.add(i)
        (num, i) = (num / 2, i + 1)
        pass
    return s

def merge(a,b):
    #Union two sets and see if there's anything in common
    union = copy(a)
    overlap = False
    for elem in b:
        if elem in a: overlap = True
        else: union.add(elem)
    return (union, overlap)

def solve(sets, start, n, prev, prevContrib):
    #Recursive function that tests every combo of numbers/components
    ans = 0
    for i in range(start, n):
        component = sets[i]
        
        #If the size of the largest component is bigger than 1...
        if len(component) > 1:
            #Upon incorporating the component, the bits change
            (newBits, overlap) = merge(prev, component)
            #If just starting or there's overlap between prev. and current component
            #  there's just one component larger than 1
            if len(prev) == 0 or overlap: contrib = N - len(newBits) + 1
            #Otherwise, there are two
            else: contrib = prevContrib + 1 - len(component)
            pass
        
        #Otherwise, this number contributes no new edges
        else: (newBits, contrib) = (prev, prevContrib)
        
        ans += contrib + solve(sets, i+1, n, newBits, contrib)
        pass
    return ans

if __name__ == "__main__":
    n = int(raw_input().strip())
    sets = []
    for num in map(int,raw_input().strip().split()):
        s = buildSet(num)
        sets.append(s)
        pass
    
    print N + solve(sets, 0, n, set(), 64)
    pass
