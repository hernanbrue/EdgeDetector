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
- [Additional Information](#additional-information)
- [Example Usage](#example-usage)

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


## Additional Information
File Structure
The repository is organized as follows:

3d-edge-detection/
│
├── 3D/
│   └── data_saved/       # Directory where captured data is saved
│       ├── edges_detected.png
│       └── depth_data.npy
│
├── main3d.py             # Script for capturing edge images and depth data from webcam
├── draw3d.py             # Script for visualizing depth data with edge images


## Example Usage
Here is an example workflow to help you get started:

Capture Edges and Depth Data:

Run main3d.py to start capturing video from your webcam.
Press the D key to save an edge image and depth data.
Visualize Depth Data:

Run draw3d.py to load the saved data and visualize the depth using a color gradient.
