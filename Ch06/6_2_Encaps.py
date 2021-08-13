"""
날짜 : 2021/08/12
이름 : 김도은
내용 : 파이썬 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

num1 = 1
var1 = True

kb = Account('국민은행', '101-101-1001', '김유신', 10000)

kb.deposit(40000)
kb.withdraw(4000)

# 캡슐화(정보은닉)를 적용해서 취약코드 예방
# kb.__balance -= 1

kb.show()