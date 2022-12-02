import sqlite3

def insertMultipleRecords(recordList):
    try:
        sqliteConnection = sqlite3.connect('d:\Python\Portable Python-3.10.0 x64\Practice\pythondb\madaraszat.db')
        cursor = sqliteConnection.cursor()
        print("Csatlakozva az SQLite adatbázishoz")

        sqlite_insert_query = """INSERT INTO madarak
                          (id, faj, egyedszam, kozseg, kozseg_id, eov_e, eov_n)
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, recordList)
        sqliteConnection.commit()
        print("Összesen", cursor.rowcount, "Sikeres feltöltés")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Sikertelen feltöltés, hiba oka:", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Adatbáziskapcsolat lezárult")

recordsToInsert = [(13, 'Mergus albellus', 1, 'Gyöngyös', 303, 756015.3, 329347.8),]

insertMultipleRecords(recordsToInsert)