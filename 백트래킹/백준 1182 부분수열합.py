seq_len, sum = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0


# 그냥 리스트에 원소를 직접 append,pop하고
# sum, len으로 탈출조건을 계산하는 법도 있음

def dfs(acc, start, length):
    global cnt
    if acc == sum and length > 0:
        cnt += 1 # 더 긴 수열에서 같은 sum이 나올 수 있으므로 리턴없이 진행

    for i in range(start, seq_len): # start가 seq_len에 닿을때가 bottom case
        dfs(acc + seq[i], i + 1, length + 1) 


dfs(0, 0, 0)
print(cnt)
