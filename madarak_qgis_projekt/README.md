Adatok feltöltésére szolgáló Python modul QGIS térinformatikai programhoz.
A modul segítségével adatokat lehet feltölteni egy spatialite adatbázisba.
QGIS Plugin Builderrel készült, azonban jócskán átalakítottam a jobb érthetőség végett.
A modul csak manuálisan telepíthető.
A Plugin Builderrel létrehozott modulból eltávolítottam minden olyan állományt, amely nem feltétlenül szükséges a futtatáshoz.
Így végül egy teljesen csupasz, minimál modul jött létre, amely alapján szerintem jobban megérthető a QGIS modulok szerkezete.

A madarak könyvtár teljes tartalmát be kell másolni, Windows alatt az alábbi könyvtárba:
c:\Users\UserName\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
Ezt követően a QGIS-en belül a "modulok kezelése és telepítése" ablakban megjelenik majd a modul, amit ki kell pipálni.
A modul működése feltételezi egy megfelelő struktúrájú és nevű spatialite adatbázis meglétét.
Jelen formájában inkább csak mintaként szolgál, az adatbázis nélkül nem használható.
A modulról bővebben a (https://pythondb.wordpress.com/) oldalon lehet majd olvasni.

QGIS 3.22.1-Białowieża alatt létrehozva, tesztelve.
