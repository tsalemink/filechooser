# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loaddirectoryfiles.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QTreeView, QWidget)

class Ui_LoadDirectoryFilesDialog(object):
    def setupUi(self, LoadDirectoryFilesDialog):
        if not LoadDirectoryFilesDialog.objectName():
            LoadDirectoryFilesDialog.setObjectName(u"LoadDirectoryFilesDialog")
        LoadDirectoryFilesDialog.resize(585, 412)
        self.gridLayout = QGridLayout(LoadDirectoryFilesDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeView = QTreeView(LoadDirectoryFilesDialog)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout.addWidget(self.treeView, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(LoadDirectoryFilesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.lineEditFilterList = QLineEdit(LoadDirectoryFilesDialog)
        self.lineEditFilterList.setObjectName(u"lineEditFilterList")

        self.gridLayout.addWidget(self.lineEditFilterList, 0, 1, 1, 1)

        self.label = QLabel(LoadDirectoryFilesDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(LoadDirectoryFilesDialog)
        self.buttonBox.accepted.connect(LoadDirectoryFilesDialog.accept)
        self.buttonBox.rejected.connect(LoadDirectoryFilesDialog.reject)

        QMetaObject.connectSlotsByName(LoadDirectoryFilesDialog)
    # setupUi

    def retranslateUi(self, LoadDirectoryFilesDialog):
        LoadDirectoryFilesDialog.setWindowTitle(QCoreApplication.translate("LoadDirectoryFilesDialog", u"Load Directory Files", None))
#if QT_CONFIG(tooltip)
        self.lineEditFilterList.setToolTip(QCoreApplication.translate("LoadDirectoryFilesDialog", u"Comma separated list of filters (*.json, *.exf)", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("LoadDirectoryFilesDialog", u"File Filters:", None))
    # retranslateUi

