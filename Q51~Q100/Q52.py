# quick sort
# 퀵 정렬은 찰스 앤터니 리처드 호어가 개발한 정렬 알고리즘이다. 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬에 속한다. 퀵 정렬은 n개의 데이터를 정렬할 때, 최악의 경우에는 O(n²)번의 비교를 수행하고, 평균적으로 O(n log n)번의 비교를 수행한다

def quick_sort(user_data):
    user_data_len = len(user_data)
    if user_data_len <= 1:
        return user_data
    standard_value = user_data.pop(user_data_len//2)
    data_group1 = []
    data_group2 = []

    for i in range(user_data_len-1):
        if user_data[i] < standard_value:
            data_group1.append(user_data[i])
        else:
            data_group2.append(user_data[i])
    return quick_sort(data_group1) + [standard_value] + quick_sort(data_group2)


user_data = input().split(' ')
user_data = [int(i) for i in user_data]

print(quick_sort(user_data))
