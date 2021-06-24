# a = [1,2,3,4]
# b = [a,b,c,d]
# 이런 리스트가 있을 때 [[1,a],[b,2],[3,c],[d,4]] 이런식으로 a,b리스트가 번갈아가면서 출력되게 해주세요.


a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
c = []
d = list(zip(a, b))
print(d)
for i, j in zip(a, b):
    c.append([i, j])

print(c)
