# 새 학기를 맞아 호준이네 반은 반장 선거를 하기로 했습니다.
# 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 하였습니다.


data = list(map(str, input().split()))
name = 0
for i in range(len(data)):
    if data.count(data[i-1]) < data.count(data[i]):
        name = i
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(data[name], data.count(data[name])))
