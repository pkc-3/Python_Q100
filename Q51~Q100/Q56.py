# 다음의 딕셔너리가 주어졌을 때 한국의 면적과 가장 비슷한 국가와 그 차이를 출력하세요.

# 데이터
nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England': 242900}

# 출력
# England 22023

country = input("나라입력 : ")
w = nationWidth[country]  # korean value값 w에 넣음
nationWidth.pop(country)  # nationWidth에서 korea를 빼버림

l = list(nationWidth.items())  # 딕셔너리에서 리스트로 변환
gap = max(nationWidth.values())  # 면적 제일 큰 값을 gap에 넣음
item = 0

for i in l:  # i Rusia => China => France => Japan => England
    if gap > abs(i[1] - w):  # 17098242 > i[1] - 220877 : 러시아 땅 보다 작으면
        gap = abs(i[1] - w)  # gap에 두 수 차이를 넣음 점점 작아짐 제일 작은 값만 남음
        item = i  # 차가 제일 작을때 England가 들어가짐

print(item)  # ('England', 242900)으로 남음
print(item[0], abs(item[1]-w))  # England, 두 땅의 차이
