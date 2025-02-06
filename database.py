import sqlite3

# Initialize Database
DB_NAME = "captions.db"

def init_db():
    """Create a database table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS captions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            caption TEXT,
            alert_triggered INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def save_caption(caption, alert_triggered=0):
    """Insert a new caption log into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO captions (caption, alert_triggered) VALUES (?, ?)", (caption, alert_triggered))
    conn.commit()
    conn.close()

# Initialize the database when the script runs
init_db()

