import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera hasta que presione el botón Cancelar (en el prompt).
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de ceros

    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados

    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        # negativos
        suma_acumulada_negativos = 0
        contador_de_negativos = 0
        # positivos
        suma_acumulada_positivos = 0
        contador_de_positivos = 0
        # ceros
        contador_de_ceros = 0

        while True:
            numero_ingresado = prompt("Datos", "Ingrese un número")
            if numero_ingresado == None:
                break
            else:
                numero_ingresado = int(numero_ingresado)
                if numero_ingresado < 0:
                    suma_acumulada_negativos += numero_ingresado
                    contador_de_negativos += 1
                    mensaje_negativos = "La suma acumulada de los negativos es: {0} y la cantidad ingresada es: {1}".format(suma_acumulada_negativos, contador_de_negativos)
                elif numero_ingresado > 0:
                    suma_acumulada_positivos += numero_ingresado
                    contador_de_positivos += 1
                    mensaje_positivos = "La suma acumulada de los positivos es: {0} y la cantidad ingresada es: {1}".format(suma_acumulada_positivos, contador_de_positivos)
                elif numero_ingresado == 0:
                    contador_de_ceros += 1
                    mensaje_ceros = "La cantidad de ceros ingresados es: {0}".format(contador_de_ceros)

        if contador_de_positivos > contador_de_negativos:
            diferencia_positivos_negativos = contador_de_positivos - contador_de_negativos
        else:
            diferencia_positivos_negativos = contador_de_negativos - contador_de_positivos

        alert("Datos", "{0}\n{1}\n{2}\nLa diferencia entre la cantidad de los números positivos ingresados y los negativos es: {3}".format(mensaje_negativos, mensaje_positivos, mensaje_ceros, diferencia_positivos_negativos))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
