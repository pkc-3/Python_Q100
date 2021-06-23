# 2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수를 만들려고 합니다.

def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two


a = one(2)  # 제곱값 나오게
b = one(3)  # 세제곱값 나오게
c = one(4)  # 네제곱값  나오게
print(a(10))
print(b(10))
print(c(10))
