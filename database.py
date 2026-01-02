import sqlite3
 
def connect_db():
    return sqlite3.connect("expensed.db")

def create_table():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   category TEXT,
                   amount REAL,
                   date TEXT,
                   note TEXT
                   )
                """)
    conn.commit()
    conn.close()

def insert_expense(category,amount,date,note):
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (category, amount, date, note) VALUES (?, ?, ?, ?)",
        (category, amount, date, note)
    )
    conn.commit()
    conn.close()

def fetch_expenses():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows=cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()