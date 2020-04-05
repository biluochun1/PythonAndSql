import random
import sys

CARD_SCORE = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}  # 存储牌面和对应的分数
CARD_TYPE = ["Red Tao", "Black Tao", "Square", "Mei Hua"]  # 牌面类型
CARD_VALUE = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]  # 牌面的值


def get_all_combination(l1, l2):
    total_res = []
    for i in l1:
        for j in l2:
            total_res.append(i + " " + j)
    return total_res


def shuffle(card):
    random.shuffle(card)


def get_a_card(l: list):
    return l.pop()


def cal_hand_list_score(l: list):
    score = 0
    ace_flag = False
    for card in l:
        if card[-1] is "A":
            ace_flag = True
        score += CARD_SCORE.get(card[-1])
    if score + 9 <= 21 and ace_flag:
        return score + 9, len(l)
    else:
        return score, len(l)


def check_hand_card_lose(s, c):
    WIN = True
    LOSE = False
    if c > 5 and s <= 21:
        return WIN
    if s > 21:
        return LOSE


def check_zhuang(score1, score2, hand1, hand2):
    if score2 < score1 < 22 and score2 < 22:
        print("U win", hand1, hand2)
        print("the Finally score is {}".format(score1))
    elif score1 < 22 and score2 > 22:
        print("U win", hand1, hand2)
        print("the Finally score is {}".format(score1))
    else:
        print("U Lose", hand1, hand2)
        print("the Finally score is {}".format(score1))


if __name__ == '__main__':
    print("*****2020-04-05*********")
    card_list = get_all_combination(CARD_TYPE, CARD_VALUE)  # 买了一副牌
    print("buy a card")
    shuffle(card_list)  # 洗牌
    print("shuffle card")
    hand = [get_a_card(card_list), get_a_card(card_list)]  # 发了两张牌
    hand_zhuang = [get_a_card(card_list), get_a_card(card_list)]
    print("get two cards:", hand)
    score, count = cal_hand_list_score(hand)  # 计算一下得分
    score_zhuang, count_zhuang = cal_hand_list_score(hand_zhuang)
    print("the current score is {}, cards count is {}".format(score, count))
    flag = input("if get a card？(y/n)")
    if flag is "y":
        hand.append(get_a_card(card_list))  # 又拿了一张牌
        print("current hand card:", hand)
        score, count = cal_hand_list_score(hand)  # 重新计算得分
        print("the current score is {}, cards count is {}".format(score, count))
        if score_zhuang < 18:
            hand_zhuang.append(get_a_card(card_list))
            score_zhuang, count_zhuang = cal_hand_list_score(hand_zhuang)
        if check_hand_card_lose(score, count) is False:
            print("U Lose")
            sys.exit(1)
        if input("if get a card？(y/n)") is "y":
            hand.append(get_a_card(card_list))  # 又拿了一张牌
            print("current hand card:", hand)
            score, count = cal_hand_list_score(hand)  # 重新计算得分
            print("the current score is {}, cards count is {}".format(score, count))
            if score_zhuang < 18:
                hand_zhuang.append(get_a_card(card_list))
                score_zhuang, count_zhuang = cal_hand_list_score(hand_zhuang)
            if check_hand_card_lose(score, count) is False:
                print("U Lose")
                sys.exit(1)
            if input("if get a card？(y/n)") is "y":
                hand.append(get_a_card(card_list))  # 又拿了一张牌
                print("current hand card:", hand)
                score, count = cal_hand_list_score(hand)  # 重新计算得分
                print("the current score is {}, cards count is {}".format(score, count))
                if score_zhuang < 18:
                    hand_zhuang.append(get_a_card(card_list))
                    score_zhuang, count_zhuang = cal_hand_list_score(hand_zhuang)
                if check_hand_card_lose(score, count) is False:
                    print("U Lose")
                    sys.exit(1)
                else:
                    print("has five cards u win ", hand, score, count)
            else:
                check_zhuang(score, score_zhuang, hand, hand_zhuang)
        else:
            check_zhuang(score, score_zhuang, hand, hand_zhuang)
    elif flag is "n":
        check_zhuang(score, score_zhuang, hand, hand_zhuang)
    else:
        print("invalid input")
