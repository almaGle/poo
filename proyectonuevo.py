import tkinter as tk

#atributo de los personajes
class MainChar():
    hp=100
    energia=100

    def __init__(self):
        pass

    def recibirdano(self, cantidad):
        self.hp=self.hp-cantidad
        if(self.hp<0):
            self.hp=100
            self.nivel=self.nivel-1
            self.exp=0
        
    def recuperarhp(self,cantidad):
        self.hp=self.hp+cantidad
        if(self.hp>self.hpmax):
            self.hap=self.hpmax
    def cambioexp(self,cantidad):
        if(self.exp>self.expcap):
            self.nivel=self.nivel+1
        self.exp=(self.exp+cantidad)-self.expcap
    def informacion(self):
        return 'hp: ', self.hp, 'exp: ', self.exp, 'nivel: ', self.nivel
    pass
personaje=MainChar()
personaje2=MainChar()

#Crear ventana 800x800
ventana = tk.Tk()
ventana.title("Juego siuuu")
ventana.geometry("800x800")


ventana.mainloop()