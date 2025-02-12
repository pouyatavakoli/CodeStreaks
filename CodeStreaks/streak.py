from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone

def calculate_streak(submissions):
    local_tz = get_localzone()
    today = datetime.now(local_tz).date()
    
    # Extract all submission dates in LOCAL TIMEZONE
    submission_dates = set()
    for sub in submissions:
        # Convert creationTimeSeconds (UTC timestamp) to local datetime
        utc_time = datetime.fromtimestamp(sub["creationTimeSeconds"], tz=pytz.utc)
        local_time = utc_time.astimezone(local_tz)
        submission_dates.add(local_time.date())
    
    # Calculate streak (consecutive days up to today)
    streak = 0
    # Start the streak from yesterday (they still have time to submit for today)
    current_day = today - timedelta(days=1)
    while True:
        if current_day in submission_dates:
            streak += 1
            current_day -= timedelta(days=1)
        else:
            break

    # Count today at the end so it dosn't break the streak
    if today in submission_dates:
        streak += 1
    
    return streak