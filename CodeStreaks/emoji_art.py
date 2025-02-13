from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone

def generate_emoji_art(submissions, period_length=30):
    local_tz = get_localzone()
    today = datetime.now(local_tz).date()
    emoji_list = []
    
    for i in range(period_length):
        check_date = today - timedelta(days=i)
        has_submission = any(
            datetime.fromtimestamp(sub['creationTimeSeconds'], tz=pytz.utc).astimezone(local_tz).date() == check_date
            for sub in submissions
        )
        emoji_list.append("🟩" if has_submission else "🟥")
    
    return ''.join(emoji_list)