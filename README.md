# Alien Invasion

Alien Invasion es un juego desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es controlar una nave espacial para defenderse de oleadas de alienígenas mientras acumulas puntos y evitas perder todas tus vidas.

## Características

- **Nave controlable**: Mueve la nave hacia la izquierda o derecha y dispara balas normales o especiales.
- **Oleadas de alienígenas**: Los alienígenas descienden en filas y columnas, aumentando la dificultad a medida que avanzas.
- **Sistema de puntuación**: Gana puntos al eliminar alienígenas.
- **Vidas limitadas**: Pierdes una vida si un alienígena colisiona con tu nave o alcanza la parte inferior de la pantalla.
- **Balas especiales**: Usa balas especiales para eliminar múltiples alienígenas a la vez.

## Requisitos

- Python 3.8 o superior
- Biblioteca Pygame

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/alien_invasion.git
   cd alien_invasion

2. Crea un entorno virtual e instale las dependencias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # En Windows: venv\Scripts\activate
   pip install pygame
   ```
3. Ejecuta el juego:
   ```bash
   python alien_invasion.py
   ```
## Cómo jugar
1. Usa las teclas de flecha para mover la nave espacial.
2. Presiona la barra espaciadora para disparar balas normales.
3. Presiona la tecla 'Shift Izquierda' para disparar balas especiales (limitadas).
4. Elimina a los alienígenas antes de que lleguen a la parte inferior de la pantalla.
5. Evita que los alienígenas colisionen con tu nave para no perder vidas.
6. Avanza a través de los niveles eliminando todas las oleadas de alienígenas.

## Archivos principales
- `alien_invasion.py`: Archivo principal que inicia el juego.
- `settings.py`: Configuraciones del juego.
- `ship.py`: Clase que maneja la nave espacial.
- `alien.py`: Clase que maneja los alienígenas.
- `bullet.py`: Clase que maneja las balas disparadas por la nave.
- `game_stats.py`: Clase que maneja las estadísticas del juego.