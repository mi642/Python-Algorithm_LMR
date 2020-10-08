A = 5
B = 8
C = 4

a = (A+B)%C
print('a = ', a)

b = ((A%C)+(B%C))%C
print('b = ', b)

c = (A*B)%C
print('c = ', c)

d = ((A%C)*(B%C))%C
print('d = ', d)