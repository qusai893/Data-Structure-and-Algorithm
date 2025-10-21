def factoriyal(n):
    if n == 0:
        return 1
    result = n * factoriyal(n-1)
    return result



print(factoriyal(1000))