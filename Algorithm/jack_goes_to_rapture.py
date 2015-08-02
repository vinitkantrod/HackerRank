from collections import defaultdict,deque
import heapq
N,E=(int(i) for i in raw_input().split())

adj=defaultdict(list)

for _ in xrange(E):
    a,b,w=(int(i) for i in raw_input().split())
    
    adj[a].append((w,b))
    adj[b].append((w,a))

queue = []
visited = set()
queue.append((0,1))
rekt=True

while queue:
    cur = heapq.heappop(queue)
    if cur[1] in visited:
        continue
    visited.add(cur[1])
    if cur[1]==N:
        print cur[0]
        rekt=False
        break
    for a in adj[cur[1]]:
        if a[1] not in visited:
            out = (max(a[0],cur[0]),a[1])
            heapq.heappush(queue,out)
            
if rekt:
    print "NO PATH EXISTS"
