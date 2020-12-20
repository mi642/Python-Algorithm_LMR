N = int(input())


class count:
    def __init__(self):
        self.result = 0

    def select(self, list):
        list.sort()
        list.reverse()
        self.result = list[2]
        return self.result


for i in range(N):
    list1 = list(map(int, input().split()))
    cN = count()
    print(cN.select(list1))
