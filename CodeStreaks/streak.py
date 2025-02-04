from datetime import datetime, timedelta, timezone

def calculate_streak(submissions):
    today = datetime.now(timezone.utc).date()
    streak = 0
    for i in range(30):  # Check the last 30 days
        check_date = today - timedelta(days=i)
        has_submission = any(
            datetime.fromtimestamp(sub['creationTimeSeconds'], tz=timezone.utc).date() == check_date
            for sub in submissions
        )
        if has_submission:
            streak += 1
        else:
            break
    return streak
