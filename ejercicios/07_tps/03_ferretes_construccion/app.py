import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios a la hora de realizar un alambrado perimetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (F)Poste Quebracho Fino de 2.2 mts
    (V)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)      
        self.btn_calcular = customtkinter.CTkButton(master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        

    def btn_calcular_on_click(self):
        largo_guardado = float(self.txt_largo.get())
        ancho_guardado = float(self.txt_ancho.get())

        # PUNTO A
        area_terreno = largo_guardado * ancho_guardado
        perimetro_terreno = (largo_guardado + ancho_guardado)*2

        # PUNTO B
        cantidad_quebracho_grueso = (perimetro_terreno // 250) + 4

        # PUNTO C
        cantidad_quebracho_fino = (perimetro_terreno // 12) - cantidad_quebracho_grueso

        # PUNTO D
        cantidad_varillas = (perimetro_terreno // 2) - cantidad_quebracho_fino

        # PUNTO E
        cantidad_alambre = perimetro_terreno * 7

        mensaje_final = "El terreno tiene un total de {0}m2 y {1} metros de perímetro. Por lo tanto, se necesitarán: \n{2} postes de quebracho grueso \n{3} postes de quebracho fino \n{4} varillas \n{5}mts de alambre 17/15 considerando 7 hilos".format(area_terreno, perimetro_terreno, cantidad_quebracho_grueso, cantidad_quebracho_fino, cantidad_varillas, cantidad_alambre)

        alert("Lista de Materiales ;)", mensaje_final)

if __name__ == "__main__":
    app = App()
    app.mainloop()