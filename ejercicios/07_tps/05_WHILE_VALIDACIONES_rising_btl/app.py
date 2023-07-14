import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Albana
apellido: Meloni

Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        self.txt_apellido.delete(0, "end")
        self.txt_edad.delete(0, "end")
        self.txt_legajo.delete(0, "end")

        # validando apellido
        apellido_validado = False
        while apellido_validado != True:
            apellido_ingresado = prompt("Datos", "Ingrese su apellido, por favor")
            if apellido_ingresado == None or apellido_ingresado.isdigit() or apellido_ingresado == "":
                alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
            else:
                apellido_validado = True
                self.txt_apellido.insert(0, apellido_ingresado)

        # validando edad
        edad_validada = False
        while edad_validada != True:
            edad_ingresada = prompt("Datos", "Ingrese su edad, por favor")
            if edad_ingresada == None or not(edad_ingresada.isdigit()) or edad_ingresada == "":
                alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
            else:
                edad_ingresada = int(edad_ingresada)
                if edad_ingresada > 17 and edad_ingresada < 91:
                    edad_validada = True
                    self.txt_edad.insert(0, edad_ingresada)
                else:
                    alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
                    edad_validada = False

        # validando estado civil
        estado_civil_validado = False
        while estado_civil_validado != True:
            estado_civil_ingresado = prompt("Datos", "Ingrese su estado civil, escriba 1=Soltero/a, 2=Casado/a, 3=Divorciado/a o 4=Viudo/a según corresponda")
            if estado_civil_ingresado == None or not(estado_civil_ingresado.isdigit()) or estado_civil_ingresado == "":
                alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
            else:
                match estado_civil_ingresado:
                    case "1":
                        estado_civil_validado = True
                        self.combobox_tipo.set("Soltero/a")
                    case "2":
                        estado_civil_validado = True
                        self.combobox_tipo.set("Casado/a")
                    case "3":
                        estado_civil_validado = True
                        self.combobox_tipo.set("Divorciado/a")
                    case "4":
                        estado_civil_validado = True
                        self.combobox_tipo.set("Viudo/a")
                    case _:
                        alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
                        estado_civil_validado = False

        # validanado legajo
        legajo_validado = False
        while legajo_validado != True:
            legajo_ingresado = prompt("Datos", "Ingrese su número de legajo de 4 cifras, por favor")
            if legajo_ingresado == None or not(legajo_ingresado.isdigit()) or legajo_ingresado == "":
                alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
            else:
                primero_digito = legajo_ingresado[0]
                if len(legajo_ingresado) == 4 and primero_digito != "0":
                    legajo_validado = True
                    self.txt_legajo.insert(0, legajo_ingresado)
                else:
                    alert("WASTED", "Error 22. Debe ingresar un valor correcto >:(")
                    legajo_validado = False

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
