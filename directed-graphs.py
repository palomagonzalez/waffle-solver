import os
import sys


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


mydict = {}
print('How many distinct letters do you have?')

numLetters = int(input())

i = 0

while i < numLetters:
    print('Enter a letter')

    key = input()

    print('Now enter its pairings, separated by commas')

    value = input()

    value = value.split(',')

    mydict[key] = value

    i += 1

#print(mydict)

paths = []

for k in mydict.keys():
    value = mydict[k]
    print(value)
    shortest = find_shortest_path(mydict, k, value[0])
    if shortest and len(shortest) > 1:
        paths.append(shortest)

print(paths)
# Check for two swaps

