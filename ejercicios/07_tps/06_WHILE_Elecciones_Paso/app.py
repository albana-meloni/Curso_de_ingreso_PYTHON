'''
nombre: Albana
apellido: Meloni

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        bandera = False
        contador_candidatos = 0
        acumulador_edades = 0
        total_votos = 0

        candidatos = question("pregunta...", "Querés agregar un candidato?")

        while candidatos == True:
            # validar nombre
            nombre_valido = False
            while nombre_valido != True:
                nombre_ingresado = prompt("candiDATOS", "Ingrese el nombre del candidato")
                if nombre_ingresado == None or nombre_ingresado == "" or nombre_ingresado.isdigit():
                    alert("ERROR", error)
                    nombre_valido = False
                else:
                    nombre_valido = True

            # validar edad
            edad_valida = False
            while edad_valida != True:
                edad_ingresada = prompt("candiDATOS", "Ingrese la edad del candidato (mayor a 25 años)")
                if edad_ingresada == None or edad_ingresada == "" or not(edad_ingresada.isdigit()):
                    alert("ERROR", error)
                    edad_valida = False
                else:
                    edad_ingresada = int(edad_ingresada)
                    if edad_ingresada > 25:
                        edad_valida = True
                        acumulador_edades += edad_ingresada
                    else:
                        alert("ERROR", error)
                        edad_valida = False

            # validar votos
            votos_validos = False
            while votos_validos != True:
                votos_ingresados = prompt("candiDATOS", "Ingrese el total de votos obtenidos")
                if votos_ingresados == None or votos_ingresados == "" or not(votos_ingresados.isdigit()):
                    alert("ERROR", error)
                    votos_validos = False
                else:
                    votos_ingresados = int(votos_ingresados)
                    if votos_ingresados <= 0:
                        votos_validos = False
                    else:
                        votos_validos = True
                        total_votos += votos_ingresados

            match bandera:
                case False:
                    mayores_votos = votos_ingresados
                    candidato_mayores_votos = nombre_ingresado
                    menores_votos = votos_ingresados
                    candidato_menores_votos = nombre_ingresado
                    edad_candidato_menores_votos = edad_ingresada
                    bandera = True
                case True:
                    if votos_ingresados > mayores_votos:
                        mayores_votos = votos_ingresados
                        candidato_mayores_votos = nombre_ingresado
                    elif votos_ingresados < menores_votos:
                        menores_votos = votos_ingresados
                        candidato_menores_votos = nombre_ingresado
                        edad_candidato_menores_votos = edad_ingresada

            contador_candidatos += 1
            candidatos = question("pregunta...", "Querés agregar otro candidato?")

        promedio_edades = acumulador_edades // contador_candidatos

        mensaje = "El candidato con más votos es: {0}\nEl candidato con menos votos es: {1} y tiene {2} años\nEl promedio de las edades de los candidatos es: {3}\nEl total de votos emitidos es: {4}".format(candidato_mayores_votos, candidato_menores_votos, edad_candidato_menores_votos, promedio_edades, total_votos)

        print(mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
