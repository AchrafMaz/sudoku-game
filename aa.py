import numpy as np



board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def find_zero(board):
	b = []
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				b.append([i,j])
	return b

def possible(y,x,n):
	global board
	for i in range(0,9):
		if board[y][i]==n:
			return False
	for i in range(0,9):
		if board[i][x]==n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if board[y0+i][x0+j]==n:
				return False
	return True

b = find_zero(board)

def solve(board):
	while len(b)!=0:
		h = 0
		for a in b:
			c = []
			vb = []
			for i in range(0,10):
				if possible(a[0],a[1],i):
					c.append(i)
					vb.append(a[0])
					vb.append(a[1])

			if len(c)==1:
				board[vb[0]][vb[1]] = c[0]
				b.pop(h)
		
			h+=1
	return board
solution = solve(board)