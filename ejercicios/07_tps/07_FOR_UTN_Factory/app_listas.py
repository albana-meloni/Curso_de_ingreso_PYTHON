'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

        self.lista_nombres = []
        self.lista_edades = []
        self.lista_generos = []
        self.lista_tecnologias = []
        self.lista_puestos = []

    def btn_validar_on_click(self):
        total_postulantes = 0
        # punto a
        contador_punto_a = 0
        # punto b
        menor_edad_jr = None
        nombre_menor_edad_jr = None
        # punto c
        contador_f = 0
        acumulador_edades_f = 0
        contador_m = 0
        acumulador_edades_m = 0
        contador_nb = 0
        acumulador_edades_nb = 0
        # punto d
        contador_python = 0
        contador_js = 0
        contador_aspnet = 0
        contador_tecnologias = 0
        tecnologia_mayor_postulantes = None


        for i in range(10):
            while True:
                nombre_ingresado = prompt("UTN Software Factory", "ingrese el nombre del postulante")
                if nombre_ingresado == None:
                    alert("error", "ingrese un valor")
                else:
                    self.lista_nombres.append(nombre_ingresado)
                    break
            while True:
                edad_ingresada = prompt("UTN Software Factory", "ingrese la edad del postulante")
                if edad_ingresada == None:
                    alert("error", "ingrese un valor")
                else:
                    edad_ingresada = int(edad_ingresada)
                    if edad_ingresada > 17:
                        self.lista_edades.append(edad_ingresada)
                        break
                    else:
                        alert("error", "debe ser mayor de edad")
            while True:
                genero_ingresado = prompt("UTN Software Factory", "ingrese el genero del postulante (F-M-NB)")
                if genero_ingresado == None or (genero_ingresado != "F" and genero_ingresado != "M" and genero_ingresado != "NB"):
                    alert("error", "ingrese un valor correcto")
                else:
                    self.lista_generos.append(genero_ingresado)
                    break
            while True:
                tecnologia_ingresada = prompt("UTN Software Factory", "ingrese la tecnologia que maneje el postulante (PYTHON - JS - ASP.NET)")
                if tecnologia_ingresada == None or (tecnologia_ingresada != "PYTHON" and tecnologia_ingresada != "JS" and tecnologia_ingresada != "ASP.NET"):
                    alert("error", "ingrese un valor correcto")
                else:
                    self.lista_tecnologias.append(tecnologia_ingresada)
                    break
            while True:
                puesto_ingresado = prompt("UTN Software Factory", "ingrese el puesto del postulante (Jr - Ssr - Sr)")
                if puesto_ingresado == None or (puesto_ingresado != "Jr" and puesto_ingresado != "Ssr" and puesto_ingresado != "Sr"):
                    alert("error", "ingrese un valor correcto")
                else:
                    self.lista_puestos.append(puesto_ingresado)
                    break

            total_postulantes += 1

        for i in range(total_postulantes):
            if (self.lista_generos[i] == "NB" and
                (self.lista_tecnologias[i] == "ASP.NET" or self.lista_tecnologias[i] == "JS") and
                self.lista_edades[i] > 24 and self.lista_edades[i] < 41 and
                self.lista_puestos[i] == "Ssr"):
                contador_punto_a += 1

            if self.lista_puestos[i] == "Jr" and (menor_edad_jr == None or self.lista_edades[i] < menor_edad_jr):
                menor_edad_jr = self.lista_edades[i]
                nombre_menor_edad_jr = self.lista_nombres[i]

            match self.lista_generos[i]:
                case "F":
                    contador_f += 1
                    acumulador_edades_f += self.lista_edades[i]
                case "M":
                    contador_m += 1
                    acumulador_edades_m += self.lista_edades[i]
                case "NB":
                    contador_nb += 1
                    acumulador_edades_nb += self.lista_edades[i]

            match self.lista_tecnologias[i]:
                case "PYTHON":
                    contador_python += 1
                case "JS":
                    contador_js += 1
                case "ASP.NET":
                    contador_aspnet += 1

        # punto c
        promedio_edades_f = acumulador_edades_f // contador_f
        promedio_edades_m = acumulador_edades_m // contador_m
        promedio_edades_nb = acumulador_edades_nb // contador_nb

        # punto d
        if contador_python > contador_js and contador_python > contador_aspnet:
            tecnologia_mayor_postulantes = "PYTHON"
            contador_tecnologias = contador_python
        elif contador_js > contador_aspnet and contador_js > contador_python:
            tecnologia_mayor_postulantes = "JS"
            contador_tecnologias = contador_js
        elif contador_aspnet > contador_js and contador_aspnet > contador_python:
            tecnologia_mayor_postulantes = "ASP.NET"
            contador_tecnologias = contador_aspnet

        # punto e
        porcentaje_f = contador_f * 100 // total_postulantes
        porcentaje_m = contador_m * 100 // total_postulantes
        porcentaje_nb = contador_nb * 100 // total_postulantes



        mensaje = "a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {0}\n".format(contador_punto_a)
        mensaje += "b. Nombre del postulante Jr con menor edad: {0}, {1} años\n".format(nombre_menor_edad_jr, menor_edad_jr)
        mensaje += "c. Promedio de edades por género: F={0} M={1} NB={2}\n".format(promedio_edades_f, promedio_edades_m, promedio_edades_nb)
        mensaje += "d. Tecnologia con mas postulantes: {0} ({1})\n".format(tecnologia_mayor_postulantes, contador_tecnologias)
        mensaje += "e. Porcentaje de postulantes de cada genero: F={0}% M={1}% NB={2}%".format(porcentaje_f, porcentaje_m, porcentaje_nb)

        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()