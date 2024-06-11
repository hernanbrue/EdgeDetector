import os
import cv2
import numpy as np
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Captura de Bordes desde Webcam")

# Configurar el color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Carpeta para guardar los archivos
save_folder = "3D/data_saved"

# Crear la carpeta si no existe
os.makedirs(save_folder, exist_ok=True)

# Captura de video desde la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    sys.exit()

# Bucle principal
running = True
saved = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                saved = True

    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el frame de la cámara.")
        break

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar el detector de bordes de Canny
    edges = cv2.Canny(gray, 100, 200)

    # Mostrar la imagen de bordes en Pygame
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    edges_rgb = np.rot90(edges_rgb)
    edges_surface = pygame.surfarray.make_surface(edges_rgb)
    screen.blit(edges_surface, (0, 0))
    pygame.display.flip()

    # Guardar la imagen de bordes si se presionó 'D'
    if saved:
        cv2.imwrite(os.path.join(save_folder, 'edges_detected.png'), edges)
        np.save(os.path.join(save_folder, 'depth_data.npy'), gray)  # Guardar los datos de profundidad en un archivo .npy
        saved = False

cap.release()
pygame.quit()
sys.exit()
