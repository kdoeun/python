"""
날짜 : 2021/08/13
이름 : 김도은
내용 : 코딩 테스트 - 큰 수의 법칙
"""
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)

# 가장 큰 수, 두 번째로 큰 수
first = data[0]
second = data[1]

result = 0

repeat = k

for i in range(m):

    if repeat > 0:
        result += first
        repeat -= 1
    else:
        result += second
        repeat = k

# 최종 답안 출력
print(result)

"""
5 8 3
2 4 5 4 6 일때 46

7 5 2
1 5 2 4 5 4 6 일때 29

5 8 3
3 4 3 4 3 일때 28
"""