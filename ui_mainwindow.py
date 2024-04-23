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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(964, 746)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget_1 = QTabWidget(self.centralwidget)
        self.tabWidget_1.setObjectName(u"tabWidget_1")
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -713, 906, 1350))
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
        self.label_36.setPixmap(QPixmap(u"images/f_laminar.png"))

        self.gridLayout_7.addWidget(self.label_36, 4, 2, 1, 1)

        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setPixmap(QPixmap(u"images/f_turbulent.png"))

        self.gridLayout_7.addWidget(self.label_35, 3, 2, 1, 1)

        self.label_37 = QLabel(self.groupBox_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_7.addWidget(self.label_37, 0, 4, 1, 1)

        self.label_34 = QLabel(self.groupBox_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setPixmap(QPixmap(u"images/Re.png"))

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
        self.label_33.setPixmap(QPixmap(u"images/Vel.png"))

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
        self.label_49.setPixmap(QPixmap(u"images/L_TEL.png"))

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
        self.label_51.setPixmap(QPixmap(u"images/delta_P.png"))

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
        self.label_52.setPixmap(QPixmap(u"images/bar.png"))

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
        self.label_47.setPixmap(QPixmap(u"images/L_f.png"))

        self.gridLayout_4.addWidget(self.label_47, 0, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setPixmap(QPixmap(u"images/h_L.png"))

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

        self.tabWidget_1.addTab(self.pressure_drop, "")
        self.wall_thickness = QWidget()
        self.wall_thickness.setObjectName(u"wall_thickness")
        self.tabWidget_1.addTab(self.wall_thickness, "")
        self.pump_sizing = QWidget()
        self.pump_sizing.setObjectName(u"pump_sizing")
        self.tabWidget_1.addTab(self.pump_sizing, "")

        self.verticalLayout_10.addWidget(self.tabWidget_1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 964, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_1.setCurrentIndex(0)
        self.tab_fluid_properties.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Pipe Characteristics", None))
        self.d.setText(QCoreApplication.translate("MainWindow", u"729", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Inside Diameter (D):", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nominal size", None))
        self.absolute_roughness.setText(QCoreApplication.translate("MainWindow", u"0.00004572", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Line Description", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Material and Schedule", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Absolute Roughness (\u03b5)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Inside Diameter (d):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source Parameters", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"kg / hr", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"bar a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"kJ / kg", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Destination Parameters", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"bar a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"kJ / kg", None))
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
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.pressure_drop), QCoreApplication.translate("MainWindow", u"Piping Pressure Drop", None))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.wall_thickness), QCoreApplication.translate("MainWindow", u"Wall Thickness", None))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.pump_sizing), QCoreApplication.translate("MainWindow", u"Pump Sizing", None))
    # retranslateUi

