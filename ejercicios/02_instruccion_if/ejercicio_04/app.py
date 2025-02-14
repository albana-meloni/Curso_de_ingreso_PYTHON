import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, menor o adolescente (edad entre 13 y 17 años) 
de edad, se deberá informar utilizando el Dialog aler.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_guardada = int(self.txt_edad.get())
        mensaje = ""

        if edad_guardada >= 18:
            mensaje = "Usted es mayor de edad"
        elif edad_guardada >= 13:
            mensaje = "Usted es adolescente"
        else:
            mensaje = "Usted es un niño"

        alert("Tu edad", mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()