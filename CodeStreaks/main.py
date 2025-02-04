from .api import get_user_submissions
from .streak import calculate_streak

def main():
    handle = "handle"  # replace with a valid Codeforces handle
    submissions = get_user_submissions(handle)
    streak = calculate_streak(submissions)
    print(f"{handle}: {streak} days")

if __name__ == "__main__":
    main()