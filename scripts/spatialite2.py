import sqlite3, spatialite

def insertData():
    try:
        sqliteConnection = spatialite.connect('d:\Python\Portable Python-3.10.0 x64\Practice\pythondb\mod_spatialite\madaraszat.sqlite')
        cursor = sqliteConnection.cursor()
        print("Csatlakozva az SQLite adatbázishoz")

        sqlite_insert_query = """INSERT INTO madarak
                          (id, geom, faj, egyedszam, kozseg, kozseg_id, eov_e, eov_n)
                          VALUES (19, ST_GeomFromText('Point(756100.3 329337.8)',23700), 'Carduelis spinus', 2, 'Putnok', 623, 756100.3, 329337.8);"""

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