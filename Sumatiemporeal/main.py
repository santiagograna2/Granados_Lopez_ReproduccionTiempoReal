
#programa que reproduce archivos de audio en tiempo real
#disenado por santiago granados e ismael lopez
#programacion de audio aplicada
#universidad de san buenaventura
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
import threading
from play import Play

def main():

    ventana = Tk()
    ventana.title('Suma de audios')
    ventana.geometry("427x327")
    imageL=PhotoImage(file="pastools.gif")
    lblImagen=Label(ventana,image=imageL).place(x=0,y=1)

    #Cargar achivo1
    def archivo():

        global audio
        audio= askopenfilename()

    #Cargar archivo2
    def archivo2():

        global audio2
        audio2= askopenfilename()

    #Cargar archivo3
    def archivo3():

        global audio3
        audio3= askopenfilename()

    def archivo4():

        global audio4
        audio4= askopenfilename()

    def reproducir():

        global audio, audio2, audio3, audio4

        s=threading.Thread(target=suma, args=(audio,))
        t=threading.Thread(target=suma, args=(audio2,))
        u=threading.Thread(target=suma, args=(audio3,))
        v=threading.Thread(target=suma, args=(audio4,))
        s.start()
        t.start()
        u.start()
        v.start()


    def suma(nombre):

        sonido=Play(1024)
        Datos=sonido.open(nombre)
        sonido.start(Datos[0],Datos[1],Datos[2])
        sonido.play(Datos[3])
        sonido.closed()

    b1 = Button(ventana,text="ARCHIVO 1",command = archivo ,font=("Agency FB", 14),width=10).place(x=20,y=200)
    b2 = Button(ventana,text="ARCHIVO 2",command = archivo2,font=("Agency FB", 14),width=10).place(x=120,y=200)
    b3 = Button(ventana,text="ARCHIVO 3",command = archivo3,font=("Agency FB", 14),width=10).place(x=220,y=200)
    b4 = Button(ventana,text="ARCHIVO 4",command = archivo4,font=("Agency FB", 14),width=10).place(x=320,y=200)
    b5 = Button(ventana,text="PLAY",command =reproducir,font=("Agency FB", 14),width=10).place(x=172,y=265)

    ventana.mainloop()

if __name__=="__main__":
    main()