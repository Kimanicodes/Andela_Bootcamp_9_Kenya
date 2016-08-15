def Get_Primes_Upto(x):
    prime_numbers = [2, 3]
    start_point = 4

    while True:
        for number in range(2, (start_point // 2) + 1):

            if start_point % number == 0:
                break

        else:
            prime_numbers.append(start_point)
        start_point += 1
        if start_point == x + 1:
            break
    return str(prime_numbers)

print(Get_Primes_Upto(11))