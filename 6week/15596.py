n = int(input())

def solve(n):
    a = [0]
    sum = 0

    for i in range(1, n + 1):
        a.append(i)
        sum = sum + i
    return a, sum

h = solve(n)
print(h)