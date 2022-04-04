from src.prime import get_primes
from src.json_module import save_data, get_data
from src.recursive_reciprocal import find_len_repeating_reciprocal

def main():
	# Getting the previous calculations from json
	dict = get_data()
	# The primes are calculated here between the upper and lower value
	lower = dict['data']['end_point']
	upper = lower + 300
	primes = get_primes(lower, upper)
	# Calculates the number of values 
	for prime in primes:
		dict["primes"].append({"prime":prime, "len_reciprocal_root": find_len_repeating_reciprocal(prime)})
	# Setting new upper value
	dict['data']['end_point'] = upper
	# Setting number of values done
	dict['data']['values_completed'] = len(dict['primes'])
	# Save those values to json
	save_data(dict)

if __name__ == '__main__':
	main()
		