N = int(input())
list = list(map(int, input().split()))
new_list = []
total = 0

list.sort()
list.reverse()

for i in range(len(list)):
    new_list.append(list[i] / list[0] * 100)
    total += new_list[i]

print(total / N)