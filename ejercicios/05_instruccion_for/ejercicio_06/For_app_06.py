import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni

Al presionar el botón Mostrar pedir un número. mostrar los números pares desde el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = int(prompt("numeritos","ingrese un número"))
        contador_pares = 0
        for numero in range(0,numero_ingresado,2):
            contador_pares += 1
            alert("mensaje", "número par encontrado: {0}\nnúmeros pares encontrados en total: {1}".format(numero,contador_pares))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()