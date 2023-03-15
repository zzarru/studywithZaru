def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list


trump_card_list = making_card_list()

import random

player1 = random.choice(trump_card_list)
player2 = random.choice(trump_card_list)

print(player1)
print(player2)
