import sqlite3


conn = sqlite3.connect("patient_records.db", check_same_thread=False)

cursor = conn.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS patients(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

pregnancies INTEGER,

glucose REAL,

bloodpressure REAL,

skinthickness REAL,

insulin REAL,

bmi REAL,

diabetespedigree REAL,

age INTEGER,

prediction TEXT,

probability REAL

)

""")

conn.commit()


def save_patient(data):

    cursor.execute("""

    INSERT INTO patients(

    name,

    pregnancies,

    glucose,

    bloodpressure,

    skinthickness,

    insulin,

    bmi,

    diabetespedigree,

    age,

    prediction,

    probability

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?)

    """, data)

    conn.commit()