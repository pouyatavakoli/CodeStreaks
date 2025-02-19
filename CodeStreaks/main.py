import argparse
from .api import get_user_submissions
from .utils import load_handles
from .leaderboard import create_leaderboard
from .emoji_art import generate_emoji_art

def main():
    parser = argparse.ArgumentParser(description='CodeStreaks: Track coding streaks of Codeforces users.')
    parser.add_argument('--emoji-art', action='store_true', help='Enable emoji art representation of streaks.')
    parser.add_argument('--only-accepted', action='store_true', help='Only count the accepted submissions')
    args = parser.parse_args()

    handles = load_handles("handles.txt")
    if not handles:
        print("No handles found. Please add user handles to 'handles.txt'.")
        return
    leaderboard = create_leaderboard(handles, args.only_accepted)
    print("CodeStreaks Leaderboard:")
    for rank, (handle, streak) in enumerate(leaderboard, start=1):
        if args.emoji_art:
            submissions = get_user_submissions(handle)
            if args.only_accepted:
                submissions = [sub for sub in submissions if sub.get("verdict") == "OK"]
            emoji_art = generate_emoji_art(submissions)
            if len(handle) > 9:
                print(f"{rank}. {handle[:4]}...{handle[-2:]}: {streak} days \t{emoji_art}")
            else:   
                print(f"{rank}. {handle}: {streak} days \t{emoji_art}")
        else:
            print(f"{rank}. {handle}: {streak} days")

if __name__ == "__main__":
    main()