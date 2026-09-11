def generate_primes(n):
    prime = []

    for num in range(2,n+1):
        is_prime = True

        for i in range(2,num):
            if num % i == 0:
               is_prime = False
               break

        if is_prime  :
         prime.append(str(num))

    return ", ".join(prime)

print(generate_primes(10)) # Output: "2, 3, 5, 7"
print(generate_primes(20)) # Output: "2, 3, 5, 7, 11, 13, 17, 19"
print(generate_primes(1))  # Output: ""
print(generate_primes(2))  # Output: "2"