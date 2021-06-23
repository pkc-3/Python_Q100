# **2-gram**이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다.
# 예를 들어 '**Python**'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다.

target = str(input("문자 입력 : "))

result = list(target)

print(result)
for i in range(1, len(result)):
    print(result[i-1]+result[i])
