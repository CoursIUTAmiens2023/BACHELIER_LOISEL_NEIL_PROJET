from tkinter import *

fen=Tk()
fen.title('Ping Pong')
canv=Canvas(fen , width=800,height=600,background="black")
canv.pack(fill="both",expand=True)
canv.create_oval (350,250,450,350, fill='black', outline='white', width=1)
canv.create_rectangle (399 ,0 ,401 ,600 , fill='white')
Label(fen,text=" Blue use Z and S, Red use Up and Down ", fg='grey', font=("Impact",16 ,"bold")).place(x=220,y=575)
Raquette = canv.create_rectangle (10 ,250 ,20 ,350 , fill='blue', outline='white')
Raquette2 = canv.create_rectangle (780 ,250 ,790 ,350 , fill='red', outline='white')
global Compteur1,Compteur2
Compteur1 = 0
Compteur2 = 0


def animation () :
    global Vx,Vy
    global Compteur1,Compteur2
    if Compteur1 == 0 and Compteur2 == 0:
        Label(fen,text=" "+str(Compteur1)+"  -  "+str(Compteur2)+" ", fg='grey', font=("Impact",24 ,"bold")).place(x=355,y=0)
    if (canv.coords(Balle)[0]<canv.coords(Raquette)[2]) and (canv.coords(Balle)[1]<canv.coords(Raquette)[3]) and (canv.coords(Balle)[3]>canv.coords(Raquette)[1]) :
        Vx=-Vx
    if canv.coords(Balle)[1]<10 or canv.coords(Balle)[3]>590:
        Vy=-Vy
    if canv.coords(Balle)[0]<0:
        Vx=0
        Vy=0
        Compteur2 = Compteur2 + 1
        Label(fen,text=" "+str(Compteur1)+"  -  "+str(Compteur2)+" ", fg='grey', font=("Impact",24 ,"bold")).place(x=355,y=0)
        canv.coords(Balle,190 ,290 ,210 ,310)
        Vx,Vy=10,10
    if (canv.coords(Balle)[2]>canv.coords(Raquette2)[0]) and (canv.coords(Balle)[1]<canv.coords(Raquette2)[3]) and (canv.coords(Balle)[3]>canv.coords(Raquette2)[1]) :
        Vx=-Vx
    if canv.coords(Balle)[2]>800:
        Vx=0
        Vy=0
        Compteur1 = Compteur1 + 1
        Label(fen,text=" "+str(Compteur1)+"  -  "+str(Compteur2)+" ", fg='grey', font=("Impact",24 ,"bold")).place(x=355,y=0)
        canv.coords(Balle,590 ,290 ,610 ,310)
        Vx,Vy=-10,10
    if Compteur1 == 3:
        Label(fen,text="You win ! :)", fg='blue', font=("Impact",24 ,"bold")).place(x=100,y=250)
        Label(fen,text="You lose ! :(", fg='red', font=("Impact",24 ,"bold")).place(x=550,y=250)
        canv.coords(Balle,390,290,410,310)
        Vx=0
        Vy=0
    if Compteur2 == 3:
        Label(fen,text="You lose ! :(", fg='blue', font=("Impact",24 ,"bold")).place(x=100,y=250)
        Label(fen,text="You win ! :)", fg='red', font=("Impact",24 ,"bold")).place(x=550,y=250)
        canv.coords(Balle,390,290,410,310)
        Vx=0
        Vy=0
    canv.move(Balle ,Vx,Vy)
    fen.after(50 ,animation)
Vx,Vy=10,10
Ballex , Balley=190 ,290
Balle=canv.create_oval(190 ,290 ,210 ,310 , fill='green', outline='white')
animation()

def haut (event) :
    if canv.coords(Raquette)[1]>10 :
        canv.move(Raquette ,0 ,-15)
def bas (event) :
    if canv.coords(Raquette)[3]<590 :
        canv.move(Raquette ,0 ,15)
canv.bind_all( '<z>' , haut )
canv.bind_all( '<s>' , bas )

def haut2 (event) :
    if canv.coords(Raquette2)[1]>10 :
        canv.move(Raquette2 ,0 ,-15)
def bas2 (event) :
    if canv.coords(Raquette2)[3]<590 :
        canv.move(Raquette2 ,0 ,15)
canv.bind_all( '<Up>' , haut2 )
canv.bind_all( '<Down>' , bas2 )

fen.mainloop()