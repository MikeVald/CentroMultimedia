import Tkinter as tk  
import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from vlc import Instance
import time
import os
import sys
#import pathlib
import webbrowser

class VLC:# Crea instancia de VLC
    def __init__(self):
        self.Player = Instance('--loop')#lo genera en modo bucle

    def addPlaylist(self,op):   #agrega a la lista de reproduccion dependiendo el tipo de archivo
        self.mediaList = self.Player.media_list_new()#crea lista de reproduccion vacia
       
        path = r"/home/pi/Desktop/PFE"
        songs = os.listdir(path)#crea lista de los archivos
#        for x in songs:
 #           
  #              print(x)
        for s in songs:#filtra tipo de archivo dependiendo la eleccion
            if op==1:#fotos
                if '.jpg' in str(s) or 'png' in str(s) or 'jpeg' in str(s):
                    self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        
            if op==2:#videos
                if '.mp4' in str(s) or '.avi' in str(s):
                    self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        
            if op==3:#musica
                if '.mp3' in str(s):
                    self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()#crea lista de reproduccion vacia en la instancia de VLC
        self.listPlayer.set_media_list(self.mediaList)#remplaza la lista de reproduccion de la instancia anterior con la nueva
    def play(self):#reproduce
        self.listPlayer.play()
    def next(self):#siguiente
        self.listPlayer.next()
    def pause(self):#pausa
        self.listPlayer.pause()
    def previous(self):#anterior
        self.listPlayer.previous()
    def stop(self):#Alto
        self.listPlayer.stop()
    def playpause(self):#itera entre reproducir y pausar
        if self.listPlayer.is_playing():
            self.stop()
        else:
            self.play()
        
def repMusica(op):
    
    player.addPlaylist(op)#crea lista de reproduccion

    player.play()#reproduce
    
    while player.is_playing():#mientras este reproduciendo, no pasa a la siguiente
        time.sleep(1)

    player.next()#siguiente elemento
    time.sleep(9)

win = tk.Tk()  #crea la ventana
win.title("ProyectoEmbebidos")  
win.geometry("1000x800")#redimenciona la ventana
lab=ttk.Label(win, text="Bienvenido", font=('Helvetica', 18, "bold")).pack(side="top", fill="x")

style = ttk.Style()

try:#estilo de pantalla
    style.theme_create( "yumi", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1],"font" : ('URW Gothic L', '11', 'bold'), "background": "#CCD1D1" },
            "map":       {"background": [("selected", "#D6DBDF")],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )
    style.theme_use("yumi")
except:
    
    style.theme_use("yumi")

#Create Tab Control  
tabControl=ttk.Notebook(win) 
#Tab1  
Video=tk.Frame(tabControl,bg='#AAB7B8') 
tabControl.add(Video,text='Videos Online')  

#Tab2  
Musica=tk.Frame(tabControl,bg='#AAB7B8')  
tabControl.add(Musica, text='Musica  Online')

#Tab3  
USB=tk.Frame(tabControl,bg='#AAB7B8')  
tabControl.add(USB, text="Contenido de USB")
tabControl.pack(expand=1, fill="both")  

#Video online  
netflix = Image.open('netflix.png')#carga logo
netflix = netflix.resize((220,120),Image.ANTIALIAS)
netflix = ImageTk.PhotoImage(netflix)#crea instancia de Image
ttk.Button(Video,image=netflix,
          command=lambda : webbrowser.open("http://www.netflix.com", new=2, autoraise=True)).pack(padx=20,side="left")#boton para netflix

prime = Image.open('prime.png')
prime = prime.resize((220,120),Image.ANTIALIAS)
prime = ImageTk.PhotoImage(prime)
ttk.Button(Video,image=prime,
          command=lambda : webbrowser.open("http://www.primevideo.com", new=2, autoraise=True)).pack(padx=10,side="left")#boton para prime video

blim = Image.open('blim.png')
blim = blim.resize((220,120),Image.ANTIALIAS)
blim = ImageTk.PhotoImage(blim)
ttk.Button(Video,image=blim,
          command=lambda : webbrowser.open("http://www.blim.com", new=2, autoraise=True)).pack(padx=10,side="left")#boton para blim

#Musica

spotify = Image.open('spotify.png')
spotify = spotify.resize((220,120),Image.ANTIALIAS)
spotify = ImageTk.PhotoImage(spotify)
ttk.Button(Musica,image=spotify,
           command=lambda : webbrowser.open("http://www.spotify.com", new=2, autoraise=True)).pack(padx=20,side="left")#boton para spotify

deezer = Image.open('deezer.png')
deezer = deezer.resize((220,120),Image.ANTIALIAS)
deezer = ImageTk.PhotoImage(deezer)
ttk.Button(Musica,image=deezer,
           command=lambda : webbrowser.open("http://www.deezer.com", new=2, autoraise=True)).pack(padx=10,side="left")#boton para deezer

#USB  

player = VLC()

fotos = Image.open('fotos.png')
fotos = fotos.resize((220,120),Image.ANTIALIAS)
fotos = ImageTk.PhotoImage(fotos)
ttk.Button(USB,image=fotos,
           command=lambda : repMusica(1)).pack(padx=20,side="left")#reproduce imagenes

videos = Image.open('videos.png')
videos = videos.resize((220,120),Image.ANTIALIAS)
videos = ImageTk.PhotoImage(videos)
ttk.Button(USB,image=videos,
           command=lambda : repMusica(2)).pack(padx=10,side="left")#reproduce videos

musica = Image.open('musica.png')
musica = musica.resize((220,120),Image.ANTIALIAS)
musica = ImageTk.PhotoImage(musica)
ttk.Button(USB,image=musica,
           command=lambda : repMusica(3)).pack(padx=10,side="left")#reproduce musica

#botones para controlar la reproduccion
ttk.Button(USB,text="Prev",
           command=lambda : player.previous()).place(x=20, y=400)
ttk.Button(USB,text="PAUSE/PLAY",
           command=lambda : player.playpause()).place(x=70, y=400)
ttk.Button(USB,text="STOP",
           command=lambda : player.stop()).place(x=170, y=400)
ttk.Button(USB,text="Next",
           command=lambda : player.next()).place(x=230, y=400)

#Calling Main()  
win.mainloop()  

