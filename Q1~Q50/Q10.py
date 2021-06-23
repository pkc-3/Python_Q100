stars = int(input("단수를 입력해주세요 :"))

for i in range(1, stars+1):
    print(" "*(stars-i)+("*"*(2*i-1)))
