from select import select
import tkinter as ttk
import threading
import time

## Tiene 4 pantallas Menu- Créditos - Puntaje - Juego
## Menu -> Salir - Créditos - Jugar - Puntajes

## Créditos -> Institución - Carrera - Nombre del Curso - Profesor - Estudiante - Carnet - Version - Fotografiá - Fecha modificación 
## Puntajes -> Tiempos de las partidas (puntaje). Las primeras 7 posiciones - Archivos Secuenciales - No se permiten librerías 
## Juego -> Interfaz Gráfica

## Limite de 7 kilometros -> método para contar kilometros dentro de la aplicación
## Velocidad minima y maxima ->  4 marchas
### El aumento de marcha se da cuando llega a las rpm maximas de la marcha actual (Lo define el programdor) rpm se mide por cantidad de tiempo que se presiona el acelerador
### Primera 1s 10-15 
### Segunda 2s 15-45
### Tercera 3s 45-70 

## Cuando se suelta el acelerador las rpm se reinician
## Cambios prematuros disminuyen la velocidad % pero no menos de la velocidad minima
## Una vez alcanzadas las rpm tiene un 1s  para realizar el cambio de marcha, sino el auto se bloquea

## Al frenar el cambio de marcha se realiza de forma automática 

## La velocidad de desplazamiento de los objetos es relativa a la velocidad del jugador.

## La pantalla de juego debe mostrar el Nombre del Piloto - Velocidad - Tiempo - Posición (Cantidad de autos adelantados) - Marcha - Distancia

## Tres carriles y los autos aparecen de forma aleatoria en los carriles en un intervalo aleatorio

## Muestra de rpm, mediante indicadores verdes que se encienden de la siguiente forma
### 1. Se esta acelerando Verde claro
### 2. 50% del tiempo
### 3. 80% del tiempo
### 4. Debe hacer el cambio Verde Fosforescente 

## Frenado 
### 1. Se esta frenando Rojo
### 2. 50% de la velocidad
### 3. mínimo de la velocidad
### 4. Debe hacer el cambio Verde Fosforescente

## Recomendada para trabajar con elementos fijos.
class Menu(ttk.Frame):
    def __init__(self, Window):
        super().__init__(Window)
        self.main = Window
        
        self.label = ttk.Label(self, text="MENU")
        self.label.pack()
        
        self.btn = ttk.Button(self, text="Creditos", command= self.go_Credits)
        self.btn.pack()
        self.btn = ttk.Button(self, text="Puntaje", command= self.go_Puntaje)
        self.btn.pack()
        self.btn = ttk.Button(self, text="Game", command= self.go_Juego)
        self.btn.pack()
        
        self.pack()
        
    def go_Credits(self):
        self.main.destroy()
        C = Creditos(ttk.Tk())
        
    def go_Puntaje(self):
        self.main.destroy()
        C = Puntaje(ttk.Tk())
        
    def go_Juego(self):
        self.main.destroy()
        J = Juego(ttk.Tk(),"Kenneth")

class Creditos(ttk.Frame):
    def __init__(self, Window):
        super().__init__(Window)
        self.main = Window
        
        self.label = ttk.Label(self, text="Creditos")
        self.label.pack()
        
        self.btn = ttk.Button(self, text="Menu", command= self.go_Menu)
        self.btn.pack()
        
        self.pack()
        
    def go_Menu(self):
        self.main.destroy()
        M = Menu(ttk.Tk())

class Puntaje(ttk.Frame):
    def __init__(self, Window):
        super().__init__(Window)
        self.main = Window
        
        self.label = ttk.Label(self, text="Puntaje")
        self.label.pack()
        
        self.btn = ttk.Button(self, text="Menu", command= self.go_Menu)
        self.btn.pack()
        
        self.pack()
        
    def go_Menu(self):
        self.main.destroy()
        M = Menu(ttk.Tk())

## Elementos dinamicos
## GUI
class Juego():
    def __init__(self, window,nombre):
        self.window = window
        self.Jugador = Jugador(nombre)
        self.window.geometry("600x600")
        
        self.btn = ttk.Button(self.window, text="Menu", command= self.go_Menu)
        self.btn.place(x=550,y=550)
        
        self.btn_frenado = ttk.Button(self.window, text="Frenar")
        self.btn_acelerar = ttk.Button(self.window, text="Acelerar")
        self.btn_subirmarcha = ttk.Button(self.window, text="Subir Marcha")
        
        self.btn_acelerar.bind('<Button-1>',lambda e: self.Jugador.acelerar(True,False))
        self.btn_acelerar.bind('<ButtonRelease-1>',lambda e:self.Jugador.acelerar(False,True))
        
        self.btn_acelerar.place(x=100,y=100)
        self.btn_frenado.place(x=100,y=150)
        self.btn_subirmarcha.place(x=150,y=125)
        
        self.Update_Recursivo()
        
        
    def Update_Recursivo(self):
        #print(self.Jugador.get_velocity())
        self.window.after(100,self.Update_Recursivo)
        
    def Update_Thread(self):
        while(True):
            pass
        
    def go_Menu(self):
        self.window.destroy()
        M = Menu(ttk.Tk())

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre;
        self.marcha = 2;
        self.velocity = 10;
        self.rpm = [1,2,2]
        self.max_velocity = [15,45,70]
        self.min_velocity = [10,15,45]
        self.start = 0
        self.end = 0
        self.acelerando = False
        threading.Thread(target = self.Update,daemon=True).start()
        
    def get_velocity(self):
        return self.velocity
    
    def get_Nombre(self):
        return self.nombre
    
    def Update(self):
        while(True):
            if(self.acelerando):
                if((time.time() - self.start)  < self.rpm[self.marcha-1]):
                    tiempo = time.time() - self.start
                    aceleracion = (self.max_velocity[self.marcha-1]-self.min_velocity[self.marcha-1])/self.rpm[self.marcha-1]
                    self.velocity = self.min_velocity[self.marcha-1]+aceleracion*tiempo
                else:
                    print("RPM Maximas")
                    
            else:
                self.velocity = self.min_velocity[self.marcha-1]
            print(self.velocity)
            
    def acelerar(self,Press,Release):
        if(Press):
            self.start = time.time()
            self.acelerando = True
        
        if(Release):
            self.acelerando = False
            
            
    def subir_marcha(self):
        pass
    def frenar(self):
        pass
    def bajar_marcha(self):
        pass

class Obstaculo():
    def __init__(self):
        self.image
        self.posx = 0 
        self.posy = 0
        
    def setPos(self,x,y):
        self.posx = x
        self.posy = y
        
if __name__ == '__main__':
    window = ttk.Tk()
    app = Menu(window)
    app.mainloop()