import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Axel
apellido: Cannavina
 
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero_positivo = 0
        numero_negativo = 1

        while True:
            numero = prompt("Numero ingresado", "Ingrese un número (Presione el boton cancelar para finalizar) ")

            if numero == None:
                break
            if numero.isalpha():
                alert("Error!", "Caracter invalido. Intente nuevamente.")
            else:
                # numero = int(numero) Si uso esto no funciona porque isdigit no pasa a negativos, tengo que usar un lstrip
                if numero.isdigit() or int(numero) > 0:     
                    numero = int(numero)
                    numero_positivo += numero
                elif numero.isdigit() or int(numero) < 0:
                    numero_negativo *= int(numero)


        self.txt_suma_acumulada.delete(0, "end")
        self.txt_suma_acumulada.insert("end", numero_positivo)
        self.txt_producto.delete(0, "end")
        self.txt_producto.insert("end", numero_negativo)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
