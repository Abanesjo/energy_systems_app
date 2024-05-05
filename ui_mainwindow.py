# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1092, 1154)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.button_hydraulic = QTabWidget(self.centralwidget)
        self.button_hydraulic.setObjectName(u"button_hydraulic")
        self.pressure_drop = QWidget()
        self.pressure_drop.setObjectName(u"pressure_drop")
        self.verticalLayout_7 = QVBoxLayout(self.pressure_drop)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea = QScrollArea(self.pressure_drop)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1034, 1350))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.d = QLineEdit(self.groupBox)
        self.d.setObjectName(u"d")

        self.gridLayout_6.addWidget(self.d, 2, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 3, 2, 1, 1)

        self.nominal_size = QLineEdit(self.groupBox)
        self.nominal_size.setObjectName(u"nominal_size")

        self.gridLayout_6.addWidget(self.nominal_size, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)

        self.absolute_roughness = QLineEdit(self.groupBox)
        self.absolute_roughness.setObjectName(u"absolute_roughness")

        self.gridLayout_6.addWidget(self.absolute_roughness, 1, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)

        self.material_and_schedule = QLineEdit(self.groupBox)
        self.material_and_schedule.setObjectName(u"material_and_schedule")

        self.gridLayout_6.addWidget(self.material_and_schedule, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 1, 2, 1, 1)

        self.line_description = QLineEdit(self.groupBox)
        self.line_description.setObjectName(u"line_description")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_description.sizePolicy().hasHeightForWidth())
        self.line_description.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.line_description, 0, 1, 1, 3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 2, 2, 1, 1)

        self.D = QLineEdit(self.groupBox)
        self.D.setObjectName(u"D")
        self.D.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.D.setReadOnly(True)

        self.gridLayout_6.addWidget(self.D, 3, 3, 1, 1)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 1, 4, 1, 1)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 2, 4, 1, 1)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_6.addWidget(self.label_23, 3, 4, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_6)


        self.verticalLayout_13.addWidget(self.groupBox)

        self.tab_fluid_properties = QTabWidget(self.scrollAreaWidgetContents_3)
        self.tab_fluid_properties.setObjectName(u"tab_fluid_properties")
        sizePolicy1.setHeightForWidth(self.tab_fluid_properties.sizePolicy().hasHeightForWidth())
        self.tab_fluid_properties.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalGroupBox = QGroupBox(self.tab)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_12 = QLabel(self.verticalGroupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 1, 1, 1, 1)

        self.line_edit_source_h = QLineEdit(self.verticalGroupBox)
        self.line_edit_source_h.setObjectName(u"line_edit_source_h")

        self.gridLayout_2.addWidget(self.line_edit_source_h, 1, 2, 1, 1)

        self.line_edit_source_p = QLineEdit(self.verticalGroupBox)
        self.line_edit_source_p.setObjectName(u"line_edit_source_p")

        self.gridLayout_2.addWidget(self.line_edit_source_p, 0, 0, 1, 1)

        self.label_14 = QLabel(self.verticalGroupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 0, 3, 1, 1)

        self.line_edit_source_q = QLineEdit(self.verticalGroupBox)
        self.line_edit_source_q.setObjectName(u"line_edit_source_q")

        self.gridLayout_2.addWidget(self.line_edit_source_q, 1, 0, 1, 1)

        self.label_13 = QLabel(self.verticalGroupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)

        self.label_11 = QLabel(self.verticalGroupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 3, 1, 1)

        self.line_edit_source_t = QLineEdit(self.verticalGroupBox)
        self.line_edit_source_t.setObjectName(u"line_edit_source_t")

        self.gridLayout_2.addWidget(self.line_edit_source_t, 0, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox)

        self.verticalGroupBox_2 = QGroupBox(self.tab)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalGroupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_edit_destination_t = QLineEdit(self.verticalGroupBox_2)
        self.line_edit_destination_t.setObjectName(u"line_edit_destination_t")

        self.gridLayout_3.addWidget(self.line_edit_destination_t, 0, 2, 1, 1)

        self.label_17 = QLabel(self.verticalGroupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 1)

        self.line_edit_destination_h = QLineEdit(self.verticalGroupBox_2)
        self.line_edit_destination_h.setObjectName(u"line_edit_destination_h")

        self.gridLayout_3.addWidget(self.line_edit_destination_h, 1, 2, 1, 1)

        self.label_18 = QLabel(self.verticalGroupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 3, 1, 1)

        self.line_edit_destination_q = QLineEdit(self.verticalGroupBox_2)
        self.line_edit_destination_q.setObjectName(u"line_edit_destination_q")

        self.gridLayout_3.addWidget(self.line_edit_destination_q, 1, 0, 1, 1)

        self.label_15 = QLabel(self.verticalGroupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 3, 1, 1)

        self.line_edit_destination_p = QLineEdit(self.verticalGroupBox_2)
        self.line_edit_destination_p.setObjectName(u"line_edit_destination_p")

        self.gridLayout_3.addWidget(self.line_edit_destination_p, 0, 0, 1, 1)

        self.label_16 = QLabel(self.verticalGroupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.tab_fluid_properties.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.line_edit_p_avg = QLineEdit(self.tab_2)
        self.line_edit_p_avg.setObjectName(u"line_edit_p_avg")

        self.horizontalLayout_3.addWidget(self.line_edit_p_avg)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.line_edit_t_avg = QLineEdit(self.tab_2)
        self.line_edit_t_avg.setObjectName(u"line_edit_t_avg")

        self.horizontalLayout_2.addWidget(self.line_edit_t_avg)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.line_edit_q = QLineEdit(self.tab_2)
        self.line_edit_q.setObjectName(u"line_edit_q")

        self.horizontalLayout.addWidget(self.line_edit_q)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tab_fluid_properties.addTab(self.tab_2, "")

        self.verticalLayout_13.addWidget(self.tab_fluid_properties)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_27 = QLabel(self.groupBox_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_7.addWidget(self.label_27)

        self.line_edit_V = QLineEdit(self.groupBox_2)
        self.line_edit_V.setObjectName(u"line_edit_V")
        self.line_edit_V.setAutoFillBackground(False)
        self.line_edit_V.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_V.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.line_edit_V)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_7.addWidget(self.label_26)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_7.addWidget(self.label_25)

        self.line_edit_mu = QLineEdit(self.groupBox_2)
        self.line_edit_mu.setObjectName(u"line_edit_mu")
        self.line_edit_mu.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_mu.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.line_edit_mu)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_7.addWidget(self.label_24)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_36 = QLabel(self.groupBox_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setPixmap(QPixmap(u":/images/f_laminar.png"))

        self.gridLayout_7.addWidget(self.label_36, 4, 2, 1, 1)

        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setPixmap(QPixmap(u":/images/f_turbulent.png"))

        self.gridLayout_7.addWidget(self.label_35, 3, 2, 1, 1)

        self.label_37 = QLabel(self.groupBox_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_7.addWidget(self.label_37, 0, 4, 1, 1)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setPixmap(QPixmap(u":/images/Re.png"))

        self.gridLayout_7.addWidget(self.label_34, 1, 2, 1, 1)

        self.line_edit_vel = QLineEdit(self.groupBox_2)
        self.line_edit_vel.setObjectName(u"line_edit_vel")
        self.line_edit_vel.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_vel.setReadOnly(True)

        self.gridLayout_7.addWidget(self.line_edit_vel, 0, 3, 1, 1)

        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.line_edit_vel2 = QLineEdit(self.groupBox_2)
        self.line_edit_vel2.setObjectName(u"line_edit_vel2")
        self.line_edit_vel2.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_vel2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.line_edit_vel2, 0, 5, 1, 1)

        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 0, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 2, 0, 1, 2)

        self.line_edit_f = QLineEdit(self.groupBox_2)
        self.line_edit_f.setObjectName(u"line_edit_f")
        self.line_edit_f.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_f.setReadOnly(True)

        self.gridLayout_7.addWidget(self.line_edit_f, 2, 3, 3, 2)

        self.label_38 = QLabel(self.groupBox_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_7.addWidget(self.label_38, 0, 6, 1, 1)

        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 1, 0, 1, 2)

        self.label_33 = QLabel(self.groupBox_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setPixmap(QPixmap(u":/images/Vel.png"))

        self.gridLayout_7.addWidget(self.label_33, 0, 2, 1, 1)

        self.line_edit_Re = QLineEdit(self.groupBox_2)
        self.line_edit_Re.setObjectName(u"line_edit_Re")
        self.line_edit_Re.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_Re.setReadOnly(True)

        self.gridLayout_7.addWidget(self.line_edit_Re, 1, 3, 1, 2)

        self.label_32 = QLabel(self.groupBox_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_7.addWidget(self.label_32, 4, 1, 1, 1)

        self.line_edit_fluid_type = QLineEdit(self.groupBox_2)
        self.line_edit_fluid_type.setObjectName(u"line_edit_fluid_type")
        self.line_edit_fluid_type.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_fluid_type.setReadOnly(True)

        self.gridLayout_7.addWidget(self.line_edit_fluid_type, 2, 5, 3, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_7)


        self.verticalLayout_13.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.table_fittings = QTableWidget(self.groupBox_4)
        if (self.table_fittings.columnCount() < 3):
            self.table_fittings.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_fittings.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_fittings.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_fittings.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_fittings.rowCount() < 2):
            self.table_fittings.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_fittings.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_fittings.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_fittings.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_fittings.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_fittings.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_fittings.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_fittings.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_fittings.setItem(1, 2, __qtablewidgetitem10)
        self.table_fittings.setObjectName(u"table_fittings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_fittings.sizePolicy().hasHeightForWidth())
        self.table_fittings.setSizePolicy(sizePolicy2)
        self.table_fittings.setMinimumSize(QSize(0, 200))
        self.table_fittings.horizontalHeader().setCascadingSectionResizes(True)
        self.table_fittings.horizontalHeader().setMinimumSectionSize(26)
        self.table_fittings.horizontalHeader().setDefaultSectionSize(223)
        self.table_fittings.horizontalHeader().setStretchLastSection(False)
        self.table_fittings.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_14.addWidget(self.table_fittings)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(320, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.button_add_row = QPushButton(self.groupBox_4)
        self.button_add_row.setObjectName(u"button_add_row")

        self.horizontalLayout_4.addWidget(self.button_add_row)

        self.button_remove_row = QPushButton(self.groupBox_4)
        self.button_remove_row.setObjectName(u"button_remove_row")

        self.horizontalLayout_4.addWidget(self.button_remove_row)

        self.button_reset_rows = QPushButton(self.groupBox_4)
        self.button_reset_rows.setObjectName(u"button_reset_rows")

        self.horizontalLayout_4.addWidget(self.button_reset_rows)

        self.label_39 = QLabel(self.groupBox_4)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_4.addWidget(self.label_39)

        self.line_edit_fittings_total = QLineEdit(self.groupBox_4)
        self.line_edit_fittings_total.setObjectName(u"line_edit_fittings_total")
        self.line_edit_fittings_total.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_fittings_total.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.line_edit_fittings_total)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.button_pipe_calculate = QPushButton(self.groupBox_4)
        self.button_pipe_calculate.setObjectName(u"button_pipe_calculate")

        self.verticalLayout_14.addWidget(self.button_pipe_calculate)

        self.groupBox_3 = QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_54 = QLabel(self.groupBox_3)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_4.addWidget(self.label_54, 5, 5, 1, 1)

        self.label_42 = QLabel(self.groupBox_3)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_4.addWidget(self.label_42, 3, 0, 1, 1)

        self.label_55 = QLabel(self.groupBox_3)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_4.addWidget(self.label_55, 6, 5, 1, 1)

        self.line_edit_static_head_m = QLineEdit(self.groupBox_3)
        self.line_edit_static_head_m.setObjectName(u"line_edit_static_head_m")

        self.gridLayout_4.addWidget(self.line_edit_static_head_m, 5, 2, 1, 1)

        self.label_46 = QLabel(self.groupBox_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setTextFormat(Qt.MarkdownText)

        self.gridLayout_4.addWidget(self.label_46, 7, 0, 1, 1)

        self.label_61 = QLabel(self.groupBox_3)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_4.addWidget(self.label_61, 0, 5, 1, 1)

        self.line_edit_delta_p = QLineEdit(self.groupBox_3)
        self.line_edit_delta_p.setObjectName(u"line_edit_delta_p")
        self.line_edit_delta_p.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_4.addWidget(self.line_edit_delta_p, 4, 4, 1, 1)

        self.line_edit_l_p = QLineEdit(self.groupBox_3)
        self.line_edit_l_p.setObjectName(u"line_edit_l_p")

        self.gridLayout_4.addWidget(self.line_edit_l_p, 1, 4, 1, 1)

        self.label_49 = QLabel(self.groupBox_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setPixmap(QPixmap(u":/images/L_TEL.png"))

        self.gridLayout_4.addWidget(self.label_49, 2, 1, 1, 1)

        self.label_56 = QLabel(self.groupBox_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setTextFormat(Qt.MarkdownText)

        self.gridLayout_4.addWidget(self.label_56, 7, 5, 1, 1)

        self.line_edit_misc_bar = QLineEdit(self.groupBox_3)
        self.line_edit_misc_bar.setObjectName(u"line_edit_misc_bar")
        self.line_edit_misc_bar.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_4.addWidget(self.line_edit_misc_bar, 6, 4, 1, 1)

        self.label_59 = QLabel(self.groupBox_3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_4.addWidget(self.label_59, 2, 5, 1, 1)

        self.line_edit_l_tel = QLineEdit(self.groupBox_3)
        self.line_edit_l_tel.setObjectName(u"line_edit_l_tel")
        self.line_edit_l_tel.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_4.addWidget(self.line_edit_l_tel, 2, 4, 1, 1)

        self.line_edit_static_head_bar = QLineEdit(self.groupBox_3)
        self.line_edit_static_head_bar.setObjectName(u"line_edit_static_head_bar")
        self.line_edit_static_head_bar.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_4.addWidget(self.line_edit_static_head_bar, 5, 4, 1, 1)

        self.line_edit_l_f = QLineEdit(self.groupBox_3)
        self.line_edit_l_f.setObjectName(u"line_edit_l_f")
        self.line_edit_l_f.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_l_f.setReadOnly(True)

        self.gridLayout_4.addWidget(self.line_edit_l_f, 0, 4, 1, 1)

        self.label_40 = QLabel(self.groupBox_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_51 = QLabel(self.groupBox_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setPixmap(QPixmap(u":/images/delta_P.png"))

        self.gridLayout_4.addWidget(self.label_51, 4, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_3)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_4.addWidget(self.label_48, 2, 0, 1, 1)

        self.label_58 = QLabel(self.groupBox_3)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_4.addWidget(self.label_58, 3, 5, 1, 1)

        self.line_edit_h_l = QLineEdit(self.groupBox_3)
        self.line_edit_h_l.setObjectName(u"line_edit_h_l")
        self.line_edit_h_l.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_4.addWidget(self.line_edit_h_l, 3, 4, 1, 1)

        self.label_45 = QLabel(self.groupBox_3)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_4.addWidget(self.label_45, 6, 0, 1, 1)

        self.label_52 = QLabel(self.groupBox_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setPixmap(QPixmap(u":/images/bar.png"))

        self.gridLayout_4.addWidget(self.label_52, 5, 1, 1, 1)

        self.label_60 = QLabel(self.groupBox_3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_4.addWidget(self.label_60, 1, 5, 1, 1)

        self.label_41 = QLabel(self.groupBox_3)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_4.addWidget(self.label_41, 1, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_4.addWidget(self.label_43, 4, 0, 1, 1)

        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_4.addWidget(self.label_44, 5, 0, 1, 1)

        self.label_47 = QLabel(self.groupBox_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setPixmap(QPixmap(u":/images/L_f.png"))

        self.gridLayout_4.addWidget(self.label_47, 0, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setPixmap(QPixmap(u":/images/h_L.png"))

        self.gridLayout_4.addWidget(self.label_50, 3, 1, 1, 1)

        self.label_57 = QLabel(self.groupBox_3)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_4.addWidget(self.label_57, 4, 5, 1, 1)

        self.label_53 = QLabel(self.groupBox_3)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_4.addWidget(self.label_53, 5, 3, 1, 1)

        self.line_edit_pressure_drop = QLineEdit(self.groupBox_3)
        self.line_edit_pressure_drop.setObjectName(u"line_edit_pressure_drop")
        self.line_edit_pressure_drop.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(85, 170, 255)\n"
"}")

        self.gridLayout_4.addWidget(self.line_edit_pressure_drop, 7, 4, 1, 1)

        self.line_edit_misc_m = QLineEdit(self.groupBox_3)
        self.line_edit_misc_m.setObjectName(u"line_edit_misc_m")

        self.gridLayout_4.addWidget(self.line_edit_misc_m, 6, 2, 1, 1)

        self.label_62 = QLabel(self.groupBox_3)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_4.addWidget(self.label_62, 6, 3, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_4)

        self.button_pipe_excel = QPushButton(self.groupBox_3)
        self.button_pipe_excel.setObjectName(u"button_pipe_excel")

        self.verticalLayout_12.addWidget(self.button_pipe_excel)


        self.verticalLayout_14.addWidget(self.groupBox_3)


        self.verticalLayout_13.addWidget(self.groupBox_4)


        self.gridLayout.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.button_hydraulic.addTab(self.pressure_drop, "")
        self.wall_thickness = QWidget()
        self.wall_thickness.setObjectName(u"wall_thickness")
        self.verticalLayout_15 = QVBoxLayout(self.wall_thickness)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.button_wall_autofill = QPushButton(self.wall_thickness)
        self.button_wall_autofill.setObjectName(u"button_wall_autofill")

        self.verticalLayout_15.addWidget(self.button_wall_autofill)

        self.groupBox_5 = QGroupBox(self.wall_thickness)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_69 = QLabel(self.groupBox_5)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_5.addWidget(self.label_69, 4, 2, 1, 1)

        self.label_65 = QLabel(self.groupBox_5)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_5.addWidget(self.label_65, 3, 0, 1, 1)

        self.line_edit_applicable_pipes = QLineEdit(self.groupBox_5)
        self.line_edit_applicable_pipes.setObjectName(u"line_edit_applicable_pipes")

        self.gridLayout_5.addWidget(self.line_edit_applicable_pipes, 1, 1, 1, 1)

        self.label_68 = QLabel(self.groupBox_5)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_5.addWidget(self.label_68, 3, 2, 1, 1)

        self.label_66 = QLabel(self.groupBox_5)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_5.addWidget(self.label_66, 4, 0, 1, 1)

        self.label_67 = QLabel(self.groupBox_5)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_5.addWidget(self.label_67, 1, 2, 1, 1)

        self.label_63 = QLabel(self.groupBox_5)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_5.addWidget(self.label_63, 0, 0, 1, 1)

        self.line_edit_BREI = QLineEdit(self.groupBox_5)
        self.line_edit_BREI.setObjectName(u"line_edit_BREI")

        self.gridLayout_5.addWidget(self.line_edit_BREI, 3, 1, 1, 1)

        self.line_edit_pipeline_identification = QLineEdit(self.groupBox_5)
        self.line_edit_pipeline_identification.setObjectName(u"line_edit_pipeline_identification")

        self.gridLayout_5.addWidget(self.line_edit_pipeline_identification, 0, 1, 1, 1)

        self.label_64 = QLabel(self.groupBox_5)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_5.addWidget(self.label_64, 1, 0, 1, 1)

        self.line_edit_design_temperature = QLineEdit(self.groupBox_5)
        self.line_edit_design_temperature.setObjectName(u"line_edit_design_temperature")

        self.gridLayout_5.addWidget(self.line_edit_design_temperature, 4, 3, 1, 1)

        self.line_edit_fahrenheit = QLineEdit(self.groupBox_5)
        self.line_edit_fahrenheit.setObjectName(u"line_edit_fahrenheit")
        self.line_edit_fahrenheit.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_fahrenheit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.line_edit_fahrenheit, 4, 5, 1, 1)

        self.label_103 = QLabel(self.groupBox_5)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_5.addWidget(self.label_103, 4, 4, 1, 1)

        self.line_edit_ASTM = QLineEdit(self.groupBox_5)
        self.line_edit_ASTM.setObjectName(u"line_edit_ASTM")

        self.gridLayout_5.addWidget(self.line_edit_ASTM, 4, 1, 1, 1)

        self.label_95 = QLabel(self.groupBox_5)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_5.addWidget(self.label_95, 4, 6, 1, 1)

        self.label_102 = QLabel(self.groupBox_5)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_5.addWidget(self.label_102, 3, 6, 1, 1)

        self.line_edit_design_pressure = QLineEdit(self.groupBox_5)
        self.line_edit_design_pressure.setObjectName(u"line_edit_design_pressure")

        self.gridLayout_5.addWidget(self.line_edit_design_pressure, 3, 3, 1, 3)

        self.line_edit_fluid = QLineEdit(self.groupBox_5)
        self.line_edit_fluid.setObjectName(u"line_edit_fluid")

        self.gridLayout_5.addWidget(self.line_edit_fluid, 1, 3, 1, 3)


        self.verticalLayout_15.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.wall_thickness)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.gridLayout_9 = QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_78 = QLabel(self.groupBox_6)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_9.addWidget(self.label_78, 7, 0, 1, 4)

        self.label_74 = QLabel(self.groupBox_6)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_9.addWidget(self.label_74, 3, 0, 1, 3)

        self.line_edit_Y = QLineEdit(self.groupBox_6)
        self.line_edit_Y.setObjectName(u"line_edit_Y")

        self.gridLayout_9.addWidget(self.line_edit_Y, 4, 8, 1, 1)

        self.label_96 = QLabel(self.groupBox_6)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_9.addWidget(self.label_96, 5, 9, 1, 1)

        self.line_edit_BEND = QLineEdit(self.groupBox_6)
        self.line_edit_BEND.setObjectName(u"line_edit_BEND")

        self.gridLayout_9.addWidget(self.line_edit_BEND, 7, 8, 1, 1)

        self.label_71 = QLabel(self.groupBox_6)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setPixmap(QPixmap(u":/images/t_n.png"))
        self.label_71.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_71, 0, 6, 1, 2)

        self.line_edit_SE_ksi = QLineEdit(self.groupBox_6)
        self.line_edit_SE_ksi.setObjectName(u"line_edit_SE_ksi")

        self.gridLayout_9.addWidget(self.line_edit_SE_ksi, 3, 6, 1, 1)

        self.line_edit_P_display = QLineEdit(self.groupBox_6)
        self.line_edit_P_display.setObjectName(u"line_edit_P_display")
        self.line_edit_P_display.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_9.addWidget(self.line_edit_P_display, 1, 8, 1, 1)

        self.label_92 = QLabel(self.groupBox_6)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_9.addWidget(self.label_92, 1, 9, 1, 1)

        self.line_edit_MFG = QLineEdit(self.groupBox_6)
        self.line_edit_MFG.setObjectName(u"line_edit_MFG")

        self.gridLayout_9.addWidget(self.line_edit_MFG, 6, 8, 1, 1)

        self.label_83 = QLabel(self.groupBox_6)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_9.addWidget(self.label_83, 2, 4, 1, 1)

        self.line_edit_SE = QLineEdit(self.groupBox_6)
        self.line_edit_SE.setObjectName(u"line_edit_SE")
        self.line_edit_SE.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_SE.setReadOnly(True)

        self.gridLayout_9.addWidget(self.line_edit_SE, 3, 8, 1, 1)

        self.line_edit_A = QLineEdit(self.groupBox_6)
        self.line_edit_A.setObjectName(u"line_edit_A")

        self.gridLayout_9.addWidget(self.line_edit_A, 5, 8, 1, 1)

        self.label_88 = QLabel(self.groupBox_6)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_9.addWidget(self.label_88, 7, 4, 1, 4)

        self.label_70 = QLabel(self.groupBox_6)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setPixmap(QPixmap(u":/images/t_m.png"))
        self.label_70.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_70, 0, 4, 1, 1)

        self.label_82 = QLabel(self.groupBox_6)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_9.addWidget(self.label_82, 1, 4, 1, 1)

        self.label_93 = QLabel(self.groupBox_6)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_9.addWidget(self.label_93, 2, 9, 1, 1)

        self.label_94 = QLabel(self.groupBox_6)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_9.addWidget(self.label_94, 3, 9, 1, 1)

        self.label_73 = QLabel(self.groupBox_6)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_9.addWidget(self.label_73, 2, 0, 1, 4)

        self.label_72 = QLabel(self.groupBox_6)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_9.addWidget(self.label_72, 1, 0, 1, 4)

        self.label_97 = QLabel(self.groupBox_6)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_9.addWidget(self.label_97, 3, 7, 1, 1)

        self.label_87 = QLabel(self.groupBox_6)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_9.addWidget(self.label_87, 6, 4, 1, 1)

        self.label_85 = QLabel(self.groupBox_6)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_9.addWidget(self.label_85, 4, 4, 1, 1)

        self.label_77 = QLabel(self.groupBox_6)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_9.addWidget(self.label_77, 6, 0, 1, 3)

        self.label_75 = QLabel(self.groupBox_6)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_9.addWidget(self.label_75, 4, 0, 1, 3)

        self.line_edit_internal_diameter = QLineEdit(self.groupBox_6)
        self.line_edit_internal_diameter.setObjectName(u"line_edit_internal_diameter")

        self.gridLayout_9.addWidget(self.line_edit_internal_diameter, 2, 8, 1, 1)

        self.label_86 = QLabel(self.groupBox_6)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_9.addWidget(self.label_86, 5, 4, 1, 4)

        self.label_76 = QLabel(self.groupBox_6)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_9.addWidget(self.label_76, 5, 0, 1, 3)

        self.label_84 = QLabel(self.groupBox_6)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_9.addWidget(self.label_84, 3, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 3, 5, 1, 1)


        self.verticalLayout_15.addWidget(self.groupBox_6)

        self.button_wall_calculate = QPushButton(self.wall_thickness)
        self.button_wall_calculate.setObjectName(u"button_wall_calculate")

        self.verticalLayout_15.addWidget(self.button_wall_calculate)

        self.groupBox_7 = QGroupBox(self.wall_thickness)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_100 = QLabel(self.groupBox_7)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_10.addWidget(self.label_100, 0, 4, 1, 1)

        self.label_81 = QLabel(self.groupBox_7)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_10.addWidget(self.label_81, 2, 0, 1, 1)

        self.line_edit_OD = QLineEdit(self.groupBox_7)
        self.line_edit_OD.setObjectName(u"line_edit_OD")
        self.line_edit_OD.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(85, 170, 255)\n"
"}")
        self.line_edit_OD.setReadOnly(True)

        self.gridLayout_10.addWidget(self.line_edit_OD, 2, 3, 1, 1)

        self.label_80 = QLabel(self.groupBox_7)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_10.addWidget(self.label_80, 0, 0, 1, 1)

        self.label_91 = QLabel(self.groupBox_7)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_10.addWidget(self.label_91, 2, 1, 1, 1)

        self.label_101 = QLabel(self.groupBox_7)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_10.addWidget(self.label_101, 2, 4, 1, 1)

        self.label_99 = QLabel(self.groupBox_7)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_10.addWidget(self.label_99, 1, 4, 1, 1)

        self.label_90 = QLabel(self.groupBox_7)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_10.addWidget(self.label_90, 0, 1, 1, 1)

        self.label_89 = QLabel(self.groupBox_7)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_10.addWidget(self.label_89, 1, 1, 1, 1)

        self.line_edit_t_m = QLineEdit(self.groupBox_7)
        self.line_edit_t_m.setObjectName(u"line_edit_t_m")
        self.line_edit_t_m.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(85, 170, 255)\n"
"}")
        self.line_edit_t_m.setReadOnly(True)

        self.gridLayout_10.addWidget(self.line_edit_t_m, 0, 3, 1, 1)

        self.label_79 = QLabel(self.groupBox_7)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_10.addWidget(self.label_79, 1, 0, 1, 1)

        self.line_edit_t_n = QLineEdit(self.groupBox_7)
        self.line_edit_t_n.setObjectName(u"line_edit_t_n")
        self.line_edit_t_n.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(85, 170, 255)\n"
"}")
        self.line_edit_t_n.setReadOnly(True)

        self.gridLayout_10.addWidget(self.line_edit_t_n, 1, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.groupBox_7)

        self.button_wall_excel = QPushButton(self.wall_thickness)
        self.button_wall_excel.setObjectName(u"button_wall_excel")

        self.verticalLayout_15.addWidget(self.button_wall_excel)

        self.button_hydraulic.addTab(self.wall_thickness, "")
        self.pump_sizing = QWidget()
        self.pump_sizing.setObjectName(u"pump_sizing")
        self.verticalLayout_16 = QVBoxLayout(self.pump_sizing)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.groupBox_8 = QGroupBox(self.pump_sizing)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_98 = QLabel(self.groupBox_8)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_8.addWidget(self.label_98)

        self.line_edit_service = QLineEdit(self.groupBox_8)
        self.line_edit_service.setObjectName(u"line_edit_service")

        self.horizontalLayout_8.addWidget(self.line_edit_service)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_104 = QLabel(self.groupBox_8)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_9.addWidget(self.label_104)

        self.line_edit_equipment_tag = QLineEdit(self.groupBox_8)
        self.line_edit_equipment_tag.setObjectName(u"line_edit_equipment_tag")

        self.horizontalLayout_9.addWidget(self.line_edit_equipment_tag)


        self.gridLayout_8.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_105 = QLabel(self.groupBox_8)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_10.addWidget(self.label_105)

        self.line_edit_location = QLineEdit(self.groupBox_8)
        self.line_edit_location.setObjectName(u"line_edit_location")

        self.horizontalLayout_10.addWidget(self.line_edit_location)


        self.gridLayout_8.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_106 = QLabel(self.groupBox_8)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_11.addWidget(self.label_106)

        self.line_edit_quantity_required = QLineEdit(self.groupBox_8)
        self.line_edit_quantity_required.setObjectName(u"line_edit_quantity_required")

        self.horizontalLayout_11.addWidget(self.line_edit_quantity_required)


        self.gridLayout_8.addLayout(self.horizontalLayout_11, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.pump_sizing)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_116 = QLabel(self.groupBox_9)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_11.addWidget(self.label_116, 1, 7, 1, 1)

        self.label_115 = QLabel(self.groupBox_9)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_11.addWidget(self.label_115, 1, 5, 1, 1)

        self.label_117 = QLabel(self.groupBox_9)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_11.addWidget(self.label_117, 2, 5, 1, 1)

        self.label_241 = QLabel(self.groupBox_9)
        self.label_241.setObjectName(u"label_241")

        self.gridLayout_11.addWidget(self.label_241, 0, 3, 1, 1)

        self.label_109 = QLabel(self.groupBox_9)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_11.addWidget(self.label_109, 1, 1, 1, 1)

        self.line_edit_1 = QLineEdit(self.groupBox_9)
        self.line_edit_1.setObjectName(u"line_edit_1")
        self.line_edit_1.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_1.setReadOnly(True)

        self.gridLayout_11.addWidget(self.line_edit_1, 1, 2, 1, 1)

        self.label_113 = QLabel(self.groupBox_9)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_11.addWidget(self.label_113, 0, 5, 1, 1)

        self.line_edit_4 = QLineEdit(self.groupBox_9)
        self.line_edit_4.setObjectName(u"line_edit_4")

        self.gridLayout_11.addWidget(self.line_edit_4, 1, 6, 1, 1)

        self.line_edit_5 = QLineEdit(self.groupBox_9)
        self.line_edit_5.setObjectName(u"line_edit_5")
        self.line_edit_5.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_5.setReadOnly(True)

        self.gridLayout_11.addWidget(self.line_edit_5, 2, 6, 1, 1)

        self.label_110 = QLabel(self.groupBox_9)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_11.addWidget(self.label_110, 1, 3, 1, 1)

        self.label_118 = QLabel(self.groupBox_9)
        self.label_118.setObjectName(u"label_118")

        self.gridLayout_11.addWidget(self.label_118, 2, 7, 1, 1)

        self.line_edit_3 = QLineEdit(self.groupBox_9)
        self.line_edit_3.setObjectName(u"line_edit_3")

        self.gridLayout_11.addWidget(self.line_edit_3, 0, 6, 1, 1)

        self.line_edit_mass_flow_rate = QLineEdit(self.groupBox_9)
        self.line_edit_mass_flow_rate.setObjectName(u"line_edit_mass_flow_rate")

        self.gridLayout_11.addWidget(self.line_edit_mass_flow_rate, 0, 2, 1, 1)

        self.label_111 = QLabel(self.groupBox_9)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_11.addWidget(self.label_111, 2, 1, 1, 1)

        self.label_112 = QLabel(self.groupBox_9)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_11.addWidget(self.label_112, 2, 3, 1, 1)

        self.line_edit_2 = QLineEdit(self.groupBox_9)
        self.line_edit_2.setObjectName(u"line_edit_2")

        self.gridLayout_11.addWidget(self.line_edit_2, 2, 2, 1, 1)

        self.label_107 = QLabel(self.groupBox_9)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_11.addWidget(self.label_107, 0, 1, 1, 1)

        self.button_get_capacity = QPushButton(self.groupBox_9)
        self.button_get_capacity.setObjectName(u"button_get_capacity")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_get_capacity.sizePolicy().hasHeightForWidth())
        self.button_get_capacity.setSizePolicy(sizePolicy4)

        self.gridLayout_11.addWidget(self.button_get_capacity, 0, 4, 3, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_11)


        self.verticalLayout_16.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.pump_sizing)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_43 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.line_edit_8 = QLineEdit(self.groupBox_10)
        self.line_edit_8.setObjectName(u"line_edit_8")
        self.line_edit_8.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_8.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_8, 3, 3, 1, 2)

        self.line_edit_10 = QLineEdit(self.groupBox_10)
        self.line_edit_10.setObjectName(u"line_edit_10")

        self.gridLayout_12.addWidget(self.line_edit_10, 5, 3, 1, 2)

        self.label_120 = QLabel(self.groupBox_10)
        self.label_120.setObjectName(u"label_120")
        font = QFont()
        font.setUnderline(True)
        self.label_120.setFont(font)
        self.label_120.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_120, 0, 0, 1, 6)

        self.label_148 = QLabel(self.groupBox_10)
        self.label_148.setObjectName(u"label_148")

        self.gridLayout_12.addWidget(self.label_148, 11, 0, 1, 3)

        self.label_144 = QLabel(self.groupBox_10)
        self.label_144.setObjectName(u"label_144")

        self.gridLayout_12.addWidget(self.label_144, 9, 0, 1, 3)

        self.line_edit_7 = QLineEdit(self.groupBox_10)
        self.line_edit_7.setObjectName(u"line_edit_7")
        self.line_edit_7.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_7.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_7, 2, 3, 1, 2)

        self.label_114 = QLabel(self.groupBox_10)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_12.addWidget(self.label_114, 4, 3, 1, 1)

        self.line_edit_12 = QLineEdit(self.groupBox_10)
        self.line_edit_12.setObjectName(u"line_edit_12")

        self.gridLayout_12.addWidget(self.line_edit_12, 7, 3, 1, 2)

        self.label_146 = QLabel(self.groupBox_10)
        self.label_146.setObjectName(u"label_146")

        self.gridLayout_12.addWidget(self.label_146, 10, 0, 1, 3)

        self.line_edit_14 = QLineEdit(self.groupBox_10)
        self.line_edit_14.setObjectName(u"line_edit_14")
        self.line_edit_14.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_14.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_14, 9, 3, 1, 2)

        self.line_edit_16 = QLineEdit(self.groupBox_10)
        self.line_edit_16.setObjectName(u"line_edit_16")
        self.line_edit_16.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_16.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_16, 11, 3, 1, 2)

        self.line_edit_11 = QLineEdit(self.groupBox_10)
        self.line_edit_11.setObjectName(u"line_edit_11")

        self.gridLayout_12.addWidget(self.line_edit_11, 6, 3, 1, 2)

        self.label_119 = QLabel(self.groupBox_10)
        self.label_119.setObjectName(u"label_119")

        self.gridLayout_12.addWidget(self.label_119, 4, 5, 1, 1)

        self.line_edit_9 = QLineEdit(self.groupBox_10)
        self.line_edit_9.setObjectName(u"line_edit_9")
        self.line_edit_9.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_9.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_9, 4, 4, 1, 1)

        self.label_149 = QLabel(self.groupBox_10)
        self.label_149.setObjectName(u"label_149")

        self.gridLayout_12.addWidget(self.label_149, 11, 5, 1, 1)

        self.label_136 = QLabel(self.groupBox_10)
        self.label_136.setObjectName(u"label_136")

        self.gridLayout_12.addWidget(self.label_136, 5, 0, 1, 3)

        self.label_108 = QLabel(self.groupBox_10)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_12.addWidget(self.label_108, 4, 0, 1, 2)

        self.line_edit_suction_static_head_m = QLineEdit(self.groupBox_10)
        self.line_edit_suction_static_head_m.setObjectName(u"line_edit_suction_static_head_m")

        self.gridLayout_12.addWidget(self.line_edit_suction_static_head_m, 4, 2, 1, 1)

        self.label_141 = QLabel(self.groupBox_10)
        self.label_141.setObjectName(u"label_141")

        self.gridLayout_12.addWidget(self.label_141, 7, 5, 1, 1)

        self.label_132 = QLabel(self.groupBox_10)
        self.label_132.setObjectName(u"label_132")

        self.gridLayout_12.addWidget(self.label_132, 2, 0, 1, 3)

        self.label_135 = QLabel(self.groupBox_10)
        self.label_135.setObjectName(u"label_135")

        self.gridLayout_12.addWidget(self.label_135, 3, 5, 1, 1)

        self.label_139 = QLabel(self.groupBox_10)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_12.addWidget(self.label_139, 6, 5, 1, 1)

        self.line_edit_13 = QLineEdit(self.groupBox_10)
        self.line_edit_13.setObjectName(u"line_edit_13")
        self.line_edit_13.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_13.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_13, 8, 3, 1, 2)

        self.label_142 = QLabel(self.groupBox_10)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_12.addWidget(self.label_142, 8, 0, 1, 3)

        self.label_147 = QLabel(self.groupBox_10)
        self.label_147.setObjectName(u"label_147")

        self.gridLayout_12.addWidget(self.label_147, 10, 5, 1, 1)

        self.label_121 = QLabel(self.groupBox_10)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_12.addWidget(self.label_121, 1, 0, 1, 3)

        self.label_123 = QLabel(self.groupBox_10)
        self.label_123.setObjectName(u"label_123")

        self.gridLayout_12.addWidget(self.label_123, 1, 5, 1, 1)

        self.label_137 = QLabel(self.groupBox_10)
        self.label_137.setObjectName(u"label_137")

        self.gridLayout_12.addWidget(self.label_137, 5, 5, 1, 1)

        self.label_138 = QLabel(self.groupBox_10)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_12.addWidget(self.label_138, 6, 0, 1, 3)

        self.label_140 = QLabel(self.groupBox_10)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_12.addWidget(self.label_140, 7, 0, 1, 3)

        self.label_145 = QLabel(self.groupBox_10)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_12.addWidget(self.label_145, 9, 5, 1, 1)

        self.label_134 = QLabel(self.groupBox_10)
        self.label_134.setObjectName(u"label_134")

        self.gridLayout_12.addWidget(self.label_134, 3, 0, 1, 3)

        self.line_edit_15 = QLineEdit(self.groupBox_10)
        self.line_edit_15.setObjectName(u"line_edit_15")
        self.line_edit_15.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_15.setReadOnly(True)

        self.gridLayout_12.addWidget(self.line_edit_15, 10, 3, 1, 2)

        self.label_143 = QLabel(self.groupBox_10)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_12.addWidget(self.label_143, 8, 5, 1, 1)

        self.line_edit_6 = QLineEdit(self.groupBox_10)
        self.line_edit_6.setObjectName(u"line_edit_6")

        self.gridLayout_12.addWidget(self.line_edit_6, 1, 3, 1, 2)


        self.horizontalLayout_43.addLayout(self.gridLayout_12)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_212 = QLabel(self.groupBox_10)
        self.label_212.setObjectName(u"label_212")

        self.gridLayout_15.addWidget(self.label_212, 1, 0, 1, 3)

        self.line_edit_25 = QLineEdit(self.groupBox_10)
        self.line_edit_25.setObjectName(u"line_edit_25")

        self.gridLayout_15.addWidget(self.line_edit_25, 9, 3, 1, 2)

        self.label_217 = QLabel(self.groupBox_10)
        self.label_217.setObjectName(u"label_217")

        self.gridLayout_15.addWidget(self.label_217, 3, 5, 1, 1)

        self.label_221 = QLabel(self.groupBox_10)
        self.label_221.setObjectName(u"label_221")

        self.gridLayout_15.addWidget(self.label_221, 11, 0, 1, 3)

        self.label_203 = QLabel(self.groupBox_10)
        self.label_203.setObjectName(u"label_203")

        self.gridLayout_15.addWidget(self.label_203, 2, 0, 1, 3)

        self.label_220 = QLabel(self.groupBox_10)
        self.label_220.setObjectName(u"label_220")

        self.gridLayout_15.addWidget(self.label_220, 5, 0, 1, 3)

        self.line_edit_22 = QLineEdit(self.groupBox_10)
        self.line_edit_22.setObjectName(u"line_edit_22")

        self.gridLayout_15.addWidget(self.line_edit_22, 6, 3, 1, 2)

        self.label_206 = QLabel(self.groupBox_10)
        self.label_206.setObjectName(u"label_206")

        self.gridLayout_15.addWidget(self.label_206, 5, 5, 1, 1)

        self.line_edit_21 = QLineEdit(self.groupBox_10)
        self.line_edit_21.setObjectName(u"line_edit_21")

        self.gridLayout_15.addWidget(self.line_edit_21, 5, 3, 1, 2)

        self.label_198 = QLabel(self.groupBox_10)
        self.label_198.setObjectName(u"label_198")

        self.gridLayout_15.addWidget(self.label_198, 9, 5, 1, 1)

        self.line_edit_discharge_static_head_m = QLineEdit(self.groupBox_10)
        self.line_edit_discharge_static_head_m.setObjectName(u"line_edit_discharge_static_head_m")

        self.gridLayout_15.addWidget(self.line_edit_discharge_static_head_m, 4, 2, 1, 1)

        self.line_edit_23 = QLineEdit(self.groupBox_10)
        self.line_edit_23.setObjectName(u"line_edit_23")

        self.gridLayout_15.addWidget(self.line_edit_23, 7, 3, 1, 2)

        self.label_200 = QLabel(self.groupBox_10)
        self.label_200.setObjectName(u"label_200")

        self.gridLayout_15.addWidget(self.label_200, 10, 5, 1, 1)

        self.label_205 = QLabel(self.groupBox_10)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setFont(font)
        self.label_205.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_205, 0, 0, 1, 6)

        self.label_210 = QLabel(self.groupBox_10)
        self.label_210.setObjectName(u"label_210")

        self.gridLayout_15.addWidget(self.label_210, 6, 5, 1, 1)

        self.label_211 = QLabel(self.groupBox_10)
        self.label_211.setObjectName(u"label_211")

        self.gridLayout_15.addWidget(self.label_211, 11, 5, 1, 1)

        self.label_201 = QLabel(self.groupBox_10)
        self.label_201.setObjectName(u"label_201")

        self.gridLayout_15.addWidget(self.label_201, 1, 5, 1, 1)

        self.label_215 = QLabel(self.groupBox_10)
        self.label_215.setObjectName(u"label_215")

        self.gridLayout_15.addWidget(self.label_215, 8, 0, 1, 3)

        self.label_209 = QLabel(self.groupBox_10)
        self.label_209.setObjectName(u"label_209")

        self.gridLayout_15.addWidget(self.label_209, 8, 5, 1, 1)

        self.label_216 = QLabel(self.groupBox_10)
        self.label_216.setObjectName(u"label_216")

        self.gridLayout_15.addWidget(self.label_216, 10, 0, 1, 3)

        self.label_218 = QLabel(self.groupBox_10)
        self.label_218.setObjectName(u"label_218")

        self.gridLayout_15.addWidget(self.label_218, 4, 0, 1, 2)

        self.label_219 = QLabel(self.groupBox_10)
        self.label_219.setObjectName(u"label_219")

        self.gridLayout_15.addWidget(self.label_219, 9, 0, 1, 3)

        self.label_214 = QLabel(self.groupBox_10)
        self.label_214.setObjectName(u"label_214")

        self.gridLayout_15.addWidget(self.label_214, 7, 5, 1, 1)

        self.label_213 = QLabel(self.groupBox_10)
        self.label_213.setObjectName(u"label_213")

        self.gridLayout_15.addWidget(self.label_213, 3, 0, 1, 3)

        self.label_199 = QLabel(self.groupBox_10)
        self.label_199.setObjectName(u"label_199")

        self.gridLayout_15.addWidget(self.label_199, 4, 3, 1, 1)

        self.line_edit_24 = QLineEdit(self.groupBox_10)
        self.line_edit_24.setObjectName(u"line_edit_24")
        self.line_edit_24.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_24.setReadOnly(True)

        self.gridLayout_15.addWidget(self.line_edit_24, 8, 3, 1, 2)

        self.line_edit_20 = QLineEdit(self.groupBox_10)
        self.line_edit_20.setObjectName(u"line_edit_20")
        self.line_edit_20.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_20.setReadOnly(True)

        self.gridLayout_15.addWidget(self.line_edit_20, 4, 4, 1, 1)

        self.line_edit_19 = QLineEdit(self.groupBox_10)
        self.line_edit_19.setObjectName(u"line_edit_19")
        self.line_edit_19.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_19.setReadOnly(True)

        self.gridLayout_15.addWidget(self.line_edit_19, 3, 3, 1, 2)

        self.line_edit_26 = QLineEdit(self.groupBox_10)
        self.line_edit_26.setObjectName(u"line_edit_26")

        self.gridLayout_15.addWidget(self.line_edit_26, 10, 3, 1, 2)

        self.label_208 = QLabel(self.groupBox_10)
        self.label_208.setObjectName(u"label_208")

        self.gridLayout_15.addWidget(self.label_208, 4, 5, 1, 1)

        self.label_202 = QLabel(self.groupBox_10)
        self.label_202.setObjectName(u"label_202")

        self.gridLayout_15.addWidget(self.label_202, 7, 0, 1, 3)

        self.label_204 = QLabel(self.groupBox_10)
        self.label_204.setObjectName(u"label_204")

        self.gridLayout_15.addWidget(self.label_204, 6, 0, 1, 3)

        self.line_edit_27 = QLineEdit(self.groupBox_10)
        self.line_edit_27.setObjectName(u"line_edit_27")
        self.line_edit_27.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_27.setReadOnly(True)

        self.gridLayout_15.addWidget(self.line_edit_27, 11, 3, 1, 2)

        self.line_edit_18 = QLineEdit(self.groupBox_10)
        self.line_edit_18.setObjectName(u"line_edit_18")
        self.line_edit_18.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")
        self.line_edit_18.setReadOnly(True)

        self.gridLayout_15.addWidget(self.line_edit_18, 2, 3, 1, 2)

        self.line_edit_17 = QLineEdit(self.groupBox_10)
        self.line_edit_17.setObjectName(u"line_edit_17")

        self.gridLayout_15.addWidget(self.line_edit_17, 1, 3, 1, 2)


        self.horizontalLayout_43.addLayout(self.gridLayout_15)


        self.verticalLayout_16.addWidget(self.groupBox_10)

        self.button_hydraulics = QPushButton(self.pump_sizing)
        self.button_hydraulics.setObjectName(u"button_hydraulics")

        self.verticalLayout_16.addWidget(self.button_hydraulics)

        self.groupBox_11 = QGroupBox(self.pump_sizing)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_44 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_233 = QLabel(self.groupBox_11)
        self.label_233.setObjectName(u"label_233")

        self.gridLayout_16.addWidget(self.label_233, 2, 3, 1, 1)

        self.label_236 = QLabel(self.groupBox_11)
        self.label_236.setObjectName(u"label_236")

        self.gridLayout_16.addWidget(self.label_236, 1, 3, 1, 1)

        self.label_228 = QLabel(self.groupBox_11)
        self.label_228.setObjectName(u"label_228")

        self.gridLayout_16.addWidget(self.label_228, 5, 0, 1, 1)

        self.label_223 = QLabel(self.groupBox_11)
        self.label_223.setObjectName(u"label_223")

        self.gridLayout_16.addWidget(self.label_223, 2, 0, 1, 1)

        self.label_230 = QLabel(self.groupBox_11)
        self.label_230.setObjectName(u"label_230")

        self.gridLayout_16.addWidget(self.label_230, 4, 2, 1, 1)

        self.label_231 = QLabel(self.groupBox_11)
        self.label_231.setObjectName(u"label_231")

        self.gridLayout_16.addWidget(self.label_231, 5, 2, 1, 1)

        self.line_edit_37 = QLineEdit(self.groupBox_11)
        self.line_edit_37.setObjectName(u"line_edit_37")

        self.gridLayout_16.addWidget(self.line_edit_37, 4, 4, 1, 1)

        self.label_224 = QLabel(self.groupBox_11)
        self.label_224.setObjectName(u"label_224")

        self.gridLayout_16.addWidget(self.label_224, 2, 2, 1, 1)

        self.label_133 = QLabel(self.groupBox_11)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_133, 0, 0, 1, 3)

        self.line_edit_32 = QLineEdit(self.groupBox_11)
        self.line_edit_32.setObjectName(u"line_edit_32")

        self.gridLayout_16.addWidget(self.line_edit_32, 5, 1, 1, 1)

        self.line_edit_28 = QLineEdit(self.groupBox_11)
        self.line_edit_28.setObjectName(u"line_edit_28")
        self.line_edit_28.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_16.addWidget(self.line_edit_28, 1, 1, 1, 1)

        self.line_edit_36 = QLineEdit(self.groupBox_11)
        self.line_edit_36.setObjectName(u"line_edit_36")

        self.gridLayout_16.addWidget(self.line_edit_36, 3, 4, 1, 1)

        self.label_227 = QLabel(self.groupBox_11)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_16.addWidget(self.label_227, 4, 0, 1, 1)

        self.label_229 = QLabel(self.groupBox_11)
        self.label_229.setObjectName(u"label_229")

        self.gridLayout_16.addWidget(self.label_229, 6, 0, 1, 1)

        self.line_edit_35 = QLineEdit(self.groupBox_11)
        self.line_edit_35.setObjectName(u"line_edit_35")

        self.gridLayout_16.addWidget(self.line_edit_35, 2, 4, 1, 1)

        self.label_207 = QLabel(self.groupBox_11)
        self.label_207.setObjectName(u"label_207")

        self.gridLayout_16.addWidget(self.label_207, 1, 0, 1, 1)

        self.line_edit_34 = QLineEdit(self.groupBox_11)
        self.line_edit_34.setObjectName(u"line_edit_34")

        self.gridLayout_16.addWidget(self.line_edit_34, 1, 4, 1, 1)

        self.line_edit_33 = QLineEdit(self.groupBox_11)
        self.line_edit_33.setObjectName(u"line_edit_33")
        self.line_edit_33.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_16.addWidget(self.line_edit_33, 6, 1, 1, 1)

        self.label_225 = QLabel(self.groupBox_11)
        self.label_225.setObjectName(u"label_225")

        self.gridLayout_16.addWidget(self.label_225, 3, 0, 1, 1)

        self.label_232 = QLabel(self.groupBox_11)
        self.label_232.setObjectName(u"label_232")

        self.gridLayout_16.addWidget(self.label_232, 6, 2, 1, 1)

        self.label_222 = QLabel(self.groupBox_11)
        self.label_222.setObjectName(u"label_222")

        self.gridLayout_16.addWidget(self.label_222, 1, 2, 1, 1)

        self.line_edit_29 = QLineEdit(self.groupBox_11)
        self.line_edit_29.setObjectName(u"line_edit_29")
        self.line_edit_29.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_16.addWidget(self.line_edit_29, 2, 1, 1, 1)

        self.line_edit_30 = QLineEdit(self.groupBox_11)
        self.line_edit_30.setObjectName(u"line_edit_30")
        self.line_edit_30.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_16.addWidget(self.line_edit_30, 3, 1, 1, 1)

        self.line_edit_31 = QLineEdit(self.groupBox_11)
        self.line_edit_31.setObjectName(u"line_edit_31")
        self.line_edit_31.setStyleSheet(u"QLineEdit {\n"
"	background: rgb(223, 223, 223)\n"
"}")

        self.gridLayout_16.addWidget(self.line_edit_31, 4, 1, 1, 1)

        self.label_237 = QLabel(self.groupBox_11)
        self.label_237.setObjectName(u"label_237")

        self.gridLayout_16.addWidget(self.label_237, 3, 3, 1, 1)

        self.label_226 = QLabel(self.groupBox_11)
        self.label_226.setObjectName(u"label_226")

        self.gridLayout_16.addWidget(self.label_226, 3, 2, 1, 1)

        self.label_240 = QLabel(self.groupBox_11)
        self.label_240.setObjectName(u"label_240")

        self.gridLayout_16.addWidget(self.label_240, 4, 3, 1, 1)

        self.label_238 = QLabel(self.groupBox_11)
        self.label_238.setObjectName(u"label_238")

        self.gridLayout_16.addWidget(self.label_238, 1, 5, 1, 1)

        self.label_234 = QLabel(self.groupBox_11)
        self.label_234.setObjectName(u"label_234")

        self.gridLayout_16.addWidget(self.label_234, 2, 5, 1, 1)

        self.label_239 = QLabel(self.groupBox_11)
        self.label_239.setObjectName(u"label_239")

        self.gridLayout_16.addWidget(self.label_239, 3, 5, 1, 1)

        self.label_243 = QLabel(self.groupBox_11)
        self.label_243.setObjectName(u"label_243")

        self.gridLayout_16.addWidget(self.label_243, 4, 5, 1, 1)

        self.label_235 = QLabel(self.groupBox_11)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setFont(font)
        self.label_235.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_235, 0, 3, 1, 3)


        self.horizontalLayout_44.addLayout(self.gridLayout_16)


        self.verticalLayout_16.addWidget(self.groupBox_11)

        self.button_design_conditions = QPushButton(self.pump_sizing)
        self.button_design_conditions.setObjectName(u"button_design_conditions")

        self.verticalLayout_16.addWidget(self.button_design_conditions)

        self.button_hydraulic.addTab(self.pump_sizing, "")

        self.verticalLayout_10.addWidget(self.button_hydraulic)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1092, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.button_hydraulic.setCurrentIndex(0)
        self.tab_fluid_properties.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Pipe Characteristics", None))
        self.d.setText(QCoreApplication.translate("MainWindow", u"729", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Inside Diameter (D):", None))
        self.nominal_size.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nominal size", None))
        self.absolute_roughness.setText(QCoreApplication.translate("MainWindow", u"0.00004572", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Line Description", None))
        self.material_and_schedule.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Material and Schedule", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Absolute Roughness (\u03b5)", None))
        self.line_description.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Inside Diameter (d):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source Parameters", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"kg / hr", None))
        self.line_edit_source_h.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.line_edit_source_p.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.line_edit_source_q.setText(QCoreApplication.translate("MainWindow", u"1574000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"bar a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"kJ / kg", None))
        self.line_edit_source_t.setText(QCoreApplication.translate("MainWindow", u"602", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Destination Parameters", None))
        self.line_edit_destination_t.setText(QCoreApplication.translate("MainWindow", u"600", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"bar a", None))
        self.line_edit_destination_h.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.line_edit_destination_q.setText(QCoreApplication.translate("MainWindow", u"1574000", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"kJ / kg", None))
        self.line_edit_destination_p.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"kg / hr", None))
        self.tab_fluid_properties.setTabText(self.tab_fluid_properties.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Source and Destination Mode", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Average Pressure", None))
        self.line_edit_p_avg.setText(QCoreApplication.translate("MainWindow", u"54.93", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"bar a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Average Temerature", None))
        self.line_edit_t_avg.setText(QCoreApplication.translate("MainWindow", u"601", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Flow Rate", None))
        self.line_edit_q.setText(QCoreApplication.translate("MainWindow", u"1574000", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"kg / hr", None))
        self.tab_fluid_properties.setTabText(self.tab_fluid_properties.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Average Mode", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Fluid Properties", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Specific Volume (V)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"m^3 / kg", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Absolute Viscosity (\u03bc)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"cP", None))
        self.label_36.setText("")
        self.label_35.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"m/sec = ", None))
        self.label_34.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Turbulent Flow", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Fluid Velocity (Vel)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Friction Factor (f)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"m/min", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Reynolds Number (Re)", None))
        self.label_33.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Laminar Flow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Resistance Coefficients of Fittings, Valves, Etc.", None))
        ___qtablewidgetitem = self.table_fittings.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Fittings", None));
        ___qtablewidgetitem1 = self.table_fittings.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantity (n)", None));
        ___qtablewidgetitem2 = self.table_fittings.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"L/D or K/f", None));
        ___qtablewidgetitem3 = self.table_fittings.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.table_fittings.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.table_fittings.isSortingEnabled()
        self.table_fittings.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.table_fittings.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"elbow long 90", None));
        ___qtablewidgetitem6 = self.table_fittings.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem7 = self.table_fittings.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem8 = self.table_fittings.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"butterfly valve", None));
        ___qtablewidgetitem9 = self.table_fittings.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.table_fittings.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"25", None));
        self.table_fittings.setSortingEnabled(__sortingEnabled)

        self.button_add_row.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_remove_row.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_reset_rows.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Sum of nL/D for all fittings: ", None))
        self.button_pipe_calculate.setText(QCoreApplication.translate("MainWindow", u"Press to Calculate", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Pressure Drops", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Friction Head Loss (h_L):", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.line_edit_static_head_m.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<b>Total Pressure Drop: </b>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.line_edit_l_p.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_49.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<b>bar</b>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Equivalent Length of Fittings (L_F): ", None))
        self.label_51.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Total Equivalent Pipe Length (L_TEL)", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Miscellaneous Equipment Pressure Drops:", None))
        self.label_52.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Straight Pipe Length (L_P):", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Friction Pressure Drop (\u0394P)", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Static Head", None))
        self.label_47.setText("")
        self.label_50.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"m =", None))
        self.line_edit_misc_m.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"m =", None))
        self.button_pipe_excel.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.button_hydraulic.setTabText(self.button_hydraulic.indexOf(self.pressure_drop), QCoreApplication.translate("MainWindow", u"Piping Pressure Drop", None))
        self.button_wall_autofill.setText(QCoreApplication.translate("MainWindow", u"Suggest Values from Pipe Sizing", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Pipe System Characteristics", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Design Temperature (T)", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"BREI Pipe Classification", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Design Pressure (P)", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"ASTM Specification", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Fluid", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Pipeline Identification", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Applicable Pipe Sizes", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"C =", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"bar (g)", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Formula for Minimum Wall Thickness", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"BEND = ", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"SE = ", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.line_edit_BEND.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_71.setText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.line_edit_MFG.setText(QCoreApplication.translate("MainWindow", u"0.125", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Internal Diameter (mm)", None))
        self.line_edit_A.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Multipler for Additional Thickness for Bending Specified in B31.1 Table 102.4.5", None))
        self.label_70.setText("")
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Internal Design Pressure", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"d = ", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"P = ", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"ksi =", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Manufacturer's Wall Thickness Tolerance", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Coefficient with Value Specified in B31.1 Table 104.1.2A", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"MFG = ", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Y = ", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Additional Thickness Allowed for Corrosion, Erosion, and/or Mechanical Strength", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"A = ", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Maximum Allowable Stress specified in B31.1 Appendix A", None))
        self.button_wall_calculate.setText(QCoreApplication.translate("MainWindow", u"Press to Calculate", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Wall Thickness Results", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"OD = ", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"T_m = ", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Outer Diameter (mm)", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Minimum Wall Thickness (mm)", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Nominal Wall Thickness Required (mm)", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"T_n = ", None))
        self.button_wall_excel.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.button_hydraulic.setTabText(self.button_hydraulic.indexOf(self.wall_thickness), QCoreApplication.translate("MainWindow", u"Wall Thickness", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Pump Information", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Service: ", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Equipment Tag(s):", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Location: ", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Quantity Required: ", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Fluid Properties", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"(4) Pumping Temperature", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"(5) Vapor Pressure @ Temperature", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"kg / hr", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"(1) Pump Capacity", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"(3) Fluid Pumped", None))
        self.line_edit_4.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"m^3 / hr", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"bar (a)", None))
        self.line_edit_3.setText(QCoreApplication.translate("MainWindow", u"Condensate Water", None))
        self.line_edit_mass_flow_rate.setText(QCoreApplication.translate("MainWindow", u"1411511", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"(2) Margin for Capacity", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.line_edit_2.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Mass Flow Rate", None))
        self.button_get_capacity.setText(QCoreApplication.translate("MainWindow", u"Get Capacity", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Hydraulic Summary", None))
        self.line_edit_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"SUCTION SIDE:", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"(16) NPSHA in meter", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"(14) Total Suction Pressure", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"m = ", None))
        self.line_edit_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"(15) NPSHA in bar", None))
        self.line_edit_11.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"(10) Equipment Loss", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"(9) Static Head", None))
        self.line_edit_suction_static_head_m.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"(7) Specific Gravity @ Temperature", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"m / bar", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"(13) Total Piping Loss with Margin", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"(6) Terminal Pressure", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"bar (a)", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"(11) Piping Friction Loss", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"(12) Margin for Piping Loss", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"bar (a)", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"(8) Meter of Fluid Head", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.line_edit_6.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"(17) Terminal Pressure", None))
        self.line_edit_25.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"m / bar", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"(27) Total Discharge Pressure", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"(18) Specific Gravity @ Temperature", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"(21) Equipment Loss", None))
        self.line_edit_22.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.line_edit_21.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.line_edit_discharge_static_head_m.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.line_edit_23.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"DISCHARGE SIDE:", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"bar (a)", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"bar (a)", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"(24) Total Piping Loss with Margin", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"(26) Pump Wear", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"(20) Static Head", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"(25) Control Valve Loss (Confirm with I&C)", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"(19) Meter of Fluid Head", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"m =", None))
        self.line_edit_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"(23) Margin for PIping Loss", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"(22) Piping Friction Loss", None))
        self.line_edit_17.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.button_hydraulics.setText(QCoreApplication.translate("MainWindow", u"Calculate Hydraulics", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Design Conditions", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"(35) Suction Design Temperature", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"(34) Suction Design Pressure", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"(32) User Specified Pump Efficiency", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"(29) Total Head (TH or TDH)", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"PUMP:", None))
        self.line_edit_32.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"(31) Design NPSHA", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"(33) Pump Power", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"(28) Total Differential Pressure", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"(30) Design Capacity", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"kW", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"bar", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"(36) User-Specified Shut-off Head", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"m^3 / hr", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"(37) Discharge Design Pressure", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"bar (g)", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"bar (g)", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"PIPING:", None))
        self.button_design_conditions.setText(QCoreApplication.translate("MainWindow", u"Get Design Conditions", None))
        self.button_hydraulic.setTabText(self.button_hydraulic.indexOf(self.pump_sizing), QCoreApplication.translate("MainWindow", u"Pump Sizing", None))
    # retranslateUi

