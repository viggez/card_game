from app.highscore import HighScore
from app.deck import Deck
from app.player import Player
from colorama import Fore, Style


class Game:
    """Represents a game of 'War' card game."""

    def __init__(self, p1_name, p2_name, high_score, hard_mode=False):
        """Initialize a game with the given player names and score table."""
        self.deck = Deck()
        self.deck.shuffle()
        self.p1 = Player(Fore.BLUE + p1_name + Style.RESET_ALL)
        self.p2 = Player(Fore.RED + p2_name + Style.RESET_ALL)
        self.high_score = HighScore()
        self.p1_name = (Fore.BLUE + p1_name + Style.RESET_ALL)
        self.p2_name = (Fore.RED + p2_name + Style.RESET_ALL)

        if hard_mode:
            for i in range(20):
                self.p1.add_card(self.deck.draw_card())
            for i in range(32):
                self.p2.add_card(self.deck.draw_card())

        else:
            for i in range(26):
                self.p1.add_card(self.deck.draw_card())
                self.p2.add_card(self.deck.draw_card())

    def play_game(self):
        """Start and play the game."""

        round_num = 1
        game_over = False

        while len(self.p1.gh()) > 0 and len(self.p2.gh()) > 0 and not game_over:
            response = input(f"\nRound {round_num}. Enter to play, or 'q' to quit: ")
            print("-----------------------------------------")
            if response == "q":
                break

            p1_card = self.p1.play_card()
            p2_card = self.p2.play_card()

            if response == "cheat":
                if len(self.p2.gh()) < 5:
                    print("Opponent doesn't have enough cards to steal.")
                else:
                    print(f"{Fore.GREEN}\nCHEAT ENABLED!")
                    print(f"{self.p1} stole 5 cards from {self.p2}\n" + Style.RESET_ALL)
                    for i in range(5):
                        self.p1.add_card(self.p2.remove_card())

            print(f"{self.p1} plays: {p1_card}")
            print(f"{self.p2} plays: {p2_card}")

            if p1_card > p2_card:
                print(f"{self.p1_name}{Fore.GREEN} wins the round!" + Style.RESET_ALL)
                self.p1.add_card(p1_card)
                self.p1.add_card(p2_card)

            elif p2_card > p1_card:
                print(f"{self.p2_name}{Fore.GREEN} wins the round!" + Style.RESET_ALL)
                self.p2.add_card(p2_card)
                self.p2.add_card(p1_card)

            else:
                print(f"{Fore.GREEN}\n=============")
                print(f"{Fore.GREEN}|   W A R   |")
                print(f"{Fore.GREEN}=============")
                cards_in_war = [p1_card, p2_card]
                resolved_war = False

                while not resolved_war:
                    if len(self.p1.gh()) < 4 or len(self.p2.gh()) < 4:
                        print("Not enought cards to play the war!")
                        resolved_war = True
                        game_over = True
                        break

                    for i in range(3):
                        if len(self.p1.gh()) == 0 or len(self.p2.gh()) == 0:
                            resolved_war = True
                            break
                        cards_in_war.append(self.p1.play_card())
                        cards_in_war.append(self.p2.play_card())

                    if resolved_war:
                        break

                    p1_card = self.p1.play_card()
                    p2_card = self.p2.play_card()
                    cards_in_war.append(p1_card)
                    cards_in_war.append(p2_card)

                    print(f"{self.p1} plays: {p1_card}")
                    print(f"{self.p2} plays: {p2_card}")

                    if p1_card > p2_card:
                        print(f"{self.p1_name}{Fore.GREEN} wins the war!" + Style.RESET_ALL)
                        for card in cards_in_war:
                            self.p1.add_card(card)
                        resolved_war = True

                    elif p2_card > p1_card:
                        print(f"{self.p2_name}{Fore.GREEN} wins the war!" + Style.RESET_ALL)
                        for card in cards_in_war:
                            self.p2.add_card(card)
                        resolved_war = True

                    else:
                        print(f"{Fore.GREEN}\nTie! War continues..." + Style.RESET_ALL)

            round_num += 1

        print("Game over!")
        if len(self.p1.gh()) > 0:
            print(f"{self.p1} wins!")
            winner_name = self.p1.name
            winner_score = round_num
        else:
            print(f"{self.p2} wins!")
            winner_name = self.p2.name
            winner_score = round_num

        self.high_score.load_scores()
        self.high_score.add_score(winner_name, winner_score)
        self.high_score.save_scores()


def main():
    high_score = HighScore()
    high_score.load_scores()

    while True:
        print(f"{Fore.GREEN}\n================================")
        print(f"{Fore.GREEN}| Welcome to my card game War! |")
        print(f"{Fore.GREEN}================================" + Style.RESET_ALL)
        print("-------------------------------|")
        print(f"| Menu options:                |")
        print("| 1. Play game                 |")
        print("| 2. Display high scores       |")
        print("| 3. Rules                     |")
        print("| 4. Quit                      |")
        print("|______________________________|")
        choice = input("\n--> Enter your choice: ")
        print("--------------------------")

        if choice == "1":
            p1_name = input("Enter p1 nickname: ")
            p2_name = input("Enter p2 nickname: ")
            hard_mode_choice = input("Play in hard mode? (y/n): ")
            if hard_mode_choice.lower() == "y":
                print(f"{Fore.GREEN}HARD MODE ACTIVATED!")
                print(f"{p2_name} Steals 6 cards from {p1_name}!" + Style.RESET_ALL)
                game = Game(p1_name, p2_name, high_score, hard_mode=True)
            else:
                game = Game(p1_name, p2_name, high_score)
            game.play_game()

        elif choice == "2":
            high_score.print_scores()

        elif choice == "3":
            print("The rules menu has been moved.")
            print("Please check the README.md file")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select one of the following options")

    high_score.save_scores()


if __name__ == "__main__":
    main()
