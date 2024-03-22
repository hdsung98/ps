from collections import deque

a, b = map(int, input().split())
q = deque([(a, 0)])
while q:
    cur, cnt = q.popleft()
    if cur == b:
        print(cnt + 1)
        exit()

    next1 = cur * 2
    next2 = cur * 10 + 1
    if next1 <= b:
        q.append((next1, cnt + 1))
    if next2 <= b:
        q.append((next2, cnt + 1))

print(-1)


#------------------------------------
# 그리디 접근법

a, b = map(int, input().split())
count = 1

while a != b:
    if b < a:
        count = -1
        break
    elif b % 10 == 1:
        b //= 10
        count += 1
    elif b % 2 == 0:
        b //= 2
        count += 1
    else:
        count = -1
        break

print(count)

