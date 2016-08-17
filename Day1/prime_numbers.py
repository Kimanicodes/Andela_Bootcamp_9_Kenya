def Get_Primes_Upto(x):
    prime_numbers = [2, 3]

    '''Start by initializing the list with 2 and 3 as the first prime numbers'''

    start_point = 4
    # Start at 4
    while True:
        for number in range(2, int(start_point**0.5) + 1):
            # check upto the square root, update from the from half

            if start_point % number == 0:
                break

        else:
            prime_numbers.append(start_point)
        start_point += 1
        if start_point == x + 1:
            break
    # return as a string
    return str(prime_numbers)
# Testing the function
print(Get_Primes_Upto(11))
