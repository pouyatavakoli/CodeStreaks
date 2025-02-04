import unittest
from datetime import datetime, timedelta, timezone
from CodeStreaks.streak import calculate_streak

class TestStreak(unittest.TestCase):
    def test_calculate_streak(self):
        # mock submissions for testing
        today = datetime.now(timezone.utc)
        submissions = [
            {"creationTimeSeconds": int((today - timedelta(days=i)).replace(hour=0, minute=0, second=0, microsecond=0).timestamp())}
            for i in range(5)  # 5-day streak
        ]
        streak = calculate_streak(submissions)
        self.assertEqual(streak, 5)

