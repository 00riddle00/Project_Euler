
def is_prime(num):
	i = 2
	while i < num:
		if num % i == 0:
			return False
		i += 1
	return True

# lpf - largest prime factor
def lpf(num):
	i = 2
	while i <= num/2:
		if num % i == 0:
			if is_prime(num/i):
				return num/i
		i += 1

result = lpf(600851475143)
print(result)