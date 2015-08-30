#!/usr/bin/env python

from PySide import QtCore,QtGui
 
 
class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        '''
        LLamada a los constructores de las 
        clases MainWindow y QtGui.QMainWindow
        '''
        super(MainWindow, self).__init__()
 
          
        self.createControls()

        self.createActions()
        self.createMenus()
        self.createToolBar()
        
        #Llamadas a las funciones
        message = "Ready"
        self.statusBar().showMessage(message)
        self.setWindowTitle("App Basic")
        self.setMinimumSize(160,160)
        self.resize(440,280)
        self.setWindowIcon(QtGui.QIcon('app.png'))
        self.center()
        
    def euros_pesetas(self):
        '''
        Metodo para transformar euros a pesetas
        '''
        self.edit2.setText(str(int(self.edit1.text()) * 166.33))
        
    def pesetas_euros(self):
        '''
        Metodo para transformar pesetas a euros
        '''
        self.edit2.setText(str(int(self.edit1.text()) / 166.33))
        
    def euros_libras(self):
        '''
        Metodo para transformar euros a libras
        '''
        self.edit2.setText(str(int(self.edit1.text()) * 0.83))
        
    def libras_euros(self):
        '''
        Metodo para transformar libras a euros 
        '''
        self.edit2.setText(str(int(self.edit1.text()) / 0.83))
        
    def euros_dolares(self):
        '''
        Metodo para transformar euros a dolares
        '''
        self.edit2.setText(str(int(self.edit1.text()) * 1.37))
        
    def dolares_euros(self):
        '''
        Metodo para transformar dolares a euros
        '''
        self.edit2.setText(str(int(self.edit1.text()) / 1.37))
    
    def center(self): 
        '''
        Metodo para posicionar la ventana en el centro
        '''
        qr=self.frameGeometry()
        cp=QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
    def newFile(self):
        '''
        Metodo crea nueva ventana
        '''
        pass
        
    def about(self):
        '''
        Metodo crea una ventana de ayuda
        '''
        QtGui.QMessageBox.about(self, "About Menu",
                "The <b>converter</b> example shows how to create menu-bar menus "
                "and context menus.")
    
    def createControls(self):
        '''
        Funcion para crear los controles de conversion monetario

        @param self: Objeto que describe las caracteristicas de la ventana
        @type self: Tipo de la ventana
        @return:  No devuelve nada
        '''
        widget = QtGui.QWidget()
        grid = QtGui.QGridLayout()
        grid.setSpacing(4)

        eur_pes=QtGui.QPushButton('Euros to pesetas')
        grid.addWidget(eur_pes,0,0)
        eur_pes.clicked.connect(self.euros_pesetas)

        pes_eur=QtGui.QPushButton('Pesetas to euros')
        grid.addWidget(pes_eur,1,0)
        pes_eur.clicked.connect(self.pesetas_euros)
        
        eur_lib=QtGui.QPushButton('Euros to pounds')
        grid.addWidget(eur_lib,2,0)
        eur_lib.clicked.connect(self.euros_libras)
  
        lib_eur=QtGui.QPushButton('Pounds to euros')
        grid.addWidget(lib_eur,3,0)
        eur_lib.clicked.connect(self.libras_euros)
        
        eur_dol=QtGui.QPushButton('Euros to dollars')
        grid.addWidget(eur_dol,4,0)
        eur_dol.clicked.connect(self.euros_dolares)

        dol_eur=QtGui.QPushButton('Dollars a euros')
        grid.addWidget(dol_eur,5,0)
        dol_eur.clicked.connect(self.dolares_euros)
        
        title1 = QtGui.QLabel('Amount')
        grid.addWidget(title1,1,2)

        self.edit1 = QtGui.QLineEdit()
        grid.addWidget(self.edit1,2,2)
        
        title2 = QtGui.QLabel('Result')
        grid.addWidget(title2,3,2)

        self.edit2 = QtGui.QLineEdit()
        grid.addWidget(self.edit2,4,2)
        
        widget.setLayout(grid)
        
        self.setCentralWidget(widget)
        
    def createActions(self):
        '''
        Funcion para crear las acciones del menu de opciones y
        barra de herramientas

        @param self: Objeto que describe las caracteristicas de la ventana
        @type self: Tipo de la ventana
        @return: No devuelve nada
        '''

        self.newAct = QtGui.QAction("&New", self,
                shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new file", triggered=self.newFile)
        self.newAct.setIcon(QtGui.QIcon('new-file-md.png') )
                
        self.exitAct = QtGui.QAction("&Exit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)    
        self.exitAct.setIcon(QtGui.QIcon('exit.png') )
                
        self.cutAct = QtGui.QAction("&Cut", self, shortcut=QtGui.QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard", triggered=self.edit1.cut)
        self.cutAct.setIcon(QtGui.QIcon('CutButtonSmall.png') )

        self.copyAct = QtGui.QAction("&Copy", self, shortcut=QtGui.QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard", triggered=self.edit1.copy)
        self.copyAct.setIcon(QtGui.QIcon('copy.jpg') )

        self.pasteAct = QtGui.QAction("&Paste", self, shortcut=QtGui.QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection", triggered=self.edit1.paste)
        self.pasteAct.setIcon(QtGui.QIcon('paste.png') )

        self.aboutAct = QtGui.QAction("&About", self,
                statusTip="Show the application's About box", triggered=self.about)
        self.aboutAct.setIcon(QtGui.QIcon('help.svg') )

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                statusTip="Show the Qt library's About box", triggered=QtGui.qApp.aboutQt)
        self.aboutQtAct.setIcon(QtGui.QIcon('qt-logo.jpg') )
        

    def createToolBar(self):
        '''
        Funcion para crear una barra de herramientas con sus opciones

        @param self: Objeto que describe las caracteristicas de la ventana
        @type self: Tipo de la ventana
        @return:  No devuelve nada
        '''
        self.toolbar = self.addToolBar('File')
        self.toolbar.addAction(self.newAct)
        self.toolbar.addAction(self.exitAct)
        
        self.toolbar = self.addToolBar('Edit')
        self.toolbar.addAction(self.cutAct)
        self.toolbar.addAction(self.copyAct)
        self.toolbar.addAction(self.pasteAct)
       
        self.toolbar = self.addToolBar('Help')
        self.toolbar.addAction(self.aboutAct)
        self.toolbar.addAction(self.aboutQtAct)
    
 
    def createMenus(self):
        '''
        Funcion para crear el menu de opciones

        @param self: Objeto que describe las caracteristicas de la ventana
        @type self: Tipo de la ventana
        @return: No devuelve nada
        '''
    
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.exitAct)
        
        
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)
        
    def closeEvent(self, event):
        '''
        Funcion que muestra una ventana emergente para cerrar
        la aplicacion

        @param self: Objeto que describe las caracteristicas de la ventana
        @type self: Tipo de la ventana
        @return: no devuelve nada
        '''
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
    
    
  
 
if __name__ == '__main__':
 
    import sys
 
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
