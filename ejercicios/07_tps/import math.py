import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk


class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour 🚂", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)


        self.label0 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label0.grid(row=1, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=1, column=1)
       
        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=2, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=2, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Genero")
        self.label2.grid(row=3, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["Masculino", "Femenino", "Otro", "Prefiero no decirlo", "Avión"])
        self.combobox_tipo.grid(row=3, column=1, padx=20, pady=10)
                
        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        n_apellido = self.txt_apellido.get()
        edad = int(self.txt_edad.get())
        genero = self.combobox_tipo.get()

        if isinstance(edad, str):
            alert("Atencion!", "Ingrese una edad valida!")
        else:
            alert(title="Alert", message="\nNombre: " + str(n_apellido) + " \nEdad: " + str(edad) + "\nGenero: " + str(genero))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()