# function to find a certain number of primes
def get_primes(low: int, high: int):
	primes = []
	for num in range(low, high+1):
		# all prime numbers are greater than 1
		if num > 1:
			for i in range(2, num):
				if num % i == 0:
					break
			else:
				primes.append(num)

	return primes
					
