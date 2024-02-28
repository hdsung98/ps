car_num = int(input().strip())
tunnel_start = []
tunnel_end = []

for _ in range(car_num):
    tunnel_start.append(input().strip())

for _ in range(car_num):
    tunnel_end.append(input().strip())

cnt = 0
for pos, name in enumerate(tunnel_start):
    if pos > tunnel_end.index(name):
        cnt += 1

print(cnt)

# 위에는 단순히 터널 진입때보다 터널 나올때 순번이 앞서면 추월한 것으로 간주했다
# 그러나 추월했음에도, 본인 추월횟수보다 추월당한 경우가 같거나 많으면 이게 안통한다
# FIFO 원칙에 따라 큐로 푸는 것이 합리적

car_num = int(input().strip())
enter = {input().strip(): i for i in range(car_num)}
out = list(enter[input().strip()] for _ in range(car_num))

cnt = 0
for i in range(len(out)):
    for j in range(i + 1, len(out)):
        if out[i] > out[j]:
            cnt += 1
            break  # 추월이 확실하면 더 검사할 필요 없음(추월한 차 갯수지 몇개 추월했냐가 아니니까)

print(cnt)

