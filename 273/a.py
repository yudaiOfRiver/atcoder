N = int(input())

def resurse(n):
    if n == 0:
        return 1

    return n * resurse(n-1)

print(resurse(N))
