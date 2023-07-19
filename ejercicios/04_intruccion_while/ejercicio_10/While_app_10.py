import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Axel
apellido: Cannavina
 
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero_positivo = 0
        numero_negativo = 0
        contador_positivo = 0
        contador_negativo = 0
        ceros = 0

        while True:
            numero = prompt("Numero ingresado", "Ingrese un número (Presione el boton cancelar para finalizar) ")

            if numero == None:
                break
            if numero.isalpha() or numero == "":
                alert("Error!", "Caracter invalido. Intente nuevamente.")
            else:
                numero = int(numero)        
                if numero > 0:     
                    numero_positivo += numero
                    contador_positivo += 1
                elif numero < 0:
                    numero_negativo -= numero
                    contador_negativo += 1
        
        for digit in str(numero_positivo):
            if digit == "0":
                ceros += 1
        for digit in str(numero_negativo):
            if digit == "0":
                ceros += 1
        
        diferencia = abs(contador_positivo - contador_negativo)
    
        alert("UTN", f"Suma acumulada de positivos: {numero_positivo}\nSuma acumulada de negativos: {-(numero_negativo)} \n"
              f"Numeros negativos ingresados: {contador_negativo} \nNumeros positivos ingresados: {contador_positivo} \n"
              f"Cantidad de ceros de ambos numeros: {ceros} \nDiferencia de numeros ingresados: {diferencia}")
        
             # ! puse un "-" aca ya que isdigit() no toma negativos, y se simplificaba mucho el codigo de esa manera, si no era con un lstrip
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
