import os
import unittest
from app.highscore import HighScore


class TestHighScore(unittest.TestCase):
    """Test cases for the HighScore class."""

    def setUp(self):
        """Set up the test environment."""
        self.filename = "test_high_scores.txt"
        self.highscore = HighScore()
        self.highscore.filename = self.filename

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_scores(self):
        """Test if the load_scores method loads high scores from a file correctly."""
        with open(self.filename, "w") as file:
            file.write("Alice,3\n")
            file.write("Bob,5\n")

        self.highscore.load_scores()
        self.assertEqual(self.highscore.scores, [("Alice", 3), ("Bob", 5)])

    def test_add_score(self):
        """Test if the add_score method adds a new score to the high scores list."""
        self.highscore.add_score("Alice", 3)
        self.highscore.add_score("Bob", 5)
        self.assertEqual(self.highscore.scores, [("Alice", 3), ("Bob", 5)])

    def test_add_score_limit(self):
        """Test if the add_score method limits the number of high scores to 10."""
        for i in range(11):
            self.highscore.add_score(f"Player{i}", i + 1)
        self.assertEqual(len(self.highscore.scores), 10)
        self.assertNotIn(("Player0", 1), self.highscore.scores)

    def test_save_scores(self):
        """Test if the save_scores method saves the high scores to a file correctly."""
        self.highscore.add_score("Alice", 3)
        self.highscore.add_score("Bob", 5)
        self.highscore.save_scores()

        with open(self.filename, "r") as file:
            lines = file.readlines()
            self.assertEqual(lines, ["Alice,3\n", "Bob,5\n"])


if __name__ == "__main__":
    unittest.main()
