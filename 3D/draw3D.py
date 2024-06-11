import os
import cv2
import numpy as np
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reconstrucción 2D")

# Carpeta donde se encuentran los archivos
folder = "3D/data_saved"

# Cargar los datos de profundidad
depth_data_path = os.path.join(folder, "depth_data.npy")
depth_data = np.load(depth_data_path)

# Ajustar los datos de profundidad para que coincidan con las dimensiones de la imagen de bordes escalada
depth_data = cv2.resize(depth_data, (width, height))

# Calcular el mínimo y máximo valor de profundidad
min_depth = np.min(depth_data)
max_depth = np.max(depth_data)

# Cargar la imagen de bordes guardada
edges_path = os.path.join(folder, "edges_detected.png")
edges = cv2.imread(edges_path, cv2.IMREAD_GRAYSCALE)

if edges is None:
    print(f"Error: No se pudo cargar la imagen '{edges_path}'.")
    sys.exit()

# Función para dibujar los bordes en Pygame con efecto de profundidad
def draw_edges_with_depth(surface, edges, depth_data, min_depth, max_depth):
    height, width = edges.shape

    for y in range(height):
        for x in range(width):
            if edges[y, x] != 0:  # Si es un borde
                # Obtener la profundidad del píxel
                depth = depth_data[y, x]

                # Interpolar entre verde y rojo basado en la profundidad
                interpolation = (depth - min_depth) / (max_depth - min_depth)
                green = int(255 * (1 - interpolation))
                red = int(255 * interpolation)
                color = (0, green, red)

                surface.set_at((x, y), color)  # Establecer el color en el píxel

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar los bordes en la pantalla de Pygame con efecto de profundidad
    draw_edges_with_depth(screen, edges, depth_data, min_depth, max_depth)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
