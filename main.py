from src.prime import get_primes
from src.json_module import save_data
from src.recursive_reciprocal import find_len_repeating_reciprocal

def main():
	# The primes are calculated here between the upper and lower value
	lower = 0
	upper = 99
	primes = get_primes(lower, upper)
	# Dict to store values
	dict = { "primes" : [] }
	# Calculates the number of values 
	for prime in primes:
		dict["primes"].append({"prime":prime, "len_reciprocal_root": find_len_repeating_reciprocal(prime)})
	# Save those values to json
	save_data(dict)

if __name__ == '__main__':
	main()
		