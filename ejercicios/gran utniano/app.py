import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:
Nombre del votante
Edad del votante (debe ser mayor a 13)
Género del votante (Masculino, Femenino, Otro)
El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A- El promedio de edad de las votantes de género Femenino 
B- Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
C- Nombre del votante más joven qué votó a Gianni.
D- Nombre de cada participante y porcentaje de los votos qué recibió.
E- El nombre del participante que debe dejar la casa (El que tiene más votos)

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_nombres = []
        self.lista_edades = []
        self.lista_genero = [] 
        self.lista_participantes = []


    def btn_mostrar_on_click(self):
        #A- El promedio de edad de las votantes de género Femenino 
        contador_femenino = 0
        acumulador_femenino = 0
        for i in range(len(self.lista_edades)):
            if self.lista_genero[i] == "Femenino":
                acumulador_femenino += self.lista_edades[i]
                contador_femenino += 1


        if contador_femenino >= 1:
            promedio_edad_femenino = acumulador_femenino / contador_femenino
        else:
            promedio_edad_femenino = "No hubo votantes femeninos"
        
        mensaje = "El promedio de edad de las votantes de género Femenino es: {0}\n".format(promedio_edad_femenino)


        #B- Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
        contador_masculino = 0
        for i in range(len(self.lista_edades)):
            if (self.lista_genero[i] == "Masculino" and 
                self.lista_edades[i] > 24 and self.lista_edades[i] < 41 and 
                (self.lista_participantes[i] == "Giovanni" or self.lista_participantes[i] == "Facundo")):
                contador_masculino += 1

        mensaje += "Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo son: {0}\n".format(contador_masculino)


        #C- Nombre del votante más joven qué votó a Gianni.
        edad_min = None
        nombre_votante_joven = None
        for i in range(len(self.lista_participantes)):
            if self.lista_participantes[i] == "Gianni":
                if edad_min == None or self.lista_edades[i] < edad_min:
                    edad_min = self.lista_edades[i]
                    nombre_votante_joven = self.lista_nombres[i]
                    
        if nombre_votante_joven == None:
            mensaje_votantes = "No hay votos para Gianni."
        else:
            mensaje_votantes = f"El votante mas joven que votó a Gianni es {nombre_votante_joven} y tiene {edad_min} años"  
        
        mensaje += "{0}\n".format(mensaje_votantes)

        #D- Nombre de cada participante y porcentaje de los votos qué recibió.
        contador_gianni = 0
        contador_giovanni = 0
        contador_facundo = 0

        for i in range(len(self.lista_participantes)):

            nombre_participante = self.lista_participantes[i]

            match nombre_participante:
                case "Gianni":
                    contador_gianni += 1
                case "Giovanni":
                    contador_giovanni += 1
                case "Facundo":
                    contador_facundo += 1
        
        # numero_votos*(100/total_participantes) = porcentaje_votos

        porcentaje_votos_gianni = contador_gianni*(100/len(self.lista_participantes))
        porcentaje_votos_giovanni = contador_giovanni*(100/len(self.lista_participantes))
        porcentaje_votos_facundo = contador_facundo*(100/len(self.lista_participantes))

        mensaje_porcentaje_votos = f"Participante Gianni. Porcentaje de votos: {round(porcentaje_votos_gianni,2)}%\nParticipante Giovanni. Porcentaje de votos: {round(porcentaje_votos_giovanni,2)}%\nParticipante facundo. Porcentaje de votos: {round(porcentaje_votos_facundo,2)}%"
        
        mensaje += mensaje_porcentaje_votos + "\n"
        
        #E- El nombre del participante que debe dejar la casa (El que tiene más votos)
        if contador_facundo > contador_gianni and contador_facundo > contador_giovanni:
            nombre_expulsado = "Facundo"
            porcentaje_expulsado = porcentaje_votos_facundo
        elif contador_gianni > contador_giovanni:
            nombre_expulsado = "Gianni"
            porcentaje_expulsado = porcentaje_votos_gianni
        else:
            nombre_expulsado = "Giovanni"
            porcentaje_expulsado = porcentaje_votos_giovanni
            
        mensaje += f"Quién debe abandonar la casa es {nombre_expulsado} con el {(round(porcentaje_expulsado,2))}% de los votos"

        print(mensaje)


    def btn_cargar_on_click(self):
        continuar = question("gran utniano", "¿desea agregar un voto?")
        while continuar != False:

            # nombre
            while True:
                nombre_votante = prompt("gran utniano", "ingrese su nombre")
                if nombre_votante == None:
                    alert("error", "ingrese un valor")
                else:
                    self.lista_nombres.append(nombre_votante)
                    break

            # edad
            while True:
                edad_votante = prompt("gran utniano", "ingrese su edad")
                if edad_votante == None:
                    alert("error", "ingrese un valor")
                else:
                    edad_votante = int(edad_votante)
                    if edad_votante > 12:
                        self.lista_edades.append(edad_votante)
                        break
                    else:
                        alert("error", "debe ser mayor a 13 años")

            # género
            while True:
                genero_votante = prompt("gran utniano", "ingrese su género (Femenino, Masculino u Otro)")
                if genero_votante == None or (genero_votante != "Femenino" and genero_votante != "Masculino" and genero_votante != "Otro"):
                    alert("error", "ingrese un valor correcto")
                else:
                    self.lista_genero.append(genero_votante)
                    break

            # a quién votó
            while True:
                participante_votado = prompt("gran utniano", "ingrese el participante que quiere votar, los nominados son: Giovanni - Gianni - Facundo")
                if participante_votado == None or (participante_votado != "Giovanni" and participante_votado != "Gianni" and participante_votado != "Facundo"):
                    alert("error", "ingrese un valor correcto")
                else:
                    self.lista_participantes.append(participante_votado)
                    break

            continuar = question("gran utniano", "el voto fue cargado, ¿desea agregar otro más?")

if __name__ == "__main__":
    app = App()
    app.mainloop()