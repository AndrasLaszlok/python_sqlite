import sqlite3

def insertData():
    try:
        sqliteConnection = sqlite3.connect('d:\Python\Portable Python-3.10.0 x64\Practice\pythondb\madaraszat.db')
        cursor = sqliteConnection.cursor()
        print("Csatlakozva az SQLite adatbázishoz")

        sqlite_insert_query = """INSERT INTO madarak
                          (id, faj, egyedszam, kozseg, kozseg_id, eov_e, eov_n)
                          VALUES (14, 'Carduelis carduelis', 2, 'Putnok', 623, 756075.3, 329337.8);"""

        cursor.execute(sqlite_insert_query)
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

insertData()