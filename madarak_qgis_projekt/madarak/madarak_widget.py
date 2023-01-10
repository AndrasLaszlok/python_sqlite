# -*- coding: utf-8 -*-
"""
/***************************************************************************
 madarakDialog
                                 A QGIS plugin
 madarak adatbázisba lehet feltölteni adatokat
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-12-13
        git sha              : $Format:%H$
        copyright            : (C) 2022 by András Lászlók
        email                : laszlokand@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


import os

from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt import uic

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'madarak_widget.ui'))


class madarakWidget(QWidget, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(madarakWidget, self).__init__(parent)
        self.setupUi(self)