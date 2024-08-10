import random

class Deck:

    def __init__(self):
        self.list = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

    def shuffle(self):
        random.shuffle(self.list)

    def display(self):
        print(f"There are {self.count()} cards. ")
        print(self.list)

    def count(self):
        return len(self.list)

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.sum = 0

    def get_card(self, deck_obj):
        self.deck.append(deck_obj.list.pop())

    def get_sum(self):
        self.sum = sum(self.deck)
        return self.sum

    def display(self):
        self.sum = self.get_sum()
        print(f"{self.name} have cards: {self.deck} " + f"The sum is {self.sum}")

class Game:
    def __init__(self, deck, player_list):
        self.deck = deck
        self.player_list = player_list
        self.winner = []
        self.winner_sum = 0

    def shuffle_cards(self):
        self.deck.shuffle()

    def deliver_cards(self):
        for player in self.player_list:
            player.get_card(self.deck)
    
    def dispaly_all(self):
        for player in self.player_list:
            print("------------------------------")
            player.display()

    def dispaly_winner(self):
        if len(self.winner) == 1:
            winner_name = vars(self.winner[0])['name']
            print("******************************")
            print(f"The only winner is {winner_name}, the sum is {self.winner_sum}")
        else:
            winner_name = []
            for player in self.winner:
                winner_name.append(vars(player)['name'])
            print("******************************")
            print(f"The winners are {winner_name}, the sum is {self.winner_sum}")
    
    def get_winner(self):
        winner_sum = 0
        for player in self.player_list:
            if player.get_sum() > winner_sum:
                winner_sum = player.get_sum()
                self.winner = []
                self.winner.append(player)
            elif player.get_sum() == winner_sum:
                self.winner.append(player)
        self.winner_sum = winner_sum


def main():
    deck = Deck()
    player1 = Player('Lyon')
    player2 = Player('Luna')

    game1 = Game(deck, [player1, player2])
    game1.shuffle_cards()
    game1.deliver_cards()
    game1.deliver_cards()
    game1.deliver_cards()
    game1.deliver_cards()
    game1.dispaly_all()
    game1.get_winner()
    game1.dispaly_winner()



if __name__ == '__main__':
    main()