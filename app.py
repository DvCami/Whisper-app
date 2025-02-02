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

frame_drop = tk.Frame(master = app, width=300, height= 300, padx=10, pady= 10)
frame_drop.pack()
frame_drop.config(background = "lightgreen") # Fondo del Frame en blanco

app.mainloop()

