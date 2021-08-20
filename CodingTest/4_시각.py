"""
날짜 : 2021/08/13
이름 : 김도은
내용 : 코딩 테스트 - 시각
"""

# h 값 입력받기
h  = int(input())

count = 0

for i in range(h+1):
    for j  in range(60):
        for k in range(60):

            time = str(i) + str(j) + str(k)

            if '3' in time:
                count += 1

print(count)