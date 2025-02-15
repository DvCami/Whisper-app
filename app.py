import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import math
from tkinter import ttk
import ttkbootstrap as ttk
from tkinterdnd2 import TkinterDnD, DND_FILES



"""
    Se necesita un boton de play centrado, que luego a su derecha este la linea de reproduccion y despues al final este los tiempos
    ademas de que abajo este el boton para transcribir y que cambie a un boton de carga hasta que termine de procesar el audio, luego en ese momento debe
    1- verificar si el audio es compatible o si lo que pasa es un audio
    2- Comprimir el audio para poder manipularlo mejor
    3-QUitar los momentos de silencio
    4- Utilizar wisper
    6-pasar el archivo transcrito
    7-Buscar librerias que ayuden a la depuracion y salida del codigo
    
"""





# Colores 
primary_color = "#424242"
secundary_color = "#757575"


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

def rotate_point(x, y, cx, cy, angle):
    """ Rota un punto (x, y) alrededor de (cx, cy) en un ángulo dado (en grados). """
    rad = math.radians(angle)  # Convertir grados a radianes
    x_new = cx + (x - cx) * math.cos(rad) - (y - cy) * math.sin(rad)
    y_new = cy + (x - cx) * math.sin(rad) + (y - cy) * math.cos(rad)
    return x_new, y_new

def draw_rounded_triangle(canvas, size,   angle=0,  fill_color="black", bg = "lightblue", padx = 0, pady = 0 ):
    """
    Dibuja un triángulo con bordes redondeados en un canvas.
    x, y -> Coordenadas del centro del triángulo.
    size -> Tamaño del triángulo.
    radius -> Radio de las esquinas redondeadas.
    angle -> Ángulo de rotación en grados.
    fill_color -> Color del triángulo.
    """
    

    # Centro de rotación
    cx, cy = size // 2, size // 2

    # Puntos iniciales (sin rotación)
    p1 = (cx, cy - size // 2)  # Punto superior
    p2 = (cx - size // 2, cy + size // 2)  # Punto inferior izquierdo
    p3 = (cx + size // 2, cy + size // 2)  # Punto inferior derecho

    # Aplicar rotación a cada punto
    p1 = rotate_point(*p1, cx, cy, angle)
    p2 = rotate_point(*p2, cx, cy, angle)
    p3 = rotate_point(*p3, cx, cy, angle)
    
    p1 = (p1[0] + padx, p1[1] + pady)
    p2 = (p2[0] + padx, p2[1] + pady)
    p3 = (p3[0] + padx, p3[1] + pady)

    # Dibujar triángulo base
    canvas.create_polygon(p1, p2, p3, fill=fill_color, outline=fill_color, smooth=True)


    return canvas 


def draw_pause_icon(canvas, x, y, height, bar_width, fill_color="black", padx = 10, pady = 10):
    """
    Dibuja un ícono de pausa en un Canvas con padding.

    Parámetros:
      - canvas: El objeto Canvas donde se dibujará.
      - x, y: Coordenadas de la esquina superior izquierda del área donde se dibujará el ícono.
      - height: Altura total del ícono.
      - bar_width: Ancho de cada barra de pausa.
      - fill_color: Color de las barras.
      - padding: Espaciado alrededor del icono de pausa.
    """
    gap = bar_width  # Espacio entre las barras

    # Aplicar padding a las coordenadas
    x += padx
    y += pady
    padx + pady
    height + 2 * pady    # Reducir la altura total por el padding

    # Nuevas coordenadas con padding
    x1 = x + gap
    x2 = x1 + bar_width
    y1, y2 = y, y + height

    # Dibujar la primera barra con padding
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline=fill_color)

    # Dibujar la segunda barra con padding
    x3 = x2 + gap
    x4 = x3 + bar_width
    canvas.create_rectangle(x3, y1, x4, y2, fill=fill_color, outline=fill_color)
    
    
    
    

app = ttk.Window(themename="darkly")


# Crear la ventana

app.title("Transcripcion beta, DvCami")
app.geometry("1300x700+256+256")
app.resizable(False,False)


# Cuerpo de la ventana

# Configuracion de la ventana
app.grid_columnconfigure(1, weight = 1) 
app.grid_columnconfigure(2, weight = 1)
app.grid_columnconfigure(3, weight = 1)
app.grid_rowconfigure(1, weight = 1)
app.grid_rowconfigure(2, weight = 1)
app.grid_rowconfigure(3, weight = 1)


# Frame del drop
frame_drop = create_rounded_frame(master = app, width=300, height= 250, bg=primary_color)
frame_drop.grid(row= 0, column=4, sticky = 'nsew', padx=10, pady=10) # Posicion del frame

frame_drop.grid_propagate(False) # Evitar que el frame se expanda

# Frame para elegir

frame_chose = create_rounded_frame(master = app, width=300, height= 410, bg = primary_color)
frame_chose.grid(row = 1, column = 4,rowspan=2, sticky="nsew", padx = 10, pady = 10) # Posicion del frame model

frame_chose.grid_propagate(False) # Evitar que el frame se expanda 


# Frame de UI audio

frame_audio = create_rounded_frame(master= app, width= 950, height= 200, bg=secundary_color)
frame_audio.grid(row = 0,columnspan = 3, column = 1, sticky="nsew", padx=10, pady = 10 )

# Posicionar el boton play

boton_play = draw_rounded_triangle(canvas = frame_audio, size=60, angle=90, bg=secundary_color, fill_color= primary_color, padx= 105.5, pady= 70)

boton_pause = draw_pause_icon(frame_audio, 20, 20, 40, 10, padx= 100, pady = 70)


app.mainloop()

