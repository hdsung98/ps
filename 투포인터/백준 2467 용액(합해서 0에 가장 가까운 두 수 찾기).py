liquid_num = int(input())
liquids = list(map(int, input().split()))

best_result, best_pair = float('inf'), [0, 0]
left, right = 0, liquid_num - 1

while left < right:
    cur_result = liquids[left] + liquids[right]
    if abs(cur_result) < abs(best_result):
        best_result = cur_result
        best_pair = [liquids[left], liquids[right]]

    if cur_result < 0:
        left += 1
    elif cur_result > 0:
        right -= 1
    else:
        break

print(best_pair[0], best_pair[1])
