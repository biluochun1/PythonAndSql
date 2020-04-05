if __name__ == '__main__':
    card_score_dict = {
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
    # hand_card = "K"
    hand_cards = ["2", "3", "4", "K", "Q"]  # list
    score = 0
    for card in hand_cards:
        score = score + card_score_dict.get(card)
    print("score:", score)
    if score > 21:
        print("lose")
    else:
        print("win")

    while score <= 50:
        score += 20
        print(score)
