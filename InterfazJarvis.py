from tkinter import *

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

ventana = Tk()
ventana.resizable(True,True)
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

nameFile = StringVar(ventana, "")
contenido = str()

def funcionLeer():
    var = askopenfilename()
    nameFile.set(var) # show an "Open" dialog box and return the path to the selected file
    with open(str(var), "r") as f:
        contenido = f.read()
    campoTexto.insert(INSERT,contenido)

botonLeer = Button(ventana, text = "Leer", command = funcionLeer)
botonLeer.grid(row = 1, column = 0)


campoTexto = Text(ventana, width = 50, height = 25) # Text() permite crear cuadros de textogrande
campoTexto.grid(row = 2, column = 0)
barra_vertical = Scrollbar(ventana, command = campoTexto.xview)
barra_vertical.grid(row = 3, column = 2)# n y s alargan el scrollbar al tamaño del textbox

print(nameFile)
ventana.mainloop()

