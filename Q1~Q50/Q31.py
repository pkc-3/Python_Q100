# 다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌것은?

# 1)  l[i] < O(1)
# 2)  l.append(5) < O(1)
# 3)  l[a:b] < O(b-a)
# 4)  l.pop() < O(1)
# 5)  l.clear() < O(1)

# Operation	        Example	        Big-O	    Notes
# Index	            l[i]	        O(1)
# Store	            l[i] = 0	    O(1)
# Length	        len(l)	        O(1)
# Append	        l.append(5)	    O(1)
# Pop	            l.pop()	        O(1)	    l.pop(-1) 과 동일
# Clear	            l.clear()	    O(1)	    l = [] 과 유사
# Slice	            l[a:b]	        O(b-a)	    l[:] : O(len(l)-0) = O(N)
# Extend	        l.extend(…)	    O(len(…))	확장 길이에 따라
# Construction	    list(…)	        O(len(…))	요소 길이에 따라
# check ==, !=	    l1 == l2	    O(N)	    비교
# Insert	        l.insert(i, v)	O(N)	    i 위치에 v를 추가
# Delete	        del l[i]	    O(N)
# Remove	        l.remove(…)	    O(N)
# Containment	    x in/not in l	O(N)	    검색
# Copy	            l.copy()	    O(N)	    l[:] 과 동일 - O(N)
# Pop	            l.pop(i)    	O(N)	    l.pop(0):O(N)
# Extreme value	    min(l)/max(l)	O(N)	    검색
# Reverse	        l.reverse()	    O(N)	    그대로 반대로
# Iteration	        for v in l:	    O(N)
# Sort	            l.sort()	    O(N Log N)
# Multiply	        k*l	            O(k N)	    [1,2,3] * 3 » O(N**2)
