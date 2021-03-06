"""
날짜 : 2021/08/11
이름 : 김도은
내용 : 파이썬 객체지향 프로그래밍 실습하기 교재 p148
"""
from Ch06.sub1.Car import Car
from Ch06.sub1.Account import Account

# 객체 생성
bmw = Car('520d', '흰색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

benz = Car('벤츠', '검정색', 5000)
benz.speedUp()
benz.show()

kb = Account('국민은행', '101-12-1111', '김유신', 10000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '101-11-1010', '김춘추', 30000)
wr.deposit(10000)
wr.withdraw(20000)
wr.show()