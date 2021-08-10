"""
날짜 : 2021/08/10
이름 : 김도은
내용 : 파이썬 if문 실습하기 교재 p60
"""

# if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고, num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 그리고 num2는 1보다 크다.')

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    # 조건이 참
    print('num3은 num4보다 크다.')
else:
    # 조건이 거짓
    print('num3은 num4보다 작다.')

# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

# 연습문제
score = int(input('점수 입력 : '))
print('입력 점수 :', score)

if score >= 90 and score <= 100:
    # 점수가 90 ~ 100
    print('A입니다.')
elif 80 <= score < 90:
    # 점수가 80 ~ 89
    print('B입니다.')
elif 70 <= score < 80:
    # 점수가 70 ~ 79
    print('C입니다.')
elif 60 <= score < 70:
    # 점수가 60 ~ 69
    print('D입니다.')
else:
    # 점수가 0 ~ 59
    print('F입니다.')
