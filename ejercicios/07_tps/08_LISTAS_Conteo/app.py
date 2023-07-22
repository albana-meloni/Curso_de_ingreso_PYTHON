import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.lista_numeros = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            numero_ingresado = prompt("datos", "ingrese un número")
            if numero_ingresado == None:
                break
            else:
                numero_ingresado = int(numero_ingresado)
                self.lista_numeros.append(numero_ingresado)


    def btn_mostrar_estadisticas_on_click(self):
        lista = self.lista_numeros
        acumulador_negativos = 0
        contador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_ceros = 0
        negativo_min = None
        positivo_max = None

        for i in range(len(lista)):
            if lista[i] < 0:
                contador_negativos += 1
                acumulador_negativos += lista[i]
                if negativo_min == None or lista[i] < negativo_min:
                    negativo_min = lista[i]
            elif lista[i] > 0:
                contador_positivos += 1
                acumulador_positivos += lista[i]
                if positivo_max == None or lista[i] > positivo_max:
                    positivo_max = lista[i]
            else:
                contador_ceros += 1

        promedio_negativos = acumulador_negativos / contador_negativos


        mensaje = "La suma acumulada de los negativos: {0}\n".format(acumulador_negativos)
        mensaje += "La suma acumulada de los positivos: {0}\n".format(acumulador_positivos)
        mensaje += "Cantidad de números positivos ingresados: {0}\n".format(contador_positivos)
        mensaje += "Cantidad de números negativos ingresados: {0}\n".format(contador_negativos)
        mensaje += "Cantidad de ceros: {0}\n".format(contador_ceros)
        mensaje += "El minimo de los negativos: {0}\n".format(negativo_min)
        mensaje += "El maximo de los positivos: {0}\n".format(positivo_max)
        mensaje += "El promedio de los negativos: {0}\n".format(promedio_negativos)

        print(mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
