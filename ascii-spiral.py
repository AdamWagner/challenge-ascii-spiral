import sys
from math import *
import time
import collections

# Utility
def sum_arrays(a,b):
	return [x + y for x, y in zip(a, b)]

def clear():
    print(' \n' * 25)

class Cell():
	content = ' . '

	def mark(self):
		self.content = ' @ '

	def is_filled(self):
		if self.content == ' @ ':
			return True


class Grid():

	size = 20
	grid = [[Cell() for x in range(size)] for y in range(size)]

	def draw(self):
		for row in self.grid:
			sys.stdout.write('\n')
			for c in row:
				sys.stdout.write(c.content)
		clear()

	def get_cell(self, x,y):
		return self.grid[x][y]

	def is_full(self):
		for x in range(self.size):
			for y in range(self.size):
				if not self.get_cell(x,y).is_filled():
					return False
		return True


directions = collections.deque([
	[0,1], # right
	[1,0], # down
	[0,-1], # left
	[-1,0], # up
])

def is_edge(coord):
	return coord < 0 or coord == grid.size

def is_filled_or_at_edge(pos):
	if is_edge(pos[0]) or is_edge(pos[1]):
		return True # cell is at boundary
	else: # cell is not at boundary
		if grid.get_cell(*pos).is_filled():
			return True # but, cell is filled

def move(pos):
	move = sum_arrays(pos, directions[0])

	# If move is filled or at edge,
	# rotate direction and recalc move
	if is_filled_or_at_edge(move):
		directions.rotate(-1)
		move = sum_arrays(pos, directions[0])

	return move

def draw_in_direction(pos):
	# mark spot
	grid.get_cell(*pos).mark()

	# wait and draw grid
	time.sleep(0.03)
	grid.draw()

	if grid.is_full():
		print 'All done'
	else:
		# recurse
		draw_in_direction(move(pos))

grid = Grid()

# must start from top left
# to change origin, must also change directions queue
draw_in_direction([0,0])
