def prime_no(number):
	"""this function checks for prime numbers in a range and outputs them in a list"""
	if type(number)!=int:
		return "Only integers allowed"
	elif number==1 or number==0 or number<0:
		return "a prime number is greater than one"
	elif number==2:
		return [2]	
	primes = [2,3]
	if number<=3:
		return primes
	for num in range(4,number+1):
		p_flag = True
		for value in primes:
			if num%value==0:
				p_flag = False
		if p_flag:
			primes.append(num)        	
	return primes					 
print(prime_no(25))