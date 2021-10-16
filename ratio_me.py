def ratio_me(r0, k=4):
	'''
	A function to find the first ten rational numbers
	that run close to the desired ratio,
	along with the specified tolerence,
	and return tuples of (numerator, denominator, ratio).
	'''

	a, b, r = 0, 1, 0
	eps = 5*10**(-k)
	y = []

	while True:
		# see if the current ratio is close enough
		if abs(r-r0) < eps:
			y.append((a, b, r))
			if len(y) == 10:
				break
		# add 1 to the numerator or the denominator
		if r < r0:
			a = a + 1
		else:
			b = b + 1
		# another ratio computed, repeat the process
		r = a / b

	return y

if __name__ == "__main__":
	print(ratio_me.__doc__)
	print("Tolerence: 0.0005")
	print(ratio_me(0.334, 4))
	print("Tolerence: 0.00005")
	print(ratio_me(0.334, 5))
	print("Tolerence: 0.005")
	print(ratio_me(0.334, 3))
	print("Tolerence: 0.000005")
	print(ratio_me(0.334, 6))
