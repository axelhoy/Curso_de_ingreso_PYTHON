import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Axel
apellido: Cannavina
 
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        tarifa = 15000
        destinos = self.combobox_destino.get()
        estaciones = self.combobox_estaciones.get()
       
        match(estaciones, destinos):                                              # otra forma!
            case("Invierno", "Bariloche"):
                tarifa = tarifa*1.2
            case("Invierno", ('Cataratas' | 'Cordoba')):
                tarifa = tarifa*.9
            case("Invierno", 'Mar del plata'):
                tarifa = tarifa*.8
            case("Verano", "Bariloche"):
                tarifa = tarifa*.8
            case("Verano", ('Cataratas' | 'Cordoba')):
                tarifa = tarifa*1.1
            case("Verano", 'Mar del plata'):
                tarifa = tarifa*1.2
            case(("Otoño" | "Primavera"), "Cordoba"):
                tarifa = tarifa
            case _:
                tarifa = tarifa*1.1

        alert("Total del viaje", f"Su precio final es de {tarifa}$")

        

        # match(estaciones, destinos):                                                  # otra forma!
        #     case("Invierno", "Bariloche"):
        #         desc_au_mento = 20
        #         tarifa = abs(tarifa + (tarifa*desc_au_mento/100))
        #     case("Invierno", ('Cataratas' | 'Cordoba')):
        #         desc_au_mento = 10
        #         tarifa = abs(tarifa - (tarifa*desc_au_mento/100))
        #     case("Invierno", 'Mar del plata'):
        #         desc_au_mento = 20
        #         tarifa = abs(tarifa - (tarifa*desc_au_mento/100))
        #     case("Verano", "Bariloche"):
        #         desc_au_mento = 10
        #         tarifa = abs(tarifa - (tarifa*desc_au_mento/100))
        #     case("Verano", ('Cataratas' | 'Cordoba')):
        #         desc_au_mento = 10
        #         tarifa = abs(tarifa + (tarifa*desc_au_mento/100))
        #     case("Verano", 'Mar del plata'):
        #         desc_au_mento = 20
        #         tarifa = abs(tarifa + (tarifa*desc_au_mento/100))
        #     case(("Otoño" | "Primavera"), "Cordoba"):
        #         tarifa = tarifa
        #     case _:
        #         tarifa = tarifa*1.1

        # alert("Total del viaje", f"Su precio final es de {tarifa}$")
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()