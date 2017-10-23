# this prolly wastes some steps on the corners
# aka the corners are being written 2x
# i could write some fn to print if sth is already there, instead of table[a][i] = 'x', eg

# another thing i cld do is to make concentric circles, and then move stuff

def print_table(table):
	for row in table:
		print ' '.join(row)

def write_spiral(size_of_table):
	table = [['-' for i in range(size_of_table)] for j in range(size_of_table)]

	n = size_of_table - 1 # bc Python is 0-indexed
	a = 0

	for i in range(n+1):
		table[0][i] = 'x'
		table[i][n] = 'x'
		table[n][i] = 'x'		

		if i >= 2 and i <= n:
			table[i][0] = 'x'

	for j in range(n):
		a += 2
		if n-a < 0: # to save time, make less steps
			break	
		for i in range(n):
			if i >= a-2 and i <= n-a:
				table[a][i] = 'x'
			if i >= a and i <= n-a:
				table[n-a][i] = 'x'
				table[i][n-a] = 'x'
			if i >= a+2 and i <= n-a:
				table[i][a] = 'x'

	print_table(table)

write_spiral(35)