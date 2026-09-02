from collections import Counter

# 遞迴檢查是否能拆成全部面子（順子/刻子）
def remove_sets(cnt):
    # 找第一張還有剩的牌
    for i in range(1, 10):
        if cnt[i] > 0:
            break
    else:
        return True  # 全部拆完

    # 嘗試刻子
    if cnt[i] >= 3:
        cnt[i] -= 3
        if remove_sets(cnt):
            cnt[i] += 3
            return True
        cnt[i] += 3

    # 嘗試順子
    if i <= 7 and cnt[i+1] > 0 and cnt[i+2] > 0:
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1

        if remove_sets(cnt):
            cnt[i] += 1
            cnt[i+1] += 1
            cnt[i+2] += 1
            return True

        cnt[i] += 1
        cnt[i+1] += 1
        cnt[i+2] += 1

    return False


# 檢查 17 張是不是胡牌（5 面子 + 1 雀頭）
def is_win(cards):

    cnt = Counter(cards)

    for pair in range(1, 10):

        if cnt[pair] >= 2:

            temp = cnt.copy()
            temp[pair] -= 2

            if remove_sets(temp):
                return True

    return False


# 對外函式：16 張 -> 是否聽牌 + 等什麼牌
def check(hand):

    nums = list(map(int, hand))

    waits = []

    for add in range(1, 10):

        # 一種牌最多四張
        if nums.count(add) >= 4:
            continue

        test = nums.copy()
        test.append(add)

        if is_win(test):
            waits.append(str(add))

    return len(waits) > 0, waits
