import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk
import math

# nombre: Axel
# apellido: Cannavina

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour ", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
   
    def btn_mostrar_on_click(self):

        # varibles y validaciones

        nombre = prompt("Ingrese sus datos", "Ingrese su nombre y apellido.")
        while nombre.isdigit() or len(nombre) < 3 :
            nombre  = prompt("Ingrese sus datos", "Ingrese un nombre y apellido valido.")
        
        edad = prompt("Ingrese sus datos", "Ingrese su edad.")
        while edad.isalpha() or edad == "":
            edad = (prompt("Ingrese sus datos", "Ingrese una edad valida."))
        edad = int(edad)

        genero = prompt("Ingrese sus datos", "Ingrese su genero. (M/F/Otro)")
        while genero.isdigit() or genero not in ["M", "F", "m", "f", "otro", "Otro"] : #preferi por usar este metodo, en el curso se habia dicho poder usar chatgpt en caso de entender los conceptos etcetc
            genero  = prompt("Ingrese sus datos", "Ingrese un genero valido.")

        altura = prompt("Ingrese sus datos", "Ingrese su altura (en centimetros)")
        while altura.isalpha() or altura == "":
            altura = (prompt("Ingrese sus datos", "Ingrese una altura valida."))
        altura = int(altura)

            #if altura

        if altura < 140:
            altura_ingresada = "baja"
        elif altura < 170:
            altura_ingresada = "media"
        elif altura < 190:
            altura_ingresada = "alta"
        else:
            altura_ingresada = "muy alta"

            # excursiones
        cantidad_exc = prompt("Excursiones", "Ingrese una cantidad de excursiones")
        while not cantidad_exc or cantidad_exc.isalpha() or cantidad_exc == "" :
            cantidad_exc = (prompt("Ingrese sus datos", "Ingrese una cantidad valida."))
        cantidad_exc = int(cantidad_exc)

        contador_exc = 0

        precio_barato = None
        tipo_mas_barato = ""
        precio_caro = None
        tipo_mas_caro = ""
        precio_promedio = 0

        while contador_exc < cantidad_exc:

            importe = prompt("Ingrese sus datos", "Ingrese su importe")
            while importe.isalpha() or importe == "":
                importe = (prompt("Ingrese sus datos", "Ingrese un importe valido."))
            importe = int(importe)

            tipo = prompt("Ingrese sus datos", "Ingrese el tipo de excursion (caminata/vehiculo)")
            while tipo != "caminata" or tipo != "vehiculo":
                tipo = (prompt("Ingrese sus datos", "Ingrese un tipo valido."))

            if precio_barato == None or precio_barato > importe:
                precio_barato = importe
                tipo_mas_barato = tipo

            if precio_caro == None or precio_caro > importe:
                precio_caro = importe
                tipo_mas_caro = tipo

                
        mensaje = f"Usted es {nombre}, tiene {str(edad)} años, y su genero es {genero} \n Su estatura es {altura_ingresada} " 
        alert("Datos", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
