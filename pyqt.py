#coding=utf-8
#对话框
import sys
from PyQt4 import QtGui, QtCore
class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle( "hello" )
        self.resize( 500, 500 )
         
        gridlayout = QtGui.QGridLayout()
         
        self.AboutButton = QtGui.QPushButton( "About" )
        gridlayout.addWidget( self.AboutButton, 0, 0 )
        self.AboutQtButton = QtGui.QPushButton( "AboutQt" )
        gridlayout.addWidget( self.AboutQtButton, 0, 1 )
        self.CriticalButton = QtGui.QPushButton( "CriticalButton" )
        gridlayout.addWidget( self.CriticalButton, 1, 0 )
        self.InfoButton = QtGui.QPushButton( "Info" )
        gridlayout.addWidget( self.InfoButton, 1, 1 )
        self.QuestionButton = QtGui.QPushButton( "Question" )
        gridlayout.addWidget( self.QuestionButton, 2, 0 )
        self.WarningButton = QtGui.QPushButton( "Warning" )
        gridlayout.addWidget( self.WarningButton, 2, 1 )
         
        spacer = QtGui.QSpacerItem( 200, 80 )
        gridlayout.addItem( spacer, 3, 1, 1, 5 )
        self.setLayout( gridlayout )
         
        self.connect( self.AboutButton, QtCore.SIGNAL( 'clicked()' ), self.OnAboutButton )
        self.connect( self.AboutQtButton, QtCore.SIGNAL( 'clicked()' ), self.OnAboutQtButton )
        self.connect( self.CriticalButton, QtCore.SIGNAL( 'clicked()' ), self.OnCriticalButton )
        self.connect( self.InfoButton, QtCore.SIGNAL( 'clicked()' ), self.OnInfoButton )
        self.connect( self.QuestionButton, QtCore.SIGNAL( 'clicked()' ), self.OnQuestionButton )
        self.connect( self.WarningButton, QtCore.SIGNAL( 'clicked()' ), self.OnWarningButton )
         
    def OnAboutButton( self ):
        QtGui.QMessageBox.about( self, 'PyQt', "About" )
         
    def OnAboutQtButton( self ):
        QtGui.QMessageBox.aboutQt( self, "PyQt" )
         
    def OnCriticalButton( self ):
        r = QtGui.QMessageBox.critical( self, "PyQT", "CriticalButton", QtGui.QMessageBox.Abort,
                                   QtGui.QMessageBox.Retry, QtGui.QMessageBox.Ignore )
        if r == QtGui.QMessageBox.Abort:
            self.setWindowTitle( "Abort" )
        elif r == QtGui.QMessageBox.Retry:
            self.setWindowTitle( "Retry" )
        elif r == QtGui.QMessageBox.Ignore:
            self.setWindowTitle( "Ignore" )
        else:
            pass
         
    def OnInfoButton( self ):
        QtGui.QMessageBox.information( self, "Pyqt", "information" )
         
    def OnQuestionButton( self ):
        r = QtGui.QMessageBox.question( self, "PyQt", "Question", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel )
         
    def OnWarningButton( self ):
        r = QtGui.QMessageBox.warning( self, "PyQT", "warning", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
     
         
app = QtGui.QApplication( sys.argv )
win = Window()
win.show()
app.exec_()