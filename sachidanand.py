def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_smallest_primes(numbers):
    if not numbers:
        return None, None

    largest = smallest = None
    primes = []

    for num in numbers:
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
        if is_prime(num):
            primes.append(num)

    return largest, smallest, primes

# Test Case 1
number_list = [13, 7, 22, 31, 19, 5, 12]
largest_num, smallest_num, prime_numbers = find_largest_smallest_primes(number_list)

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Prime numbers:", prime_numbers)

# Test Case 2

number_list = [2, 4, 6, 8, 10]
largest_num, smallest_num, prime_numbers = find_largest_smallest_primes(number_list)

print("Largest number:", largest_num)        
print("Smallest number:", smallest_num)      
print("Prime numbers:", prime_numbers)       

