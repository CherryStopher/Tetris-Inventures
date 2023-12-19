# Tetris

## Introducción

Tetris es un juego de rompecabezas diseñado por Aleksei Pázhitnov en 1984. El juego consiste en una cuadrícula en la que caen tetrominós, donde cada pieza está compuesta de cuatro bloques. 

El objetivo del juego es utilizar estas piezas para crear líneas completas en la cuadrícula, las cuales se eliminan cuando esto sucede. 

El jugador puede mover las piezas, rotarlas, almacenarlas y dejarlas caer más rápido. El juego termina cuando las piezas se apilan hasta llegar a la parte superior de la cuadrícula.

## Instrucciones para jugar

Se debe ejecutar los siguientes comandos en la terminal para poder instalar las dependencias y ejecutar el juego:

Para Linux y Mac:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Para Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Para salir del entorno virtual, ejecutar el siguiente comando:

Para Linux, Mac y Windows:


```bash
deactivate
```

## Controles

- Flecha izquierda: Mover pieza a la izquierda
- Flecha derecha: Mover pieza a la derecha
- Flecha abajo: Soft drop
- Espacio: Hard drop
- Flecha arriba: Rotar pieza en sentido horario
- Z o LCRTL: Rotar pieza en sentido antihorario
- C o LShift o RShift: Guardar pieza

## Funcionalidades

El juego está en el modo Maratón, donde el objetivo es sobrevivir el mayor tiempo posible. Para subir de nivel se debe eliminar 10 líneas, lo cual aumenta la velocidad del juego.

El juego cuenta con un sistema de puntaje, donde se obtienen puntos por cada línea eliminada. Además, se obtienen puntos por cada bloque que cae, dependiendo de la altura a la que cae.

Los puntajes se calculan de la siguiente manera:

- 1 línea: (100 * nivel) puntos
- 2 líneas: (300 * nivel) puntos
- 3 líneas: (500 * nivel) puntos
- 4 líneas: (800 * nivel) puntos

- Completar 1 fila con perfect clear: (800 * nivel) puntos
- Completar 2 filas con perfect clear: (1200 * nivel) puntos
- Completar 3 filas con perfect clear: (1800 * nivel) puntos
- Completar 4 filas con perfect clear: (2000 * nivel) puntos

- Hacer un soft drop: 1 punto 
- Hacer un hard drop: (2 * altura) puntos

- Combo: (50 * nivel * combo) puntos



Una vez se haya perdido la partida, esta puede ser reiniciada pulsando la tecla R.

## Información extra

En la interfaz de la pantalla se muestra la pieza en retención, las 3 siguientes piezas, el nivel, el puntaje, el puntaje máximo, el número de líneas eliminadas en el nivel actual y el número de combo cuando este es 1 o mayor.

Las piezas aparecen en la parte superior de la cuadrícula y esta se desplaza hacia arriba cuando hay un bloque interrumpiendo el punto de aparición. 


El juego termina cuando una pieza (o parte de ella) se encuentra por encima de la cuadrícula.



