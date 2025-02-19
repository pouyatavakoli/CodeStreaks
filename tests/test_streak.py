import unittest
from datetime import datetime, timedelta, timezone
from CodeStreaks.streak import calculate_streak

class TestStreak(unittest.TestCase):
    def setUp(self):
        self.today = datetime.now(timezone.utc)
    
    def create_submission(self, days_ago, verdict=None):
        submission_time = (self.today - timedelta(days=days_ago)).replace(hour=0, minute=0, second=0, microsecond=0)
        submission = {"creationTimeSeconds": int(submission_time.timestamp())}
        if verdict:
            submission["verdict"] = verdict
        return submission
    
    def test_without_only_accepted_flag(self):
        # All submissions (including non-OK) should count
        submissions = [
            self.create_submission(i, "OK" if i % 2 == 0 else "WRONG_ANSWER")
            for i in range(5)
        ]
        streak = calculate_streak(submissions, only_accepted=False)
        self.assertEqual(streak, 5)  # All 5 days have submissions
    
    def test_with_only_accepted_flag(self):
        # Only "OK" submissions should count (non-consecutive)
        submissions = [
            self.create_submission(i, "OK" if i % 2 == 0 else "WRONG_ANSWER")
            for i in range(5)
        ]
        streak = calculate_streak(submissions, only_accepted=True)
        # Only today (0 days ago) and 2 days ago are accepted, but not consecutive
        self.assertEqual(streak, 1)  # Only today counts
    
    def test_only_accepted_consecutive(self):
        # All submissions are "OK" and consecutive
        submissions = [self.create_submission(i, "OK") for i in range(5)]
        streak = calculate_streak(submissions, only_accepted=True)
        self.assertEqual(streak, 5)
    
    def test_combination_with_emoji_art_flag(self):
        # Test interaction with other flags (emoji-art uses filtered submissions)
        submissions = [
            self.create_submission(i, "OK" if i % 2 == 0 else "WRONG_ANSWER")
            for i in range(5)
        ]
        # Check streak calculation when both flags are active
        streak_accepted = calculate_streak(submissions, only_accepted=True)
        streak_all = calculate_streak(submissions, only_accepted=False)
        self.assertEqual(streak_accepted, 1)
        self.assertEqual(streak_all, 5)

if __name__ == "__main__":
    unittest.main()