# 탑을 쌓기 위해 각 크기별로 준비된 블럭들을 정해진 순서에 맞게 쌓아야 합니다.
# 순서에 맞게 쌓지 않으면 무너질 수 있습니다.
# 예를 들면 정해진 순서가 BAC 라면 A 다음 C가 쌓아져야 합니다.
# 선행으로 쌓아야 하는 블럭이 만족된 경우라면 탑이 무너지지 않습니다.

# - B를 쌓지 않아도 A와 C를 쌓을 수 있습니다.
# - B 다음 블럭이 C가 될 수 있습니다.

# 쌓아져 있는 블럭 탑이 순서에 맞게 쌓아져 있는지 확인하세요.

# 1. 블럭은 알파벳 대문자로 표기합니다.
# 2. 규칙에 없는 블럭이 사용될 수 있습니다.
# 3. 중복된 블럭은 존재하지 않습니다.

top = list(map(str, input().split()))

print("탑 입력값: ", top[0])
rule = str(input())

print("룰 입력값: ", rule[0])

# top[0].index[rule[0]] < top[0].index[rule[1]] < top[0].index[rule[2]]: 탑 0번은 가능

# 규칙의 첫번째 값 인덱스가 두번째보다 작아야하고 세번째는 두번째보다 커야함
# index[0] < index[1] < index[2]

# 탑.index[규칙[0]] <  탑.index[규칙[1]] < 탑.index[규칙[2]] : 가능


def solution(top, rule):
    answer = []
    for part_block in top:
        answer.append(check_order(part_block, rule))
    return answer


def check_order(part_block, rule):
    tmp = rule.index(rule[0])
    for text in part_block:
        if text in rule:
            if tmp > rule.index(text):
                return '불가능'
            tmp = rule.index(text)
    return '가능'


top = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
rule = 'ABCD'

print(solution(top, rule))
