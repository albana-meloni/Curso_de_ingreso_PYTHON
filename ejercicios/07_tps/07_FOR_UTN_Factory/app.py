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

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        error = "Ingrese un dato válido"
        contador_punto_a = 0

        bandera_edades = False

        contador_postulantes_f = 0
        acumulador_edades_f = 0
        contador_postulantes_m = 0
        acumulador_edades_m = 0
        contador_postulantes_nb = 0
        acumulador_edades_nb = 0

        contador_postulantes_python = 0
        contador_postulantes_js = 0
        contador_postulantes_aspnet = 0
        tecnologia_mas_postulantes = ""

        contador_postulantes_totales = 0


        for numero in range(10):
            # validar nombre
            nombre_valido = False
            while nombre_valido != True:
                nombre_ingresado = prompt("DATOS", "Ingrese el nombre del postulante")
                if nombre_ingresado == None or nombre_ingresado == "" or nombre_ingresado.isdigit():
                    alert("ERROR", error)
                    nombre_valido = False
                else:
                    nombre_valido = True

            # validar edad
            edad_valida = False
            while edad_valida != True:
                edad_ingresada = prompt("DATOS", "Ingrese la edad del postulante")
                if edad_ingresada == None or edad_ingresada == "" or not(edad_ingresada.isdigit()):
                    alert("ERROR", error)
                    edad_valida = False
                else:
                    edad_ingresada = int(edad_ingresada)
                    if edad_ingresada > 17:
                        edad_valida = True
                    else:
                        alert("ERROR", error)
                        edad_valida = False

            # validar género
            genero_valido = False
            while genero_valido != True:
                genero_ingresado = prompt("DATOS", "Ingrese el género del postulante (F - M - NB)")
                if genero_ingresado == None or genero_ingresado == "" or genero_ingresado.isdigit():
                    alert("ERROR", error)
                    genero_valido = False
                else:
                    match genero_ingresado:
                        case "F" | "M" | "NB":
                            genero_valido = True
                        case _:
                            alert("ERROR", error)
                            genero_valido = False

            # validar tecnología
            tecnologia_valida = False
            while tecnologia_valida != True:
                tecnologia_ingresada = prompt("DATOS", "Ingrese la tecnología que maneja el postulante (PYTHON - JS - ASP.NET)")
                if tecnologia_ingresada == None or tecnologia_ingresada == "" or tecnologia_ingresada.isdigit():
                    alert("ERROR", error)
                    tecnologia_valida = False
                else:
                    match tecnologia_ingresada:
                        case "PYTHON" | "JS" | "ASP.NET":
                            tecnologia_valida = True
                        case _:
                            alert("ERROR", error)
                            tecnologia_valida = False

            # validar puesto
            puesto_valido = False
            while puesto_valido != True:
                puesto_ingresado = prompt("DATOS", "Ingrese el puesto del postulante (Jr - Ssr - Sr)")
                if puesto_ingresado == None or puesto_ingresado == "" or puesto_ingresado.isdigit():
                    alert("ERROR", error)
                    puesto_valido = False
                else:
                    match puesto_ingresado:
                        case "Jr" | "Ssr" | "Sr":
                            puesto_valido = True
                        case _:
                            puesto_valido = False


            contador_postulantes_totales += 1


            if genero_ingresado == "NB":
                if tecnologia_ingresada == "ASP.NET" or tecnologia_ingresada == "JS":
                    if edad_ingresada > 24 and edad_ingresada < 41:
                        if puesto_ingresado == "Ssr":
                            contador_punto_a += 1


            if puesto_ingresado == "Jr":
                match bandera_edades:
                    case False:
                        edad_menor = edad_ingresada
                        nombre_edad_menor = nombre_ingresado
                        bandera_edades = True
                    case True:
                        if edad_ingresada < edad_menor:
                            edad_menor = edad_ingresada
                            nombre_edad_menor = nombre_ingresado


            match genero_ingresado:
                case "F":
                    contador_postulantes_f += 1
                    acumulador_edades_f += edad_ingresada
                case "M":
                    contador_postulantes_m += 1
                    acumulador_edades_m += edad_ingresada
                case "NB":
                    contador_postulantes_nb += 1
                    acumulador_edades_nb += edad_ingresada


            match tecnologia_ingresada:
                case "PYTHON":
                    contador_postulantes_python += 1
                case "JS":
                    contador_postulantes_js += 1
                case "ASP.NET":
                    contador_postulantes_aspnet += 1


        if contador_postulantes_python > contador_postulantes_js and contador_postulantes_python > contador_postulantes_aspnet:
            tecnologia_mas_postulantes = "PYTHON"
        elif contador_postulantes_js > contador_postulantes_python and contador_postulantes_js > contador_postulantes_aspnet:
            tecnologia_mas_postulantes = "JS"
        elif contador_postulantes_aspnet > contador_postulantes_python and contador_postulantes_aspnet > contador_postulantes_js:
            tecnologia_mas_postulantes = "ASP.NET"


        promedio_edades_f = acumulador_edades_f // contador_postulantes_f
        promedio_edades_m = acumulador_edades_m // contador_postulantes_m
        promedio_edades_nb = acumulador_edades_nb // contador_postulantes_nb

        porcentaje_postulantes_f = (contador_postulantes_f * 100) // contador_postulantes_totales
        porcentaje_postulantes_m = (contador_postulantes_m * 100) // contador_postulantes_totales
        porcentaje_postulantes_nb = (contador_postulantes_nb * 100) // contador_postulantes_totales


        mensaje = "a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {0}\n".format(contador_punto_a)
        mensaje += "b. Nombre del postulante Jr con menor edad: {0}\n".format(nombre_edad_menor)
        mensaje += "c. Promedio de edades por género: F={0} M={1} NB={2}\n".format(promedio_edades_f, promedio_edades_m, promedio_edades_nb)
        mensaje += "d. Tecnologia con mas postulantes: {0}\n".format(tecnologia_mas_postulantes)
        mensaje += "e. Porcentaje de postulantes de cada genero: F={0}% M={1}% NB={2}%".format(porcentaje_postulantes_f, porcentaje_postulantes_m, porcentaje_postulantes_nb)

        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()