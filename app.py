import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from tkinterdnd2 import TkinterDnD, DND_FILES

app = ttk.Window(themename="darkly")


# Crear la ventana

app.title("Transcripcion beta, DvCami")
app.geometry("1300x700+256+256")
app.resizable(False,False)

# Cuerpo de la ventana

# Configuracion de la ventana
app.grid_columnconfigure(0, weight = 1) # Configuracion de la columna de la izquierda
app.grid_columnconfigure(1, weight = 3) # Configuracion de la columna de la derecha

# Configuracion del frame
style = ttk.Style() # Creacion de estilo para el frame
style.configure("TFrame",
                background="white",
                relief = 'solid',
                borderwidth = 2,
                borderradius = 15) # Configuracion del estilo Frame_drop

# Frame del drop
frame_drop = ttk.Frame(master = app, width=300, height= 300, style = 'TFrame')
frame_drop.grid(row= 0, column=3, sticky = 'nw', padx=10, pady=10) # Posicion del frame

frame_drop.grid_propagate(False) #Evitar que el frame se expanda

app.mainloop()

