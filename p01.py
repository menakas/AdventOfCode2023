# https://adventofcode.com/2023/day/1
# Created by: Menaka S. 1 Dec 2023

import sys

numbers = {
   'one': '1',
   'two' : '2',
   'three' : '3',
   'four' : '4',
   'five' : '5',
   'six' : '6',
   'seven' : '7',
   'eight' : '8',
   'nine' : '9',
   '1': '1',
   '2' : '2',
   '3' : '3',
   '4' : '4',
   '5' : '5',
   '6' : '6',
   '7' : '7',
   '8' : '8',
   '9' : '9'
}


def part1(text):
    number = ''
    for i in range(0,len(text)):
        if i+1 <= len(text) and text[i:i+1] in numbers:
            number = numbers[text[i:i+1]]
            break
    for i in range(len(text)-1,-1,-1):
        if i >= 0 and text[i:i+1] in numbers:
            number += numbers[text[i:i+1]]
            break
    #print(text,int(number)) 
    return int(number)

def part2(text):
    number = ''
    for i in range(0,len(text)):
        if i+1 <= len(text) and text[i:i+1] in numbers:
            number = numbers[text[i:i+1]]
            break
        elif i+3 <= len(text) and text[i:i+3] in numbers:
            number = numbers[text[i:i+3]]
            break
        elif i+4 <= len(text) and text[i:i+4] in numbers:
            number = numbers[text[i:i+4]]
            break
        elif i+5 <= len(text) and text[i:i+5] in numbers:
            number = numbers[text[i:i+5]]
            break

    for i in range(len(text)-1,-1,-1):
        if i >= 0 and text[i:i+1] in numbers:
            number += numbers[text[i:i+1]]
            break
        elif i-2 >= 0 and text[i-2:i+1] in numbers:
            number += numbers[text[i-2:i+1]]
            break
        elif i-3 >= 0 and text[i-3:i+1] in numbers:
            number += numbers[text[i-3:i+1]]
            break
        elif i-4 >= 0 and text[i-4:i+1] in numbers:
            number += numbers[text[i-4:i+1]]
            break
   
    #print(text,int(number)) 
    return int(number)

total1 = total2 = 0
for line in sys.stdin:
    line = line.strip()
    total1 += part1(line)
    total2 += part2(line)

print(total1,total2)
