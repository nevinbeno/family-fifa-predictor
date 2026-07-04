from add_result import add_result
from generate_dashboard import generate_dashboard
import subprocess
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

def publish_result():
    # try:
    #     add_result()
    # except Exception as e:
    #     print(f"Failed to add result: {e}")
    #     return
    try:
        generate_dashboard()
        PROJECT_ROOT=Path(__file__).resolve().parent.parent
        subprocess.run(
        ["git", "add", "."],
        cwd=PROJECT_ROOT,
        check=True
        )
        last_updated = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y, %I:%M %p IST")
        msg = f"Update leaderboard {last_updated}"
        subprocess.run(
        ["git", "commit", "-m", f"{msg}"],
        cwd=PROJECT_ROOT,
        check=True
        )

        subprocess.run(
        ["git", "push"],
        cwd=PROJECT_ROOT,
        check=True
        )

    except Exception as e:
        print(f"Dashboard publish failed: {e}")


if __name__ == "__main__":
    # PROJECT_ROOT=Path(__file__).resolve().parent.parent
    # print(f"{PROJECT_ROOT}")
    # last_updated = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y, %I:%M %p IST")
    # msg = f"Update leaderboard {last_updated}"
    # print(f"{msg}")
    publish_result()