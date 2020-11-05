#첫 번째 - A, B, C 값을 튜플에 저장하기
A, B = map(int, input().split())

C = A + B
sum = (A, B, C)
sum2 = (C)

print(sum, sum2)

#두 번째 - A, B 값을 바꿔서 C 값을 출력하기
A, B = map(int, input().split())

A, B = B, A
C = A + B
sum = (A, B, C)
sum2 = (C)
print(sum, sum2)

#세 번째 - 튜플과 for문, *(별표)를 활용해서 출력하기
A, B = map(int, input().split())
C = A + B

number = {"A": A, "B": B, "C": C}

for number_detail in number.items():
    print("{} = {}".format(*number_detail))