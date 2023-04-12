import os


class HighScore:
    """Represents a high score table for the card game."""

    def __init__(self):
        """Initialize an empty high score table."""
        self.scores = []
        self.filename = "high_scores.txt"

    def load_scores(self):
        """Load high scores from a file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, score = line.strip().split(",")
                    self.scores.append((name, int(score)))

    def add_score(self, name, score):
        """Add a new score to the high score table."""
        self.scores.append((name, score))
        self.scores = sorted(self.scores, key=lambda x: x[1])
        if len(self.scores) > 10:
            self.scores.pop(0)

    def save_scores(self):
        """Save high scores to a file."""
        with open(self.filename, "w") as file:
            for name, score in self.scores:
                file.write(f"{name},{score}\n")

    def print_scores(self):
        """Print the high score table."""
        try:
            with open("high_scores.txt", "r") as file:
                scores = []
                for line in file:
                    name, score = line.strip().split(",")
                    scores.append((name, int(score)))
                if len(scores) > 0:
                    print("\n ↓ High Scores: ↓")
                    for name, score in scores:
                        print(f"{name}: {score} rounds to win")
                        print("---------------------------")
                else:
                    print("\nNo high scores to display.")
        except FileNotFoundError:
            print("No high scores to display.")
