import os


class HighScore:
    def __init__(self):
        self.scores = []
        self.filename = "high_scores.txt"

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, score = line.strip().split(",")
                    self.scores.append((name, int(score)))

    def add_score(self, name, score):
        self.scores.append((name, score))
        self.scores = sorted(self.scores, key=lambda x: x[1])
        if len(self.scores) > 10:
            self.scores.pop(0)

    def save_scores(self):
        with open(self.filename, "w") as file:
            for name, score in self.scores:
                file.write(f"{name},{score}\n")

    def print_scores(self):
        try:
            with open("high_scores.txt", "r") as file:
                scores = []
                for line in file:
                    name, score = line.strip().split(",")
                    scores.append((name, int(score)))
                if len(scores) > 0:
                    print("High Scores:")
                    for name, score in scores:
                        print(f"{name}: {score} rounds to win")
                else:
                    print("No high scores to display.")
        except FileNotFoundError:
            print("No high scores to display.")
