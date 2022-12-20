# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(776, 612)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_2 = QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonAdd = QPushButton(self.configGroupBox)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")

        self.verticalLayout.addWidget(self.pushButtonAdd)

        self.pushButtonRemove = QPushButton(self.configGroupBox)
        self.pushButtonRemove.setObjectName(u"pushButtonRemove")

        self.verticalLayout.addWidget(self.pushButtonRemove)

        self.pushButtonRemoveAll = QPushButton(self.configGroupBox)
        self.pushButtonRemoveAll.setObjectName(u"pushButtonRemoveAll")

        self.verticalLayout.addWidget(self.pushButtonRemoveAll)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.gridLayout_2.addWidget(self.lineEditIdentifier, 0, 1, 1, 1)

        self.listWidgetFiles = QListWidget(self.configGroupBox)
        self.listWidgetFiles.setObjectName(u"listWidgetFiles")
        self.listWidgetFiles.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidgetFiles.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.listWidgetFiles, 1, 1, 1, 1)

        self.labelIdentifier = QLabel(self.configGroupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.gridLayout_2.addWidget(self.labelIdentifier, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Multiple File Chooser", None))
        self.configGroupBox.setTitle("")
        self.pushButtonAdd.setText(QCoreApplication.translate("ConfigureDialog", u"Add", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemove.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Remove selected", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemove.setText(QCoreApplication.translate("ConfigureDialog", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemoveAll.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Remove selected", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemoveAll.setText(QCoreApplication.translate("ConfigureDialog", u"Remove All", None))
        self.labelIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:  ", None))
    # retranslateUi

