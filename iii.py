import sys
from PyQt4 import QtGui, QtCore
class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle( "hello" )
        self.resize( 500, 500 )
         
        gridlayout = QtGui.QGridLayout()
         
        str = "hello"  #这里中文乱码，纠结
        label = QtGui.QLabel( str )
        label.setAlignment( QtCore.Qt.AlignCenter )
         
        textFile = QtGui.QLineEdit()
        gridlayout.addWidget( label, 0, 0 )
        gridlayout.addWidget( textFile )
         
        passwordFile = QtGui.QLineEdit()
        passwordFile.setEchoMode( QtGui.QLineEdit.Password )
        gridlayout.addWidget( passwordFile )
         
        textArea = QtGui.QTextEdit()
        textArea.setText( "asdasda" )
        gridlayout.addWidget( textArea )
         
         
        self.setLayout( gridlayout )
app = QtGui.QApplication( sys.argv )
window = Window()
window.show()
app.exec_()