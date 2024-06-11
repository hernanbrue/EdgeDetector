# 3D Edge Detection and Reconstruction

This repository contains two Python scripts for capturing edge images from a webcam and reconstructing 2D depth data visualization using Pygame and OpenCV.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Edge Detection](#edge-detection)
  - [Depth Visualization](#depth-visualization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/3d-edge-detection.git
   cd 3d-edge-detection
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Edge Detection

The `main3d.py` script captures video from your webcam, detects edges using the Canny edge detection algorithm, and saves the edge images and depth data.

1. Run the script:
   ```bash
   python main3d.py
   ```

2. Press the `D` key to save the current edge image and depth data.

### Depth Visualization

The `draw3d.py` script loads the saved edge images and depth data, then visualizes the depth using a color gradient.

1. Run the script:
   ```bash
   python draw3d.py
   ```

## Dependencies

- Python 3.11
- OpenCV
- Pygame
- NumPy

Install the dependencies using the following command:
```bash
pip install opencv-python pygame numpy
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code Details

### `main3d.py`

This script captures video from the webcam, processes the frames to detect edges, and saves the results when the `D` key is pressed.

```python
import os
import cv2
import numpy as np
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Edge Detection from Webcam")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Folder to save the files
save_folder = "3D/data_saved"

# Create the folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Capture video from the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    sys.exit()

# Main loop
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
        print("Error: Could not read the frame from the camera.")
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply the Canny edge detector
    edges = cv2.Canny(gray, 100, 200)

    # Display the edge image in Pygame
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    edges_rgb = np.rot90(edges_rgb)
    edges_surface = pygame.surfarray.make_surface(edges_rgb)
    screen.blit(edges_surface, (0, 0))
    pygame.display.flip()

    # Save the edge image if 'D' is pressed
    if saved:
        cv2.imwrite(os.path.join(save_folder, 'edges_detected.png'), edges)
        np.save(os.path.join(save_folder, 'depth_data.npy'), gray)  # Save depth data as .npy file
        saved = False

cap.release()
pygame.quit()
sys.exit()
```

### `draw3d.py`

This script loads the saved edge images and depth data, then visualizes the depth using a color gradient in Pygame.

```import os
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
sys.exit()```


## Contributing
Contributions are welcome! If you have suggestions for improvements, please:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Additional Information
File Structure
The repository is organized as follows:

bash
Copy code
3d-edge-detection/
│
├── 3D/
│   └── data_saved/       # Directory where captured data is saved
│       ├── edges_detected.png
│       └── depth_data.npy
│
├── main3d.py             # Script for capturing edge images and depth data from webcam
├── draw3d.py             # Script for visualizing depth data with edge images
├── requirements.txt      # File to install dependencies (NOW EMPTY)
└── README.md             # This readme file

## Example Usage
Here is an example workflow to help you get started:

Capture Edges and Depth Data:

Run main3d.py to start capturing video from your webcam.
Press the D key to save an edge image and depth data.
Visualize Depth Data:

Run draw3d.py to load the saved data and visualize the depth using a color gradient.
