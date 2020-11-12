x, y = map(int, input().split())

#첫 번째 풀이
def Quadrant(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(2)
    elif x < 0 and y > 0:
        print(3)
    elif x < 0 and y < 0:
        print(4)

#두 번째 풀이
def Quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 2
    elif x < 0 and y > 0:
        return 3
    elif x < 0 and y < 0:
        return 4

n = Quadrant(x, y)
print(n)