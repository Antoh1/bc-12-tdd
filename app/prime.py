def prime_numbers(number):
	"""this function checks for prime numbers in a range of a given number and outputs them in a list"""
	if type(number)!=int:
		return "Only integers allowed"
	elif number==1 or number==0 or number<0:
		return "a prime number is greater than one"	
	primes = []
	for num in range(2,number+1):
		p_flag = True
		for value in primes:
			if num%value==0:
				p_flag = False
		if p_flag:
			primes.append(num)        	
	return primes					 
print(prime_numbers(25))