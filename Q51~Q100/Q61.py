# # 문자열을 입력받고 연속되는 문자열을 압축해서 표현하고싶습니다.

# user_input = str(input())

# slicing = list(user_input)


# print(slicing)
# cnt = 0
# count = []

# for i in range(1, len(slicing)):
#     if(slicing[i-1] == slicing[i]):
#         cnt = 0
#         count.append(cnt)
#     if(slicing[i-1] != slicing[i]):
#         cnt = '|'
#         count.append(cnt)


# print(count)

user_input = input()
s = ''
storeString = user_input[0]  # 맨 처음 입력문자 저장
count = 0
for i in user_input:
    if i == storeString:  # 맨 처음 입력문자가 또 나올 경우
        count += 1
    else:
        s += storeString + str(count)  # 같은 문자가 안 나올경우 그 상태의 count를 더한다.
        storeString = i  # 바뀐 문자열로 storeString을 바꿔준다.
        count = 1
s += storeString + str(count)
print(s)
