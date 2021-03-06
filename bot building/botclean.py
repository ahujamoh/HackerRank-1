#!/bin/python
# Head ends here
class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distTo(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)

def next_move(posx, posy, board):
    bot_node = Node(posx, posy)

    # find all dirty cells
    dirty_cells = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if col == "d":
                dirty_cells.append(Node(y, x))

    # find the nearest dirty cell
    nearest_node = None
    for node in dirty_cells:
        if nearest_node is None or node.distTo(bot_node) < nearest_node.distTo(bot_node):
            nearest_node = node

    if nearest_node is not None:
        print_move(nearest_node.x - bot_node.x, nearest_node.y - bot_node.y)

def print_move(x, y):
    if x < 0 :
        print "LEFT"
    elif x > 0 :
        print "RIGHT"
    elif y < 0 :
        print "UP"
    elif y > 0 :
        print "DOWN"
    else:
        print "CLEAN"

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)


