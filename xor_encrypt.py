import os
from time import time
from tkinter import *
from tkinter.filedialog import askopenfilename

def xorEncrypt(fileIn):
    start = time()

    key = enterKey.get()
    key = key.encode() #codifico la clave para que quede en formato de bytes

    file = open(fileIn, "r+b")
    size = os.path.getsize(fileIn)
    block = len(key) #cantidad de bytes que voy a ir tomando del archivo igual al largo de la clave para la iteracion

    while size > 0:
        content = file.read(min(size, block)) #tomo una cantidad "block" de bytes o directamente el tamaño del archivo si es menor que blocks
        out = b'' #la salida debe ir en formato de bytes

        for n in range(min(size, block)):
            out += bytes([content[n] ^ key[n]]) #aplico XOR a cada byte del blocke con cada byte de la llave

        file.seek(-min(size, block), 1) #el puntero que quedo al final del bloque que tome, lo vuelvo al origen del bloque para escribir el bloque encriptado
        file.write(out)

        size -= min(size, block) #resto el bloque que ya tome del tamaño total del archivo

    file.close()

    end = time()
    print(end - start)

def openFile():
    global fileName
    fileName = askopenfilename(initialdir="C:/",
                               filetypes =(("All Files","*.*"),("Text File", "*.txt"),),
                               title = "Abrir Archivo")
    route.set(fileName)

window = Tk()
window.title("XOR Encrypter")
window.geometry("300x150")

fileName = None

openFile = Button(window, text="Seleccionar Archivo", command=openFile)
openFile.pack()

route = StringVar()
fileRoute = Entry(window,
                  textvariable=route,
                  width=40)
fileRoute.pack()

passLabel = Label(window,text="Llave:")
passLabel.pack()

enterKey = Entry(window, show="*")
enterKey.pack()

encryptFile = Button(window, text="Encriptar/Desencriptar", command=lambda: xorEncrypt(fileName))
encryptFile.pack()

window.mainloop()
#xorEncrypt("prueba.txt")
