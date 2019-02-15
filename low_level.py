import sqlite3

def is_number(in_str):
    try:
        int(in_str)
        return True
    except ValueError: 
        return False

def open_db(db_name):
    try:
        con = sqlite3.connect(db_name)
        return con
    except Exception as e:
        print(e)

    return None

def execute_sql(sql_str, con):
    try:
        cur = con.cursor()
        cur.execute(sql_str)
        out = cur.fetchall()
        con.commit()
        return out
    except Exception as e:
        print(e)

    return None


