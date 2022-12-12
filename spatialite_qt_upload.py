from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys, sqlite3, spatialite

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("spatialite_qt_upload.ui", self)

        self.pushButton.pressed.connect(self.insertData)

    def insertData(self):
        try:
            sqliteConnection = spatialite.connect("madaraszat.sqlite")
            cursor = sqliteConnection.cursor()
            print("Csatlakozva az SQLite adatbázishoz")

            sqlite_insert_query = ("INSERT INTO madarak \
                              (faj, egyedszam, kozseg, kozseg_id, eov_e, eov_n) \
                              VALUES (?,?,?,?,?,?);")


            v_faj=self.textEdit.toPlainText()
            v_egyedszam=self.spinBox.value()
            v_kozseg=self.textEdit_2.toPlainText()
            v_kozseg_id=self.spinBox_2.value()
            v_eov_e=self.doubleSpinBox.value()
            v_eov_n=self.doubleSpinBox_2.value()
            
            data_tuple = (v_faj, v_egyedszam, v_kozseg, v_kozseg_id, v_eov_e, v_eov_n)

            cursor.execute(sqlite_insert_query, data_tuple)
            sqliteConnection.commit()
            print("Összesen", cursor.rowcount, "Sikeres feltöltés")
            cursor.execute('UPDATE madarak SET Geom=MakePoint(eov_e, eov_n, 23700) WHERE id = (SELECT MAX(id) FROM madarak);')
            sqliteConnection.commit()
            print("Geometria előállítva.")
            cursor.close()

        except sqlite3.Error as error:
            print("Sikertelen feltöltés, hiba oka:", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Adatbáziskapcsolat lezárult")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
