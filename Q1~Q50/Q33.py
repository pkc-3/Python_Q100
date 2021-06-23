# 한 줄에 여러개의 숫자가 입력되면, 역순으로 그 숫자들을 하나씩 출력하는 프로그램을 작성하시오.

# 방법1
n = list(map(int, input("숫자 입력 : ").split()))
result = list(reversed(n))

print("숫자 출력 :", end=' ')
for i in range(len(result)):
    print(result[i], end=' ')


# 방법2
# n = input()

# l = list(n.strip().split())
# len1 = len(l) - 1
# for i in range(len1, -1, -1):
#     print(l[i], end=' ')


# # for 변수 in range(시작, 끝, 증가폭):
