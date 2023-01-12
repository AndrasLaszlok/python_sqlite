import sqlite3, spatialite

def readSqliteTable():
    try:
        sqliteConnection = spatialite.connect('d:\madaraszat.sqlite')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT id, AsText(Geom), faj, egyedszam, kozseg, kozseg_id, eov_e, eov_n from madarak"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Geom: ", row[1])
            print("faj: ", row[2])
            print("egyedszam: ", row[3])
            print("kozseg: ", row[4])
            print("kozseg_id: ", row[5])
            print("eov_e: ", row[6])
            print("eov_n: ", row[7])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()