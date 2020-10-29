print("곱셈을 진행할 세 자리 자연수를 두 개 입력해 주세요")

A = int(input())
a = A // 100
b = A % 100 // 10
c = A % 10 // 1
X = int(input())
x = X // 100
y = X % 100 // 10
z = X % 10 // 1

print(A, "*", x, "=", A*x)
print(A, "*", y, "=", A*y)
print(A, "*", z, "=", A*y)

print(A, "*", X, "=", A*x*100+A*y*10+A*z)
