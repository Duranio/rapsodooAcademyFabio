import math

numberList = [x for x in range(2, 101)]


# numbers must be an ordered list with at least two contiguous values starting from 2
def remove_not_prime(numbers, divider_index=0, num_to_check_index=1):

    # remove number not prime from list
    if numbers[num_to_check_index] % numbers[divider_index] == 0:
        numbers.remove(numbers[num_to_check_index])

    # check next number with same divider
    if num_to_check_index + 1 < len(numbers):
        remove_not_prime(numbers, divider_index, num_to_check_index + 1)
        return

    # check next divider
    if divider_index < math.sqrt(numbers[len(numbers)-1]):
        remove_not_prime(numbers, divider_index + 1, divider_index + 2)


print(numberList)
remove_not_prime(numberList)
print(numberList)
