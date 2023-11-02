import tkinter as tk


class Instrucciones:
    # Crear una ventana
    ventana = tk.Tk()
    ventana.title("Instrucciones")

    # configuracion ventana
    ancho = 750
    alto = 480
    ventana.geometry(f"{ancho}x{alto}")
    ventana.configure(bg="#7ED957")

    # widget Label para mostrar las instrucciones predefinidas
    instrucciones_predefinidas = """
    
    
    
    Bienvenido al juego de adivinanza matemática:
    
    El objetivo es adivinar la secuencia matemática en un número limitado de intentos. 
    La secuencia consta de números entre 0 y 9, operaciones matemáticas básicas y el signo de igualdad.",
    Puedes intentar adivinar la secuencia escribiendo una expresión matemática válida.
    Por ejemplo, si la secuencia es '2 + 3 = 5', puedes intentar con '2+3=5'.
    El juego te dará pistas sobre cuántos números y operadores has adivinado correctamente.
    ¡Diviértete y buena suerte!
    
    NORMAS:
    
     * Cada suposición es un cálculo.
     * Puedes usar 0 1 2 3 4 5 6 7 8 9 + - * / = 
     * Debe contener un = 
     * Sólo debe tener un número a la derecha de =, no otro cálculo. 
     * Se aplica el orden estándar de operaciones, 
        así que calcule * y / 
        antes de + y - 
        POR EJEMPLO: 3 + 2 * 5 = 13 no 25.
     * Si la respuesta que buscamos es 10+20 = 30, entonces tambien se acepta 20+10=30
    
    
    
    """
    # Configurar la fuente y el ancho del Label
    font_style = ("Arial", 11)
    font_style_title = ("Arial", 16)
    etiqueta_instrucciones = tk.Label(text=instrucciones_predefinidas, justify="left", font=font_style)
    etiqueta_instrucciones.pack()

    titulo = "¿Como Jugar?"
    etiqueta_titulo = tk.Label(ventana, text=titulo, font=font_style_title, bg="white")
    etiqueta_titulo.place(relx=0.5, rely=0.09, anchor="center")

    ventana.mainloop()

