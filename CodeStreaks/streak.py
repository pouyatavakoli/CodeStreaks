from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone

def calculate_streak(submissions, only_accepted=False):
    local_tz = get_localzone()
    today = datetime.now(local_tz).date()
    
    if only_accepted:
        submissions = [sub for sub in submissions if sub.get("verdict") == "OK"]
    
    submission_dates = set()
    for sub in submissions:
        utc_time = datetime.fromtimestamp(sub["creationTimeSeconds"], tz=pytz.utc)
        local_time = utc_time.astimezone(local_tz)
        submission_dates.add(local_time.date())
    
    streak = 0
    current_day = today - timedelta(days=1)
    while True:
        if current_day in submission_dates:
            streak += 1
            current_day -= timedelta(days=1)
        else:
            break

    if today in submission_dates:
        streak += 1
    
    return streak