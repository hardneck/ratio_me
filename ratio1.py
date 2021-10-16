# Find two least numbers that, by division, come closest to the given ratio.
# The ratio has a fixed precision after the decimal point.

def ab_ratio(rho, sigma=1000):

	# initialization of the denominator
	j = 1

	while True:

		# the lesser numerator
		i = round(rho * j)

		# the lesser ratio and its difference
		r = i / j
		d = abs(round(sigma * (r-rho)))

		# primes, the greater ratio and its difference
		r1 = (i+1) / j
		d1 = abs(round(sigma * (r1-rho)))

		# Register the even lesser difference.
		if d1 < d:
			d = d1
			i += 1

		# Get the desired (numerajtor, denominator) pair.
		# And end the function by returning this pair.
		if d == 0:
			return i, j

		# Loop over it.
		j += 1

def abc(r, s=1000, p=9):
  a, b = ab_ratio(r, s)
  if p != 9:
  	print(f'{r} %.9f %.{p}f {a}/{b}' % (a/b, a/b))
  else:
  	print(f'{r} %.9f {a}/{b}' % (a/b))

if __name__ == '__main__':

	# test set 1
	print('#1')
	abc(0.334)
	abc(1.334)
	abc(9.334)
	abc(1999.334)

	# test set 2
	print('#2')
	abc(0.3345, 10000)
	abc(0.3344, 10000)
	abc(0.3343, 10000)
	abc(0.3342, 10000)

	# test set 3
	print('#3')
	abc(0.3349, 100, 2)
	abc(0.3349, 1000, 3)
	abc(0.3349, 10000, 4)
	abc(0.3349, 100000, 5)
	abc(0.3349, 1000000, 6)
	abc(0.3349, 10000000, 7)

	# test set 4
	print('#4')
	abc(0.34, 1, 0)
	abc(0.34, 10, 1)
	abc(0.34, 100, 2)
	abc(0.34, 1000, 3)
	abc(0.34, 10000, 4)
	abc(0.34, 100000, 5)
	abc(0.34, 1000000, 6)