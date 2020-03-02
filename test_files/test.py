from ast import literal_eval

# Read graph from file
graph = literal_eval(open('test.txt', 'r').read())
print(graph[1])

# Write graph to file
# f = open('test.txt','w')
# graph = {0: {1: True}, 1:{2: False}}
# print("{", file=f)
# for room in graph:
#     print(f"  {room}: {graph[room]},", file=f)
# print("}", file=f)
# f.close()