# 어떤 대회에 참가하는 여러 참가자와 그들이 접속할 수 있는 여러 서버가 존재할 때
# 각 서버별로 모든 참가자 중 일부로 그룹을 구성하려한다.
# 형평을 위해 그룹 멤버 중 어떤 두 멤버 사이에서도 A배 이상 또는 B초 이상의 딜레이가 발생하면 안된다.
# 각 멤버별로 모든 서버에 대한 딜레이 시간 정보가 2차원배열로 주어진다.(행은 멤버, 열은 서버)
# 각 서버별로 최대한 많은 인원을 가진 그룹을 구성하되, 그 그룹 멤버들 간에 형평성 규칙을 준수하게 해라.
# 그리고 나서, 어떤 서버에서 최대 인원의 그룹이 생성되는지를 구하라.
# 즉 구하는 값은 [최대인원인의 그룹이 생성된 서버, 그 그룹의 인원수]
# (최대그룹인원이 동률인 경우, 가장 서버 번호 수가 낮은 것을 정답으로 한다)
#
# 주어지는 정보: A,B,delay
# - A: 그룹 내 멤버간 형평규칙 1 (한 멤버가 다른 멤버보다 딜레이가 A배이상 차이나면 안됨)
# - B: 그룹 내 멤버간 형평규칙 2 (한 멤버가 다른 멤버보다 딜레이가 B초 이상 차이나면 안됨)
# - delay 배열 : 멤버-서버 간 딜레이 정보를 담은 N차원 배열 (ex. delay[i][j] = 1300 은 멤버 i가 j서버를 골랐을 때 딜레이가 1300 "ms"임을 의미)
# ( 인원(len(delay) 최대 50만, 서버(len(delay[0]) 최대 50만, 인원x서버 최대 100만)
#
# 주의:
# 1) 1초는 1000 ms 다.
# 2) 시간제한 10초, 메모리제한 2GB

def find_largest_group(A, B, delays):
    n, m = len(delays), len(delays[0])  # 멤버 수 n, 서버 수 m
    max_group_size = 0
    server_with_max_group = -1

    for server in range(m):
        # 현재 서버에 대한 딜레이 값만 저장(해당 열(서버)의 모든 멤버에 대한 딜레이 값 수집)
        server_delays = [delay[server] for delay in delays]
        # 딜레이 값에 따라 오름차순 정렬
        server_delays.sort()

        start, end = 0, 0  # 투 포인터 초기화

        while end < n:  # 그룹 사이즈를 더 늘릴 수 없을 때 종료(시작포인터를 여기서 더 옮겨 봤자 그룹사이즈는 오히려 준다)
            min_delay = server_delays[start]
            max_delay = server_delays[end]

            if max_delay <= min_delay * A and max_delay - min_delay <= B * 1000:
                # 형평성 규칙을 만족하면, 그룹 크기 증가
                current_group_size = end - start + 1
                if current_group_size > max_group_size:
                    max_group_size = current_group_size
                    server_with_max_group = server
                end += 1
            else:
                # 형평성 규칙을 만족하지 않으면, 시작 포인터 이동
                start += 1

    return [server_with_max_group, max_group_size]


# 예시 사용
A = 2  # 배수 차이 제한
B = 1000  # 최대 시간 차이 제한 (ms 단위)
delays = [
    [100, 200, 300],
    [200, 300, 400],
    [300, 400, 500]
]  # 예시 delays 배열

print(find_largest_group(A, B, delays))


#----------------------------------------------------
# 인덱스만 저장하는 방식(메모리 효과적)

def find_largest_group(A, B, delays):
    n, m = len(delays), len(delays[0])  # 멤버 수 n, 서버 수 m
    max_group_size = 0
    server_with_max_group = -1

    for server in range(m):
        # 현재 서버에 대한 딜레이 값을 가리키는 인덱스를 저장
        indices = list(range(n))
        # 인덱스를 딜레이 값에 따라 오름차순으로 정렬
        indices.sort(key=lambda x: delays[x][server])

        start, end = 0, 0  # 투 포인터 초기화

        while end < n:
            min_delay = delays[indices[start]][server]
            max_delay = delays[indices[end]][server]

            if max_delay <= min_delay * A and max_delay - min_delay <= B:
                # 형평성 규칙을 만족하면, 그룹 크기 증가
                current_group_size = end - start + 1
                if current_group_size > max_group_size:
                    max_group_size = current_group_size
                    server_with_max_group = server
                end += 1
            else:
                # 형평성 규칙을 만족하지 않으면, 시작 포인터 이동
                start += 1

    return [server_with_max_group, max_group_size]


# 예시 사용
A = 2  # 배수 차이 제한
B = 1000  # 최대 시간 차이 제한 (ms 단위)
delays = [
    [100, 200, 300],
    [200, 300, 400],
    [300, 400, 500]
]  # 예시 delays 배열

print(find_largest_group(A, B, delays))
