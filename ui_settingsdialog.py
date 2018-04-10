# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settingsdialog.ui'
#
# Created: Wed Feb  5 18:09:18 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(494, 101)
        
        self.verticalLayout = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        self.splineToleranceLabel = QtGui.QLabel(SettingsDialog)
        self.splineToleranceLabel.setObjectName(_fromUtf8("splineToleranceLabel"))
        self.horizontalLayout.addWidget(self.splineToleranceLabel)
        self.splineToleranceSpinBox = QtGui.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splineToleranceSpinBox.sizePolicy().hasHeightForWidth())
        self.splineToleranceSpinBox.setSizePolicy(sizePolicy)
        self.splineToleranceSpinBox.setDecimals(6)
        self.splineToleranceSpinBox.setMinimum(1e-06)
        self.splineToleranceSpinBox.setMaximum(10000.0)
        self.splineToleranceSpinBox.setProperty("value", 1.0)
        self.splineToleranceSpinBox.setObjectName(_fromUtf8("splineToleranceSpinBox"))
        self.horizontalLayout.addWidget(self.splineToleranceSpinBox)
        
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        
        self.splineTightnessLabel = QtGui.QLabel(SettingsDialog)
        self.splineTightnessLabel.setObjectName(_fromUtf8("splineTightnessLabel"))
        self.horizontalLayout_5.addWidget(self.splineTightnessLabel)
        self.splineTightnessSpinBox = QtGui.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splineTightnessSpinBox.sizePolicy().hasHeightForWidth())
        self.splineTightnessSpinBox.setSizePolicy(sizePolicy)
        self.splineTightnessSpinBox.setMinimum(1.00)
        self.splineTightnessSpinBox.setMaximum(10.0)
        self.splineTightnessSpinBox.setSingleStep(1.0)
        self.splineTightnessSpinBox.setProperty("value", 0.1)
        self.splineTightnessSpinBox.setObjectName(_fromUtf8("splineTightnessSpinBox"))
        self.horizontalLayout_5.addWidget(self.splineTightnessSpinBox)
        
        
  
  
        self.splineEspacamentoLabel = QtGui.QLabel(SettingsDialog)
        self.splineEspacamentoLabel.setObjectName(_fromUtf8("splineEspacamentoLabel"))
        self.horizontalLayout.addWidget(self.splineEspacamentoLabel)
        self.splineEspacamentoSpinBox = QtGui.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splineEspacamentoSpinBox.sizePolicy().hasHeightForWidth())
        self.splineEspacamentoSpinBox.setSizePolicy(sizePolicy)
        self.splineEspacamentoSpinBox.setMinimum(1e-06)
        self.splineEspacamentoSpinBox.setMaximum(100.0)
        self.splineEspacamentoSpinBox.setSingleStep(0.1)
        self.splineEspacamentoSpinBox.setProperty("value", 1.0)
        self.splineEspacamentoSpinBox.setObjectName(_fromUtf8("splineEspacamentoSpinBox"))
        self.horizontalLayout.addWidget(self.splineEspacamentoSpinBox)
        
        
        self.splineQpontosLabel = QtGui.QLabel(SettingsDialog)
        self.splineQpontosLabel.setObjectName(_fromUtf8("splineQpontosLabel"))
        self.horizontalLayout.addWidget(self.splineQpontosLabel)
        self.splineQpontosSpinBox = QtGui.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splineQpontosSpinBox.sizePolicy().hasHeightForWidth())
        self.splineQpontosSpinBox.setSizePolicy(sizePolicy)
        self.splineQpontosSpinBox.setMinimum(1e-06)
        self.splineQpontosSpinBox.setMaximum(100.0)
        self.splineQpontosSpinBox.setProperty("value", 1.0)
        self.splineQpontosSpinBox.setObjectName(_fromUtf8("splineQpontosSpinBox"))
        self.horizontalLayout.addWidget(self.splineQpontosSpinBox)
        
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Digitize Spline Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.splineToleranceLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Tolerance", None, QtGui.QApplication.UnicodeUTF8))
        self.splineToleranceSpinBox.setToolTip(QtGui.QApplication.translate("SettingsDialog", "Polyline interpolation tolerance in map units.", None, QtGui.QApplication.UnicodeUTF8))
        self.splineTightnessLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Tightness", None, QtGui.QApplication.UnicodeUTF8))
        self.splineEspacamentoLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Espacamento", None, QtGui.QApplication.UnicodeUTF8))
        self.splineQpontosLabel.setText(QtGui.QApplication.translate("SettingsDialog", "Qpontos", None, QtGui.QApplication.UnicodeUTF8))
        self.splineQpontosSpinBox.setToolTip(QtGui.QApplication.translate("SettingsDialog", "Pontos acima e abaixo do ponto central (que fica no segmento que une 2 pontos marcados pelo operador)", None, QtGui.QApplication.UnicodeUTF8))
