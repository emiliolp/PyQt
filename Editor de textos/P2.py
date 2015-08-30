#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Jan 18 11:29:53 2014
@author: Emilio López Piña
"""

import os
import sys
from PySide import QtCore
from PySide import QtGui
        

class EditorWindow(QtGui.QDialog):
    
    def __init__(self,parent=None):
        """
        LLamada a los constructores de las 
        clases MainWindow y QtGui.QMainWindow
        """
        super(EditorWindow, self).__init__(parent)
        
        self.controles()                                #Llama a controles
        
    def controles(self):
        """
        Función para crear los controles del editor de textos

        @type  self: EditorWindow
        @param self: Instancia de la clase EditorWindow
        @rtype:   Ninguno
        @return:  No devuelve nada
        """
        
        TituloCarpeta=QtGui.QLabel("Carpeta:")          #Crea etiqueta
        self.TituloEdit=QtGui.QLineEdit()               #Linea de texto
        CarpetaBoton=QtGui.QPushButton("Carpeta")       #Boton
        self.ArchivosList=QtGui.QListWidget()           #Lista de elementos
        self.ArchivoDetalle=QtGui.QTextEdit()           #Caja de texto
        AbrirBoton=QtGui.QPushButton("Abrir")           #Botones
        SalvarBoton=QtGui.QPushButton("Salvar")
        SalvarAsBoton=QtGui.QPushButton("Salvar como")
        CerrarBoton=QtGui.QPushButton("Cerrar")
        SalirBoton=QtGui.QPushButton("Salir")
        
        grid=QtGui.QGridLayout()                        #Crea rejilla
        grid.setSpacing(5)                              #Distancia elementos
        
        grid.addWidget(TituloCarpeta,0,0)               #sitiacion elementos
        grid.addWidget(self.TituloEdit,0,1,1,12)
        grid.addWidget(CarpetaBoton,0,13)
        grid.addWidget(self.ArchivosList,1,0,10,3)
        grid.addWidget(self.ArchivoDetalle,1,4,10,9)
        grid.addWidget(AbrirBoton,1,13)
        grid.addWidget(SalvarBoton,2,13)
        grid.addWidget(SalvarAsBoton,3,13)
        grid.addWidget(CerrarBoton,4,13)
        grid.addWidget(SalirBoton,5,13)
        
        CarpetaBoton.clicked.connect(self.list)         #llama a list    
        AbrirBoton.clicked.connect(self.openFile)       #llama a openFile 
        SalvarBoton.clicked.connect(self.saveFile)      #llama a saveFile
        SalvarAsBoton.clicked.connect(self.saveAsFile)  #llama a saveAsFile
        CerrarBoton.clicked.connect(self.cerrar)        #llama a cerrar
        SalirBoton.clicked.connect(self.close)          #llama a close
        
        
        self.setLayout(grid)                            #Define la cuadricula recibiendo a grid
        self.setWindowTitle('Editor de textos')         #Nombre ventana  
        self.show ()
        
    def list(self):
        """
        Lista los archivos en una determinada ventana encontrados en una ruta previamente
        seleccionada

        @type  self: EditorWindow
        @param self: Instancia de la clase EditorWindow
        @rtype:   Ninguno
        @return:  No devuelve nada
        """
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Buscar Lista Archivos",
                QtCore.QDir.currentPath())
        
        self.TituloEdit.setText(directory)
        files = os.listdir(directory)
        self.ArchivosList.clear()
        self.ArchivosList.addItems(files)
        self.ArchivosList.setCurrentRow(0)
        
    def openFile(self):
        """
        Gestiona la apertura de un archivo seleccionado de la
        lista disponible

        @type  self: EditorWindow
        @param m: Instancia de la clase EditorWindow
        @rtype:   Ninguno
        @return:  No devuelve nada
        """
        row=self.ArchivosList.currentRow()
        item=self.ArchivosList.item(row)
        try:
            content=open(self.ArchivoDetalle.text()+ item.text(),'r')
            with content:
                data=content.read()
                self.ArchivoDetalle.setText(data)
                content.close()
        except:
            try:
             content=open(self.TituloEdit.text()+ '/'+ item.text(),'r')
             with content:
                data=content.read()
                self.ArchivoDetalle.setText(data)
                content.close()   
            except:    
                print"no se puede abrir"
                
    def saveFile(self):
        """
        Guarda el archivo mostrado en el cuadro de texto apropiado en
        una determinada ruta

        @type  self: EditorWindow
        @param m: Instancia de la clase EditorWindow
        @rtype:   Ninguno
        @return:  No devuelve nada
        """
        try:
            f = open(self.filename[0], "w")
            f.write(self.ArchivoDetalle.toPlainText())
        except:
            try:
                self.filename = QtGui.QFileDialog.getSaveFileName(self, "Guardar archivo")
                self.setWindowTitle("Editor de Texto - %s" % self.filename[0])
                f = open(self.filename[0], "w")
                f.write(self.ArchivoDetalle.toPlainText())
            except:
                self.setWindowTitle("Editor de Texto")
    
    def saveAsFile(self):
        """
        Guarda la información mostrada de un archivo en uno nuevo
        seleccionado

        @type  self: EditorWindow
        @param m: Instancia de la clase EditorWindow
        @rtype:   Ninguno
        @return:  No devuelve nada
        """
        try:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, "Salvar archivo como")
            self.setWindowTitle("Editor de textos - %s" % self.filename[0])
            f = open(self.filename[0], "w")
            f.write(self.ArchivoDetalle.toPlainText())
        except:
            self.setWindowTitle("Editor de textos")  
            
    def cerrar(self):
        """
        Borra la lista de archivos pertenecientes a una carpeta mostrados
        en la ventana apropiada para ello

        @type  self: EditorWindow
        @param m: Instancia de la clase EditorWindow
        @rtype:   Ninguno
        @return:  No devuelve nada
        """
        
        self.ArchivoDetalle.clear()


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = EditorWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()