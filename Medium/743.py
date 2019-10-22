"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.


"""
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for s,d,c in times:
            graph[s].append((d,c))
            
        queue = [(0,K)]
        covered_nodes = {}
        
        while queue:
            c,d = heapq.heappop(queue)
            if d in covered_nodes: continue
            covered_nodes[d] = c
            for neighbour,c_e in graph[d]:
                if neighbour not in covered_nodes:
                    heapq.heappush(queue,(c+c_e,neighbour))
        
        return max(covered_nodes.values()) if len(covered_nodes) == N else -1
            
        
