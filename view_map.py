from ast import literal_eval
rooms = literal_eval(open('rooms.txt').read())
traversal_graph = literal_eval(open('map.txt').read())

grid = [[None]*60 for _ in range(60)]
for room in rooms:
    col,row = literal_eval(rooms[room][0])
    col -= 40
    row -= 20
    grid[row][col] = room
grid.reverse()
for row in range(len(grid)):
    s = "#"
    # NORTH CONNECTION
    for col in range(len(grid[0])):
        room = grid[row][col]
        if grid[row][col] is not None and traversal_graph[room].get('n', None) is not None:
            s += "  |  "
        else:
            s += "     "
    print(s)
    s = "#"
    # WEST EAST CONNECTION
    for col in range(len(grid[0])):
        room = grid[row][col]
        if room is None:
            s += "     "
        else:
            if traversal_graph[room].get('w', None) is not None:
                s += "-"
            else:
                s += " "
            new_room = "00" + str(room)
            s += new_room[-3:]
            if traversal_graph[room].get('e', None) is not None:
                s += "-"
            else:
                s += " "
    print(s)
    s = "#"
    # SOUTH CONNECTION
    for col in range(len(grid[0])):
        room = grid[row][col]
        if grid[row][col] is not None and traversal_graph[room].get('s', None) is not None:
            s += "  |  "
        else:
            s += "     "
    print(s)
