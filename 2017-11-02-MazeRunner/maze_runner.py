maze = [list(line.rstrip("\n")) for line in open("maze.txt")]
print(maze)

Xi, Xj = 0,0 #OUR EXPLORER
Ei, Ej = 0,0 #OUR EXIT
wall = '#'
blocks_walked = 0
def find_explorer_and_exit(maze):
    global Xi, Xj, Ei, Ej
    for row_index,row in enumerate(maze):
        if '>' in row:
            Xi, Xj=row_index,row.index('>')
        if 'E' in row:
            Ei, Ej=row_index,row.index('E')
    
def front():
    global Xi, Xj, maze
    if maze[Xi][Xj] == '>':
        return maze[Xi][Xj+1]
    if maze[Xi][Xj] == '<':
        return maze[Xi][Xj-1]
    if maze[Xi][Xj] == '^':
        return maze[Xi-1][Xj]
    else:
        return maze[Xi+1][Xj]
def front_index(i,j):
    global maze
    if maze[i][j] == '>':
        return i, j+1
    if maze[i][j] == '<':
        return i, j-1
    if maze[i][j] == '^':
        return i-1, j
    else:
        return i+1, j

def turn_left():
    global Xi, Xj, maze
    if maze[Xi][Xj] == '>':
        maze[Xi][Xj] = '^'
    if maze[Xi][Xj] == '<':
        maze[Xi][Xj] = '<'
    if maze[Xi][Xj] == '>':
        maze[Xi][Xj] = '^'
    if maze[Xi][Xj] == '_':
        maze[Xi][Xj] = '>'

def turn_right():
    global Xi, Xj, maze
    if maze[Xi][Xj] == '>':
        maze[Xi][Xj] = '_'
    if maze[Xi][Xj] == '<':
        maze[Xi][Xj] = '^'
    if maze[Xi][Xj] == '^':
        maze[Xi][Xj] = '>'
    if maze[Xi][Xj] == '_':
        maze[Xi][Xj] = '<'

def turn_180():
    global Xi, Xj, maze
    if maze[Xi][Xj] == '>':
        maze[Xi][Xj] = '<'
    if maze[Xi][Xj] == '<':
        maze[Xi][Xj] = '>'
    if maze[Xi][Xj] == '^':
        maze[Xi][Xj] = '_'
    else:
        maze[Xi][Xj] = '^'

def walk_a_block():
    global blocks_walked, Xi, Xj
    if blocks_walked == 6: #If next is 7th 
        turn_180() #Turn 180 degress
        blocks_walked = 0 
        return
    i,j = front_index(Xi,Xj)
    if front() == 'E':
        maze[Xi][Xj],maze[i][j] = ' ', maze[Xi][Xj] #If the front block is exit, swap with whitespace
    else:    
        maze[Xi][Xj],maze[i][j] = maze[i][j], maze[Xi][Xj]#Walk the block by swaping block in front
    Xi, Xj = i,j #Change the explorer's position after swaping position
    blocks_walked += 1

def main():
    global maze,Xi, Xj,Ei, Ej, wall,blocks_walked
    find_explorer_and_exit(maze)

    while Xi != Ei or Xj != Ej: #While our explorer is not standing on exit
        if wall != front(): #Check whether there is a wall in front
            walk_a_block()  
        else:
            turn_right()
            if wall == front():
                turn_left()
                turn_left()
                if wall == front():
                    turn_left()
    print("MAZE ENDED")
    with open('completed_maze.txt', 'w') as f:
        completed_maze = ''
        for row in maze:
            for col in row:
                completed_maze += col
            completed_maze += '\n'
        f.write(completed_maze)
if __name__ == '__main__':
    main()