"""
날짜 : 2021/08/13
이름 : 김도은
내용 : 코딩 테스트 - 숫자 카드 게임
"""

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
mins = []

result = 0

for i in range(n):
    # 행 데이터 입력하기
    data = list(map(int, input().split()))

    # 데이터 오름차순 정렬
    data.sort()

    # 최소값 구해서 리스트에 저장하기
    min = data[0]
    mins.append(min)

    # mins에서 최대값 구하기
    result = max(mins)

    print(result)
