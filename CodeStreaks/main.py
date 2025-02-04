from .leaderboard import create_leaderboard
from .utils import load_handles

def main():
    handles = load_handles("handles.txt")
    if not handles:
        print("No handles found. Please add user handles to 'handles.txt'.")
        return
    leaderboard = create_leaderboard(handles)
    print("CodeStreaks Leaderboard:")
    for rank, (handle, streak) in enumerate(leaderboard, start=1):
        print(f"{rank}. {handle}: {streak} days")

if __name__ == "__main__":
    main()