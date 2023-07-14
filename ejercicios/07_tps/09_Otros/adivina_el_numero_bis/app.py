import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Albana
apellido: Meloni

Adivina el número (v 1.0) bis:
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “usted es un Psíquico”.
	2° intento: “excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	Más de 6 intentos: “afortunado en el amor!!”.

de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Adivine el número ->")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0

    def btn_mostrar_on_click(self):
        numero_ingresado = int(self.txt_numero.get())
        self.numero_intento += 1
        numeros_faltantes = 0

        if numero_ingresado == self.numero_secreto:
            match self.numero_intento:
                case 1:
                    mensaje = "Usted es un psíquico :0 \n¡Adivinó el número secreto en el 1° intento!"
                case 2:
                    mensaje = "Excelente percepción c: \n¡Adivinó el número secreto en el 2° intento!"
                case 3:
                    mensaje = "Esto es suerte :P \n¡Adivinó el número secreto en el 3° intento!"
                case 4 | 5 | 6:
                    mensaje = "Excelente técnica :D \n¡Adivinó el número secreto en el {0}° intento!".format(self.numero_intento)
                case _:
                    mensaje = "Afortunado en el amor ;) \n¡Tardó {0} intentos en adivinar el número secreto!".format(self.numero_intento)
        elif numero_ingresado > self.numero_secreto:
            numeros_faltantes = numero_ingresado - self.numero_secreto
            mensaje = "¡VOLVÉ A INTENTARLO! \nTodavía no descubriste el número secreto, te pasaste por {0} número(s)\nCantidad de intentos: {1}".format(numeros_faltantes, self.numero_intento)
        else:
            numeros_faltantes = self.numero_secreto - numero_ingresado
            mensaje = "¡VOLVÉ A INTENTARLO! \nTodavía no descubriste el número secreto, te falta {0} número(s)\nCantidad de intentos: {1}".format(numeros_faltantes, self.numero_intento)

        alert("RESULTADO", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()