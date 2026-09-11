def factorrial(n):
    if n == 0:
       return 1
    else:
       return n * factorrial(n-1)

print(factorrial(5))