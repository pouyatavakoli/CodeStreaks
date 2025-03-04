from .api import get_user_submissions
from .streak import calculate_streak

def create_leaderboard(handles, only_accepted):
    leaderboard = []
    for handle in handles:
        try:
            submissions = get_user_submissions(handle)
            if only_accepted:
                submissions = [sub for sub in submissions if sub.get("verdict") == "OK"]
            streak = calculate_streak(submissions)
            leaderboard.append((handle, streak))
        except Exception as e:
            print(f"Error processing {handle}: {e}")
            leaderboard.append((handle, 0))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    return leaderboard
