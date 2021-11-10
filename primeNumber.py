import math
import time


def is_prime_iterative(number_to_check):
    if number_to_check <= 1:
        return False
    max_divider = int(math.sqrt(number_to_check))
    for divider in range(2, max_divider + 1):
        if number_to_check % divider == 0:
            return False
    return True


def is_prime_recursive(number_to_check, divider=2):

    # base case 1
    if number_to_check <= 1:
        return False

    # base case 2
    if divider > int(math.sqrt(number_to_check)):
        return True

    # base case 3
    if number_to_check % divider == 0:
        return False

    # recursion
    return is_prime_recursive(number_to_check, divider + 1)


# recursive benchmark
start_time = time.time()
for number in range(2, 100001):
    if is_prime_recursive(number):
        print(number)
end_time = time.time()
recursive_exec_time = end_time - start_time


# iterative benchmark
start_time = time.time()
for number in range(2, 100001):
    if is_prime_iterative(number):
        print(number)
end_time = time.time()
iterative_exec_time = end_time - start_time

# Iterative algorithm is about 4 or 5 times faster than recursive algorithm
print("Recursive algorithm time:", recursive_exec_time)
print("Iterative algorithm time:", iterative_exec_time)
print("Recursive vs Iterative ratio:", recursive_exec_time/iterative_exec_time)




