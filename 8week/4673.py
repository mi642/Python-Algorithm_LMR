Not_SelfNumber = []


def d(n):
    result = n
    while n != 0:
        result = result + n % 10
        return result


for n in range(1, 10001):
    Not_SelfNumber.append(d(n))
    if n in Not_SelfNumber:
        continue
    else:
        print(n)
