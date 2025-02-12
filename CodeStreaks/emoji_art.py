from datetime import datetime, timedelta, timezone

def generate_emoji_art(submissions, period_length=30):
    today = datetime.now(timezone.utc).date()
    emoji_list = []
    for i in range(period_length):
        check_date = today - timedelta(days=i)
        has_submission = any(
            datetime.fromtimestamp(sub['creationTimeSeconds'], tz=timezone.utc).date() == check_date
            for sub in submissions
        )
        emoji_list.append("🟩" if has_submission else "🟥")
    return ''.join(emoji_list)