string = input().strip()
bomb = input().strip()


def bomb_once(cur_str):
    # 폭탄을 만나면 걔 건너뛰는식의 방식으로, 폭탄 1번터진 후의 문자열을 구하는 방식
    # 매번 문자열 전체를 순회해야하므로 비효율적
    
    new_word = ""
    idx = 0
    exploded = False
    while idx < len(cur_str):
        cur = cur_str[idx]
        if cur_str[idx] != bomb[0]:
            new_word = new_word + cur
        elif cur_str[idx:idx + len(bomb)] == bomb:
            exploded = True
            idx += len(bomb)
            continue
        else:
            new_word = new_word + cur
        idx += 1

    return new_word, exploded


while True:
    left, result = bomb_once(string)
    if not result:
        if left:
            print(left)
        else:
            print("FRULA")
        break
    else:
        string = left


# 개선된 코드: 스택방식
# 폭탄이 중첩되는 것은 괄호검사와 흡사하다
# 제거할 대상이 중첩적으로 나타나고, 나타난 즉시 연쇄적으로 제거하고싶다면 LIFO방식이 효과적


string = input().strip()
bomb = input().strip()

res = []
for ch in string:
    res.append(ch)
    if len(res) >= len(bomb) and ''.join(res[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            res.pop()

result = ''.join(res)

print(result if result else 'FRULA')