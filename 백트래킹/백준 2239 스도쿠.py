sudoku = [[0] * 9 for _ in range(9)]
zeros = []
# set의 초기화 방법 기억하기
row, col, box = [set(range(1, 10)) for _ in range(9)], [set(range(1, 10)) for _ in range(9)], [set(range(1, 10)) for _
                                                                                               in range(9)]

for i in range(9):
    line = list(map(int, input().strip()))  # strip 붙이기!, map은 iterable을 두번째인자로 받는다(문자열도 iterable)
    for j, num in enumerate(line):  # enumerate 활용!
        box_idx = (i // 3) * 3 + j // 3
        if num:  # 0이 아닐때의 표현방식
            sudoku[i][j] = num
            row[i].remove(num)
            col[j].remove(num)
            box[box_idx].remove(num)
        else:
            zeros.append((i, j, box_idx))


def dfs(zero_i):
    if zero_i == len(zeros):
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        exit()

    r, c, b = zeros[zero_i]
    for n in range(1, 10):
        if n in row[r] and n in col[c] and n in box[b]:
            # for num in row[x] & col[y] & box[b]: 아니면 아싸리 교집합연산으로 구할 수도 있다
            sudoku[r][c] = n
            row[r].remove(n)  # set은 remove,add로 구현
            col[c].remove(n)
            box[b].remove(n)
            dfs(zero_i + 1)
            sudoku[r][c] = 0  # 백트래킹을 하면 전역변수여도 괜찮다!
            row[r].add(n)
            col[c].add(n)
            box[b].add(n)


dfs(0)
