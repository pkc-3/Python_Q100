# 정량 N에 정확히 맞춰야만 움직이는 화물용 엘레베이터가 있습니다.
# 화물은 7kg, 3kg 두 가지이며 팔이 아픈 은후는 가장 적게 화물을 옮기고 싶습니다.

# 예를 들어 정량이 24kg이라면 3kg 8개를 옮기는 것 보다는
# 7kg 3개, 3kg 1개 즉 4개로 더 적게 옮길 수 있습니다.

# 정량 = N(n을 7로 나누고 나머지가 3으로 나눠지면 됨 나머지가 1, 2면 - 1 출력)

N = int(input("정량 N 입력 : "))

use7 = int(N/7)

temp1 = N % 7

use3 = int(temp1/3)

temp2 = temp1 % 3
if(temp1 == 1 or temp1 == 2 or temp2 == 1 or temp2 == 2):
    print(-1)
else:
    print("7kg 사용: {} 3kg 사용: {} 총 사용 횟수: {}".format(use7, use3, use7+use3))
