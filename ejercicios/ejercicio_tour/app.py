import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
nombre: Albana
apellido: Meloni

Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:
    1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

    2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,  
    medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

    3- Validar todos los datos.

    4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

    5- Una vez ingresada la cantidad se debe pedir por cada excursión 
    el importe y el tipo de excursión (caminata  o vehículo). 
    informar cual es el precio más caro, el más barato y el promedio

    6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        error = "Debe ingresar un dato válido"

        nombre_validado = False
        edad_validada = False
        genero_validado = False
        altura_validada = False

        excursiones_validada = False
        contador = 0
        suma_acumulada = 0
        bandera = False
        acumulador_caminata = 0
        acumulador_vehiculo = 0


        # validación nombre
        while nombre_validado != True:
            nombre_ingresado = prompt("Datos", "Ingrese su nombre, por favor")
            if nombre_ingresado == None or nombre_ingresado == "" or nombre_ingresado.isdigit():
                alert("ERROR >:(", error)
                nombre_validado = False
            else:
                nombre_validado = True
                mensaje = "Usted es {0}, ".format(nombre_ingresado)

        # validación edad
        while edad_validada != True:
            edad_ingresada = prompt("Datos", "Ingrese su edad, por favor")
            if edad_ingresada == None or edad_ingresada == "" or not(edad_ingresada.isdigit()):
                alert("ERROR >:(", error)
                edad_validada = False
            else:
                edad_ingresada = int(edad_ingresada)
                edad_validada = True
                mensaje += "tiene {0} años de edad ".format(edad_ingresada)

        # validación género
        while genero_validado != True:
            genero_ingresado = prompt("Datos", "Ingrese su género, por favor")
            if genero_ingresado == None or genero_ingresado == "" or genero_ingresado.isdigit():
                alert("ERROR >:(", error)
                genero_validado = False
            else:
                genero_validado = True
                mensaje += "y su género es {0}".format(genero_ingresado)

        # validación altura
        while altura_validada != True:
            altura_ingresada = prompt("Datos", "Ingrese su altura en CM, por favor")
            if altura_ingresada == None or altura_ingresada == "" or len(altura_ingresada) > 3 or not(altura_ingresada.isdigit()):
                alert("ERROR >:(", error)
                altura_validada = False
            else:
                altura_ingresada = int(altura_ingresada)
                if altura_ingresada <= 140:
                    mensaje += ". Su altura es baja."
                elif altura_ingresada <= 170:
                    mensaje += ". Su altura es media."
                elif altura_ingresada <= 190:
                    mensaje += ". Su altura es alta."
                else:
                    mensaje += ". Su altura es muuy alta."
                altura_validada = True


        # validación excursiones
        while excursiones_validada != True:
            excursiones_ingresadas = prompt("Datos", "Ingrese la cantidad de excursiones (MÁXIMO = 11)")
            if excursiones_ingresadas == None or excursiones_ingresadas == "" or not(excursiones_ingresadas.isdigit()):
                alert("ERROR >:(", error)
                excursiones_validada = False
            else:
                excursiones_ingresadas = int(excursiones_ingresadas)
                if excursiones_ingresadas >= 0 and excursiones_ingresadas < 12:
                    excursiones_validada = True
                else:
                    alert("ERROR >:(", error)
                    excursiones_validada = False

        while contador < excursiones_ingresadas:
            importe_validado = False
            while importe_validado != True:
                importe_ingresado = prompt("Excursión", "Ingrese el importe para la excursión {0}".format(contador+1))
                if importe_ingresado == None or importe_ingresado == "" or not(importe_ingresado.isdigit()):
                    alert("ERROR >:(", error)
                    importe_validado = False
                else:
                    importe_ingresado = int(importe_ingresado)
                    suma_acumulada += importe_ingresado
                    importe_validado = True
            match bandera:
                    case False:
                        precio_mayor = importe_ingresado
                        precio_menor = importe_ingresado
                        bandera = True
                    case True:
                        if importe_ingresado > precio_mayor:
                            precio_mayor = importe_ingresado
                        elif importe_ingresado < precio_menor:
                            precio_menor = importe_ingresado


            tipo_validado = False
            while tipo_validado != True:
                tipo_ingresado = prompt("Excursión", "Indique el tipo para la excursión {0} (caminata o vehículo)".format(contador+1))
                if tipo_ingresado == "caminata" or tipo_ingresado == "vehículo":
                    tipo_validado = True
                    match tipo_ingresado:
                        case "caminata":
                            acumulador_caminata += 1
                        case "vehículo":
                            acumulador_vehiculo += 1
                else:
                    alert("ERROR >:(", error)
                    tipo_validado = False
            contador += 1

        promedio_excursiones = suma_acumulada // excursiones_ingresadas

        mensaje += "\nEl precio más caro entre todas las excursiones es ${0}, el más barato es ${1} y el promedio entre todas las excursiones es ${2}".format(precio_mayor, precio_menor, promedio_excursiones)

        if acumulador_caminata == acumulador_vehiculo:
            mensaje += "\nSe seleccionó la misma cantidad de excursiones de caminata y en vehículo ({0})".format(acumulador_vehiculo)
        elif acumulador_caminata > acumulador_vehiculo:
            mensaje += "\nLa excursión más seleccionada es caminata"
        else:
            mensaje += "\nLa excursión más seleccionada es en vehículo"


        alert("Datos ingresados", mensaje)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()