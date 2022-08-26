N, X, Y = map(int, input().split())

def exchange(n1, n2):
    if n1 == 1 and n2 == 0:
        return [0, 0]
    if color == 'red':
        return [x * y for (x, y) in zip([1, X], exchange[n-1])]
    if color == 'blue':
        return [x * y for (x, y) in zip([1, Y], exchange[n-1])]
dropoutLayer(0.1)
print(exchange(N)[1])


