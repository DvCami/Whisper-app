import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from tkinterdnd2 import TkinterDnD, DND_FILES

# Colores 
backgrond = "#424242"

#Funciones

# Función para crear un frame con bordes redondeados
def create_rounded_frame(master, width, height, radius=20, bg="lightblue"):
    canvas = tk.Canvas(master, width=width, height=height, bd=0, highlightthickness=0)
    canvas.create_oval(0, 0, radius*2, radius*2, fill=bg, outline=bg)  # Esquina superior izquierda
    canvas.create_oval(width-radius*2, 0, width, radius*2, fill=bg, outline=bg)  # Esquina superior derecha
    canvas.create_oval(0, height-radius*2, radius*2, height, fill=bg, outline=bg)  # Esquina inferior izquierda
    canvas.create_oval(width-radius*2, height-radius*2, width, height, fill=bg, outline=bg)  # Esquina inferior derecha
    canvas.create_rectangle(radius, 0, width-radius, height, fill=bg, outline=bg)  # Lado derecho
    canvas.create_rectangle(0, radius, width, height-radius, fill=bg, outline=bg)  # Lado izquierdo
    canvas.grid(row=0, column=0, padx=10, pady=10)
    return canvas

app = ttk.Window(themename="darkly")


# Crear la ventana

app.title("Transcripcion beta, DvCami")
app.geometry("1300x700+256+256")
app.resizable(False,False)

# Cuerpo de la ventana

# Configuracion de la ventana
app.grid_columnconfigure(1, weight = 1) # Configuracion de la columna de la izquierda
app.grid_columnconfigure(2, weight = 1)# Configuracion de la columna de la derecha
app.grid_columnconfigure(3, weight = 1)
app.grid_rowconfigure(1, weight = 1)
app.grid_rowconfigure(2, weight = 1)
app.grid_rowconfigure(3, weight = 1)


# Frame del drop
frame_drop = create_rounded_frame(master = app, width=300, height= 250, bg=backgrond)
frame_drop.grid(row= 0, column=4, sticky = 'nsew', padx=10, pady=10) # Posicion del frame

frame_drop.grid_propagate(False) #Evitar que el frame se expanda

# Frame para elegior

frame_chose = create_rounded_frame(master = app, width=300, height= 410, bg = backgrond)
frame_chose.grid(row = 1, column = 4,rowspan=2, sticky="nsew", padx = 10, pady = 10) # Posicion del frame model

frame_chose.grid_propagate(False)

app.mainloop()

