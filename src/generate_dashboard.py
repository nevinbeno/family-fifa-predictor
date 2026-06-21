import mysql.connector
from dotenv import load_dotenv
import os
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

def generate_dashboard():
    load_dotenv()

    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Total_Score")
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    scores = {
        "Robin": int(row[0]), 
        "Tanya": int(row[1]), 
        "Nevin": int(row[2]), 
        "Niya": int(row[3])
    }

    leaderboard = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # print(f"{leaderboard}")
    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FIFA Prediction League</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css">
        <style>
            *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

            body {
                font-family: system-ui, -apple-system, sans-serif;
                background: #f5f5f0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2rem;

                background-image: url('https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=1600&q=80');
                background-size: cover;
                background-position: center;
            }

            .container { max-width: 520px; width: 100%; }

            .header { text-align: center; margin-bottom: 2rem; }
            .header h1 { font-size: 24px; font-weight: 600; color: #ffffff; }
            .header p  { font-size: 14px; color: #00bcd4; margin-top: 4px; }

            .leaderboard { display: flex; flex-direction: column; gap: 10px; }

            .row {
                display: flex;
                align-items: center;
                gap: 14px;
                padding: 14px 18px;
                background: #ffffff;
                border: 1px solid #e8e8e8;
                border-radius: 12px;
            }
            .row.first { border: 2px solid #EF9F27; }

            .rank { font-size: 13px; font-weight: 600; color: #aaa; min-width: 20px; text-align: center; }
            .rank.gold { color: #BA7517; }

            .avatar {
                width: 40px; height: 40px;
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 13px; font-weight: 600;
                flex-shrink: 0;
            }
            .av-gold   { background: #FAEEDA; color: #633806; }
            .av-silver { background: #f0f0ec; color: #444; }
            .av-bronze { background: #FAECE7; color: #712B13; }
            .av-other  { background: #f0f0ec; color: #888; }

            .name { flex: 1; font-size: 15px; font-weight: 500; color: #1a1a1a; }

            .tied-badge {
                font-size: 11px; color: #999;
                background: #f5f5f0;
                padding: 2px 8px;
                border-radius: 999px;
                border: 1px solid #e0e0d8;
            }

            .points { display: flex; align-items: baseline; gap: 3px; }
            .pts-num   { font-size: 20px; font-weight: 600; color: #1a1a1a; }
            .pts-label { font-size: 12px; color: #aaa; }

            .footer {
                text-align: center;
                margin-top: 1.5rem;
                font-size: 12px;
                color: #aaa;
            }
        </style>
    </head>
    <body>
    <div style="
        position: fixed; inset: 0;
        background: rgba(0, 0, 0, 0.55);
        z-index: 0;
    "></div>

    <div class="container" style="position: relative; z-index: 1;">
        <div class="header">
            <h1>&#127942; FIFA WC 2026 - Kid's Prediction League</h1>
            <p>Season Standings</p>
        </div>
        <div class="leaderboard">
    """

    AVATAR_CLASSES = ["av-gold", "av-silver", "av-bronze", "av-other"]
    MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}
    TEAM_FLAGS = {
        "Tanya": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "Robin": "🇫🇷",
        "Nevin": "🇦🇷", 
        "Niya":  "🇵🇹", 
    }

    rank = 0
    prev_score = None

    for position, (name, points) in enumerate(leaderboard, start=1):
        if points != prev_score:
            rank = position

        initials = name[:2].upper()
        av_class = AVATAR_CLASSES[min(rank - 1, 3)]
        row_class = "row first" if rank == 1 else "row"
        rank_class = "rank gold" if rank == 1 else "rank"
        medal = f'<span style="font-size:18px">{MEDALS[rank]}</span>' if rank in MEDALS else ""

        tied = '<span class="tied-badge">tied</span>' if points == prev_score else ""

        flag = TEAM_FLAGS.get(name, "🏳️")
        html += f"""
            <div class="{row_class}">
                <span class="{rank_class}">{rank}</span>
                <div class="avatar" style="font-size:22px; background:#f5f5f0; border:1px solid #e8e8e8;">{flag}</div>
                <span class="name">{name}</span>
                {tied}
                <div class="points">
                    <span class="pts-num">{points}</span>
                    <span class="pts-label">pts</span>
                </div>
                {medal}
            </div>
        """
        prev_score = points

    last_updated = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y, %I:%M %p IST")
    html += f"""
        </div>
        <p class="footer">
            Last Updated: {last_updated}
        </p>
    </div>
    </body>
    </html>
    """
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    with open(PROJECT_ROOT / "index.html", "w") as f:
        f.write(html)

    print("Dashboard generated successfully!")

if __name__ == "__main__":
    generate_dashboard()