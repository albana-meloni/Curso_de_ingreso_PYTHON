import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
    Todas las lámparas están  al mismo precio de $800 pesos final.
    A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
    B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
    C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
    D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
    E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        mensaje = ""

        lamparita = 800
        total = lamparita * cantidad
        descuento = 0

        # IF - MATCH -----------------------------------------------------------------------------------
        if cantidad > 5:
            descuento = 50
        elif cantidad == 5:
            match marca:
                case "ArgentinaLuz":
                    descuento = 40
                case _:
                    descuento = 30
        elif cantidad == 4:
            match marca:
                case "ArgentinaLuz" | "FelipeLamparas":
                    descuento = 25
                case _:
                    descuento = 20
        elif cantidad == 3:
            match marca:
                case "ArgentinaLuz":
                    descuento = 15
                case "FelipeLamparas":
                    descuento = 10
                case _:
                    descuento = 5



        # MATCH - IF -----------------------------------------------------------------------------------
        match cantidad:
            case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                descuento = 50
            case 5:
                if marca == "ArgentinaLuz":
                    descuento = 40
                else:
                    descuento = 30
            case 4:
                if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                    descuento = 25
                else:
                    descuento = 20
            case 3:
                if marca == "ArgentinaLuz":
                    descuento = 15
                elif marca == "FelipeLamparas":
                    descuento = 10
                else:
                    descuento = 5



        # MATCH - MATCH  -----------------------------------------------------------------------------------
        match cantidad:
            case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                descuento = 50
            case 5:
                match marca:
                    case "ArgentinaLuz":
                        descuento = 40
                    case _:
                        descuento = 30
            case 4:
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        descuento = 25
                    case _:
                        descuento = 20
            case 3:
                match marca:
                    case "ArgentinaLuz":
                        descuento = 15
                    case "FelipeLamparas":
                        descuento = 10
                    case _:
                        descuento = 5



        # IF - IF -----------------------------------------------------------------------------------
        if cantidad > 5:
            descuento = 50
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                descuento = 40
            else:
                descuento = 30
        elif cantidad == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                descuento = 25
            else: 
                descuento = 20
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                descuento = 15
            elif marca == "FelipeLamparas":
                descuento = 10
            else:
                descuento = 5
        



        # SALIDAS -----------------------------------------------------------------------------------
        total_descuento = total - (total * descuento/100)
        mensaje = "Al comprar {0} lamparitas de bajo consumo marca {1} tiene un descuento del {2}% y el total a pagar es: ${3}".format(cantidad, marca, descuento, total_descuento)

        if total_descuento >= 4000:
            total_descuento_extra = total_descuento - (total_descuento * 0.05)
            mensaje = mensaje + "\n Como el importe supera los $4.000 le ofrecemos un 5% de descuento adicional \nEl total final a pagar es: ${0}".format(total_descuento_extra)

        alert("Factura X", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()