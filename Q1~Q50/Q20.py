# 공백으로 구분하여 두 숫자가 주어집니다.
# 첫번째 숫자로 두번째 숫자를 나누었을 때 **그 몫과 나머지를 공백으로 구분하여 출력하세요.**

data = list(map(int, input("숫자입력 : ").split()))

print(int(data[0] / data[1]), data[0] % data[1], sep=" ")
