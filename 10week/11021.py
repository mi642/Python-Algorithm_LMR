N = int(input())


class calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result += num1 + num2
        return self.result


for i in range(N):
    calN = calculator()
    A, B = map(int, input().split())
    print(calN.add(A, B))
