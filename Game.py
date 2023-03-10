from HighScore import HighScore
from Deck import Deck
from Player import Player
from colorama import Fore, Style


class Game:
    def __init__(self, player1_name, player2_name, high_score):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(Fore.BLUE + player1_name + Style.RESET_ALL)
        self.player2 = Player(Fore.RED + player2_name + Style.RESET_ALL)
        self.high_score = HighScore()

        for i in range(26):
            self.player1.add_card(self.deck.draw_card())
            self.player2.add_card(self.deck.draw_card())

    def play_game(self):
        round_num = 1

        while len(self.player1.get_hand()) > 0 and len(self.player2.get_hand()) > 0:
            response = input(f"\nRound {round_num}. Press Enter to play, or 'q' to quit: ")
            if response == 'q':
                break
            print(f"{self.player1} vs {self.player2}")

            player1_card = self.player1.play_card()
            player2_card = self.player2.play_card()

            if response == 'cheat':
                if len(self.player2.get_hand()) < 5:
                    print("Opponent doesn't have enough cards to steal.")
                else:
                    print("\nCHEAT ENABLED!")
                    print(f"{self.player1} stole 5 cards from {self.player2}\n")
                    for i in range(5):
                        self.player1.add_card(self.player2.remove_card())

            print(f"{self.player1} plays: {player1_card}")
            print(f"{self.player2} plays: {player2_card}")

            if player1_card > player2_card:
                print(f"{self.player1} wins the round!")
                self.player1.add_card(player1_card)
                self.player1.add_card(player2_card)

            elif player2_card > player1_card:
                print(f"{self.player2} wins the round!")
                self.player2.add_card(player2_card)
                self.player2.add_card(player1_card)

            else:
                print(f"{Fore.WHITE}W A R !\n")
                cards_in_war = [player1_card, player2_card]
                resolved_war = False

                while not resolved_war:
                    if len(self.player1.get_hand()) < 4 or len(self.player2.get_hand()) < 4:
                        print("Not enought cards to play the war!")

                    for i in range(3):
                        if len(self.player1.get_hand()) == 0 or len(self.player2.get_hand()) == 0:
                            resolved_war = True
                            break
                        cards_in_war.append(self.player1.play_card())
                        cards_in_war.append(self.player2.play_card())

                    if resolved_war:
                        break

                    player1_card = self.player1.play_card()
                    player2_card = self.player2.play_card()
                    cards_in_war.append(player1_card)
                    cards_in_war.append(player2_card)

                    print(f"{self.player1} plays: {player1_card}")
                    print(f"{self.player2} plays: {player2_card}")

                    if player1_card > player2_card:
                        print(f"{self.player1} wins the war!")
                        for card in cards_in_war:
                            self.player1.add_card(card)
                        resolved_war = True

                    elif player2_card > player1_card:
                        print(f"{self.player2} wins the war!")
                        for card in cards_in_war:
                            self.player2.add_card(card)
                        resolved_war = True

                    else:
                        print(f"{Fore.WHITE}\nTie! War continues...")

                if len(self.player1.get_hand()) == 0 or len(self.player2.get_hand()) == 0:
                    break

            round_num += 1

        print("Game over!")
        if len(self.player1.get_hand()) > 0:
            print(f"{self.player1} wins!")
            winner_name = self.player1.name
            winner_score = round_num
        else:
            print(f"{self.player2} wins!")
            winner_name = self.player2.name
            winner_score = round_num

        self.high_score.load_scores()
        self.high_score.add_score(winner_name, winner_score)
        self.high_score.save_scores()


def main():
    high_score = HighScore()
    high_score.load_scores()

    with open("rules.txt", "r") as f:
        rules = f.read()

    while True:
        print("Welcome to War!")
        print("1. Play game")
        print("2. High score")
        print("3. Rules")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            player1_name = input("Enter player1 nickname: ")
            player2_name = input("Enter player2 nickname: ")
            game = Game(player1_name, player2_name, high_score)
            game.play_game()

        elif choice == "2":
            high_score.print_scores()

        elif choice == "3":
            print("Rules menu option selected.")
            print(rules)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select one of the following options")

    high_score.save_scores()


if __name__ == '__main__':
    main()
