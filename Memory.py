from random import *  # Importar todas las funciones del módulo random
from turtle import *  # Importar todas las funciones del módulo turtle
from freegames import path  # Importar la función path del módulo freegames

# Cargar la imagen del auto
car = path('car.gif')

# Crear una lista de 32 pares de números (del 0 al 31) para las fichas
tiles = list(range(32)) * 2  # Duplicamos los números para formar pares

# Definir el estado del juego con una marca inicial en None y un contador de taps
state = {'mark': None, 'taps': 0}  

# Lista de 64 elementos booleanos para ocultar o mostrar las fichas
hide = [True] * 64  

# Función para dibujar un cuadrado blanco con borde negro en la posición (x, y)
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Función para convertir coordenadas (x, y) a un índice de la lista de fichas
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Función para convertir el índice de la ficha a coordenadas (x, y)
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Función que maneja los clics en el tablero
def tap(x, y):
    spot = index(x, y)  # Obtener el índice de la ficha seleccionada
    mark = state['mark']  # Obtener la ficha previamente seleccionada
    state['taps'] += 1  # Incrementar el contador de taps

    # Si no hay ficha seleccionada, si se hace clic en la misma ficha, o si las fichas no coinciden
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot  # Marcar la ficha actual
    else:
        hide[spot] = False  # Revelar la ficha actual
        hide[mark] = False  # Revelar la ficha anterior
        state['mark'] = None  # Resetear la marca

# Función para verificar si todas las fichas han sido reveladas
def all_revealed():
    return all(not h for h in hide)

# Función para dibujar la imagen de fondo y las fichas
def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibujar los cuadros de las fichas ocultas
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    
    mark = state['mark']

    # Dibujar el número en la ficha seleccionada
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        num = str(tiles[mark])  # Convertir el número en string
        if len(num) == 1:
            goto(x + 25, y + 3)  # Ajuste para un solo dígito
            font_size = 30
        else:
            goto(x + 25, y + 5)  # Ajuste para dos dígitos
            font_size = 24
        color('black')
        write(num, font=('Arial', font_size, 'bold'), align='center')

    # Mostrar el número de taps
    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 16, 'bold'))
    
    # Verificar si el juego ha terminado
    if all_revealed():
        goto(-100, 0)
        write('GANASTE!', font=('Arial', 30, 'bold'))
        update()
        return

    update()
    ontimer(draw, 100)  # Redibujar cada 100 ms

shuffle(tiles)  # Mezclar las fichas
setup(420, 420, 370, 0)  # Configurar la ventana del juego
addshape(car)  # Agregar la imagen del auto como una forma
hideturtle()
tracer(False)  # Desactivar animación automática para optimización
onscreenclick(tap)  # Detectar clics en pantalla y ejecutar tap

# Iniciar el juego
draw()
done()
