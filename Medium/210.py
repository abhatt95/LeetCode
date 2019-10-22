"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you 
have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of 
them. If it is impossible to finish all courses, return an empty array.
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prerequisite_graph = { num : set() for num in range(numCourses)}
        
        for x,y in prerequisites:
            prerequisite_graph[x].add(y)
            
        def get_start(prerequisite_graph):
            for k,v in prerequisite_graph.items():
                if len(v) == 0:
                    return k 
        
        courses_covered = [] 
        
        while len(courses_covered) < numCourses:
            start = get_start(prerequisite_graph)
            if start == None:
                return []
            courses_covered.append(start)
            if start in prerequisite_graph: del prerequisite_graph[start]
            for k,v in prerequisite_graph.items():
                if start in v:
                    prerequisite_graph[k].remove(start)
         
        return courses_covered
        