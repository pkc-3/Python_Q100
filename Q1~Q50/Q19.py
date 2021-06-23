# 공백으로 구분하여 두 숫자 a와 b가 주어지면, a의 b승을 구하는 프로그램을 작성하세요.

data = list(map(int, input("숫자 a b 입력 ").split()))


print(data[0]**data[1])
