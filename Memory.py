from random import *
from turtle import *
from freegames import path

car = path('car.gif')

# Lista de colores (duplicados para hacer pares)
color_names = [
    'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan',
    'brown', 'magenta', 'lime', 'indigo', 'violet', 'gold', 'silver', 'teal',
    'navy', 'maroon', 'olive', 'coral', 'turquoise', 'salmon', 'plum', 'beige',
    'lavender', 'khaki', 'chartreuse', 'crimson', 'peru', 'orchid', 'azure', 'tan',
] 

# Asegurar que haya 64 colores (duplicados y mezclados)
tiles = color_names * 2
shuffle(tiles)
# Definir el estado del juego con una marca inicial en None y un contador de taps
state = {'mark': None, 'taps': 0}
hide = [True] * 64

def square(x, y): # Función para dibujar un cuadrado blanco con borde negro en la posición (x, y)
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y): # Función para convertir el índice de la ficha a coordenadas (x, y)
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y): # Función que maneja los clics en el tablero
    spot = index(x, y) # Obtener el índice de la ficha seleccionada
    mark = state['mark']  # Obtener la ficha previamente seleccionada
    state['taps'] += 1  # Incrementar el contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:  # Si no hay ficha seleccionada, si se hace clic en la misma ficha, o si las fichas no coinciden
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def all_revealed(): # Función para verificar si todas las fichas han sido reveladas
    return all(not h for h in hide)

def draw(): # Función para dibujar la imagen de fondo y las fichas
    clear()
    goto(0, 0)
    shape(car)
    stamp()
 
    for count in range(64): # Dibujar los cuadros de las fichas ocultas
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 25)
        dot(40, tiles[mark])  # Mostrar un punto grande del color

    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 16, 'bold'))

    if all_revealed():
        goto(-100, 0)
        write('GANASTE!', font=('Arial', 30, 'bold'))
        update()
        return

    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
