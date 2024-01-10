import tkinter as tk
from tkinter import Entry, Label, Button
import random
import tkinter.messagebox

class GeneradorContrasenaApp:
    def __init__(self, master):
        self.master = master
        master.title("Generador de Contraseñas")

        # Establece el tamaño inicial de la ventana
        master.geometry("500x500")

        self.label = Label(master, text="Longitud de la Contraseña:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.generar_button = Button(master, text="Generar Contraseña", command=self.generar_contrasena)
        self.generar_button.pack()

        # Etiqueta para mostrar la contraseña, con ancho ajustable
        self.resultado_label = Label(master, text="", wraplength=480)
        self.resultado_label.pack()

        self.copiar_button = Button(master, text="Copiar al Portapapeles", command=self.copiar_al_portapapeles)
        self.copiar_button.pack()

    def generar_contrasena(self):
        try:
            longitud = int(self.entry.get())
            caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
            contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
            self.resultado_label.config(text=f"Contraseña generada: {contrasena}")
            self.contrasena_generada = contrasena
        except ValueError:
            self.resultado_label.config(text="Error: Ingresa un número válido")

    def copiar_al_portapapeles(self):
        try:
            self.master.clipboard_clear()
            self.master.clipboard_append(self.contrasena_generada)
            self.master.update()
            tkinter.messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles.")
        except AttributeError:
            tkinter.messagebox.showerror("Error", "Primero genera una contraseña.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorContrasenaApp(root)
    root.mainloop()
