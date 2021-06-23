# 1부터 100까지의(100을 포함) 모든 숫자를 일렬로 놓고 모든 자릿수의 총 합을 구하세요.

# 예를 들어 10부터 15까지의 모든 숫자를 일렬로 놓으면 101112131415이고 각 자리의 숫자를 더하면 25입니다.

# 방법1
# a = []
# for i in range(1, 101):
#     a.append(str(i))

# b = []
# b.append(''.join(a))
# c = str(b[0])
# print(c)

# a = list(map(int, str(c)))
# print(sum(a))

# 방법2
s = str()
for i in range(101):
    s += str(i)
print(s)
result = 0
for i in s:
    result += int(i)
print(result)
