# always ask bound of input, can it be empty? 
# always make sure intermediate functions are running.
# don't assume input to be integers can be strings.  

"""
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded by 
water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are 
all surrounded by water.

https://leetcode.com/problems/number-of-islands/

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid:
            x_max = len(grid)
        else:
            x_max = 0
        if x_max:
            y_max = len(grid[0])
        else: 
            y_max = 0
        
        def is_valid(x,y):
            if (x>=0 and x<x_max) and (y>=0 and y<y_max):
                return True
            return False
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def cover_adjacent_of(x,y):
            for x_dir,y_dir in directions:
                next_x,next_y = x+x_dir,y+y_dir
                if is_valid(next_x,next_y):
                    if grid[next_x][next_y] == '1':
                        grid[next_x][next_y] = -1
                        cover_adjacent_of(next_x,next_y)
        
        def island_from(x,y):
            # no island possible from this tile
            if grid[x][y] == -1 or grid[x][y] == '0':
                return 0 
            # island starts from this tile, this tile is already covered 
            grid[x][y] = -1 
            cover_adjacent_of(x,y)
            return 1
        
        total_islands = 0
        
        for x in range(0,x_max):
            for y in range(0,y_max):
                total_islands += island_from(x,y)
                
        return total_islands