# https://adventofcode.com/2023/day/09]
# Created by: Menaka S. 14 Dec 2023

import sys
import re

grid = []

def part1and2():
    global grid

    total1 = 0
    total2 = 0

    for line in sys.stdin:
        grid.append([ int(x)  if x != '' else 0 for x in list(re.split('\s+',line.strip()))])
        (l1,l2) = get_end_value()
        total1 +=l1
        total2 +=l2
        grid = []
    return (total1,total2)
         
def get_end_value():
    global grid

    row = 0
    while any(grid[row]):
       grid.append([])
       for j in range(0,len(grid[row])-1): # 6-0-1 = 5
          grid[row+1].append(grid[row][j+1] - grid[row][j])
       row += 1  

    grid[row].append(0)
    for i in range(row-1,-1,-1):
        grid[i].append(grid[i+1][-1] + grid[i][-1]) 
        lastvalue1 = grid[i][-1]

    grid[row].insert(0,0)
    for i in range(row-1,-1,-1):
        grid[i].insert(0,grid[i][0] - grid[i+1][0]) 
        lastvalue2 = grid[i][0]

    return (lastvalue1,lastvalue2)
      
print(part1and2())
