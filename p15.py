# https://adventofcode.com/2023/day/15
# Created by: Menaka S. 15 Dec 2023

import sys
import re
from functools import reduce

def part1and2():
    for line in sys.stdin:
        line = line.strip('\n')
        parts = re.split(',',line)
        total1 = 0
        for part in parts:
            total1 += hash(part)
            placelens(part)
    print(total1,fpower())
 

def fpower():
   global boxes
   return sum([ sum([ (box+1) * (i+1) * boxes[box][i][1] for i in range(0,len(boxes[box]))]) for box in boxes])
   
def hash(text):
   return reduce(lambda a,b : ((a + ord(b)) * 17) %256 , list(text), 0)

def placelens(text):
   global boxes

   label,fl = text.split('=') if '=' in text else [text[:-1],0]
   box = hash(label)   

   if box not in boxes and '=' in text:
       boxes[box] = [(label,int(fl))]
   elif box in boxes:
       item  = [x for x in boxes[box] if x[0] == label]
       if len(item):
           ind =boxes[box].index(item[0])
           if '=' in text: 
              boxes[box][ind] = (label,int(fl))
           else:
              del boxes[box][ind]
       elif '=' in text: 
              boxes[box].append((label,int(fl)))

boxes = {}
part1and2()
