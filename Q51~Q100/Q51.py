# 1. 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는

# 2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.

# 3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.

# 4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

# 합병 정렬 또는 병합 정렬은 O(n log n) 비교 기반 정렬 알고리즘이다. 일반적인 방법으로 구현했을 때 이 정렬은 안정 정렬에 속하며, 분할 정복 알고리즘의 하나이다.
# 병합 정렬
def merge_sort(user_data):
    user_data_len = len(user_data)
    if user_data_len <= 1:
        return user_data
    data_mid = user_data_len // 2
    data_group1 = merge_sort(user_data[:data_mid])
    data_group2 = merge_sort(user_data[data_mid:])
    result = []

    while data_group1 and data_group2:
        if data_group1[0] < data_group2[0]:
            result.append(data_group1.pop(0))
        else:
            result.append(data_group2.pop(0))

    while data_group1:
        result.append(data_group1.pop(0))
    while data_group2:
        result.append(data_group2.pop(0))
    return result


user_data = input().split(' ')
user_data = [int(i) for i in user_data]

print(merge_sort(user_data))
