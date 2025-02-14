import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni

Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        # las listas son un tipo de dato para recordar los valores y el orden en que el usuario haya ingresado datos        
        for numero in self.lista_datos:
            alert("Lista", numero)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()