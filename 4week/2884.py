print('''상근이가 일어나고자 하는 시간과 분을 입력하시오
(0<=H<=23, 0<=M<=59)''')

H = int(input())
M = int(input())

minute = H * 60 + M
todo = minute - 45

if todo < 0:
    todo = todo + 1440

resulthour = todo // 60
resultminute = todo % 60
print("창영이의 방법 : ", resulthour, "시", resultminute, "분")
