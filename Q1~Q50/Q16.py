# 문장이 입력되면 거꾸로 출력하는 프로그램을 만들어 봅시다.

n = input("단어 입력 : ")

print(n[::-1])  # 방법1
# n[3:0:-1] 이라면 3번 인덱스 부터 1번인덱스까지 역순 출력

print(''.join(reversed(n)))  # 방법2 역순했다가 조인해줌


n_list = list(n)  # 방법3
# reverse 함수를 사용하기 위해 문자열을 list로 치환
n_list.reverse()
print(''.join(n_list))
