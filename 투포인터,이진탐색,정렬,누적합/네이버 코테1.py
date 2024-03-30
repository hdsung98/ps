# 1번 문제 요약
# 식물들이 있고, 매일 식물들 중 어느 하나에게 물을 주도록 지정해놓은 스케쥴이 있다고 하자.
# 각 식물별로 물 없이 버틸 수 있는 한계일수가 정해져 있을 때
# 아직 살아있는 식물의 개수를 각 날짜별로 스케쥴 첫날부터 끝날까지 집계해 리스트로 저장하라.
# (즉, 리스트 길이는 스케쥴 길이와 동일하다)

# 주어지는 정보: plants, watered 배열 (각각 길이 최대 30만인 일차원 배열)
# - plants = 각 식물이 물 없이 버틸 수 있는 최대일 수
# (ex. plant[i]=4이면 i번째 식물은 물을 안주고 4일차까지는 행복함)
# - watered = 각 날짜에 어느 식물에게 물 줘야하는지 지정한 스케쥴 정보
# (ex. watered[i] = 3이면 i+1번째날에 인덱스 2에 있는 식물에 물 준 것)

#  주의:
#  1) 물주는 타이밍을 놓쳐 한번 죽은 식물은 다시 물을 줘도 살아나지 않음
#  2) 하루에 한 식물만 물 줄 수 있음
#  3) 0일차에 모든 식물에 물줬다 가정하고 1일차부터 시작
#  4) watered 배열은 인덱스도, 그 값도 1-based임. plant는 0-based. 이 차이를 유념해 코드 작성
#  5) 시간제한 10초, 메모리제한 2GB

# -------------------------------------------
# [접근법]
# 1.초기화: 각 식물의 마지막 생존 가능 날짜를 기록하는 die_date 리스트를 생성하고,
#          0일차에 모든 식물에게 물을 준 것으로 가정하여 초기값을 설정한다.
# 2. 스케쥴 순회: watered 배열을 순회하며, 해당 날짜에 물을 줘야 하는 식물의 die_date를 업데이트한다.
#               식물이 이미 죽었다면 업데이트를 생략한다.
# 3. 결과 리스트 초기화: 스케쥴의 각 날짜별 살아있는 식물 수를 저장할 answer 리스트를 초기화한다.
#                       초기값으로 0일차에는 모든 식물이 살아있다고 가정한다.
# 4. 생존 식물 집계: 각 식물의 die_date를 바탕으로 answer에 생존 식물 수를 집계한다.
# 5. 누적합 계산: answer 리스트의 값을 뒤에서부터 누적합을 통해 업데이트하여, 각 날짜별 살아있는 식물의 최종 수를 계산한다.
# -------------------------------------------

# 핵심: 죽은날 기점으로 그 이전 모든 날에 살아 있다 = 물 줄 때 죽을 날을 갱신 하고, 데스노트 역순으로 "누적합"
# 핵심2: 누적합은 키-값 관점으로. key=날짜, value=살아있는 식물 수
def count_alive_plants(plants, watered):
    n = len(plants)
    m = len(watered)
    death_note = [0] * n

    for i in range(n):
        death_note[i] = plants[i] + 1

    for day, plant_idx in enumerate(watered, start=1):
        idx = plant_idx - 1
        if death_note[idx] >= day:
            death_note[idx] = day + plants[idx]  # "이벤트 기반 업데이트 방식"!! : 물을 주면 목숨이 연장되는 방식

    max_day = max(death_note)  # 식물들 중 가장 늦게 죽는 날을 찾음
    answer = [0] * (max(max_day, m) + 1)  # 최대 죽는 날과 스케쥴 길이 중 큰 값으로 answer 리스트 초기화
    answer[0] = n

    for day in death_note:
        if day <= m:  # 스케쥴 길이 내에서 죽는 식물만 처리
            answer[day - 1] += 1

    for i in range(m - 1, 0, -1):
        answer[i] += answer[i + 1]

    return answer[1:m + 1]  # 1일차부터 스케쥴 길이까지의 결과 반환


plants = [4, 3, 2]
watered = [1, 2, 3, 1, 2, 3, 1]
print(count_alive_plants(plants, watered))
