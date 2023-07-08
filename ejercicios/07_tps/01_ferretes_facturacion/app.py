import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	Ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
        
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        producto_uno = int(self.txt_importe_1.get())
        producto_dos = int(self.txt_importe_2.get())
        producto_tres = int(self.txt_importe_3.get())

        resultado_total = producto_uno + producto_dos + producto_tres

        mensaje = "El total a pagar por los tres productos es ${0}".format(resultado_total)
        alert("Total a pagar", mensaje)

    def btn_promedio_on_click(self):
        producto_uno = int(self.txt_importe_1.get())
        producto_dos = int(self.txt_importe_2.get())
        producto_tres = int(self.txt_importe_3.get())

        resultado_promedio = (producto_uno + producto_dos + producto_tres) / 3

        mensaje = "El promedio de precio de los tres productos es ${0}".format(resultado_promedio)
        alert("Promedio de Productos", mensaje)

    def btn_total_iva_on_click(self):
        producto_uno = int(self.txt_importe_1.get())
        producto_dos = int(self.txt_importe_2.get())
        producto_tres = int(self.txt_importe_3.get())

        resultado_iva = (producto_uno + producto_dos + producto_tres) * 1.21

        mensaje = "El total a pagar por los tres productos + IVA (21%) es ${0}".format(resultado_iva)
        alert("Total a pagar con IVA", mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()