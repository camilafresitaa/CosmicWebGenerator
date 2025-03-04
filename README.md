# Cosmic Web Generator

This project aims to simulate the large-scale structure of the universe, known as the cosmic web, through recursive algorithms and interactive controls.
It provides users with the ability to explore how filaments, galaxies, and stars form interconnected patterns in 3D space.
The application integrates fractal-based logic, allowing adjustments in real-time using a graphical user interface (GUI).


## Project Overview

**Language:** Python 3  

**Key Libraries Used:**  
- VPython: For 3D visualization of the cosmic structures.  
- Tkinter: To create a responsive user interface.  
- Random: To add variability and randomness to the cosmic structures.


## Structure

The project is organized into three Python files:

#### 1) `main.py`  
This file initializes the simulation environment, including the 3D VPython canvas for visualization and the Tkinter-based GUI for control.  
It contains the main loop and central functions for updating the simulation parameters dynamically.

#### 2) `functions.py`  
Contains the primary logic and algorithms for fractal generation and visualization.  
Key components include:
- The recursive function responsible for generating filaments and structures.
- Supporting utilities for creating individual stars, galaxies, and filaments, as well as resetting or updating the visualization.
- Algorithms that dynamically interpret user input from the GUI and apply it to the VPython scene.

#### 3) `settings.py`  
A configuration file that defines the project's parameters and defaults.  
It includes:
- Global variables to track the state of the universe, such as universe_age and num_filaments.
- Color settings for different cosmic styles (e.g., filament color, galaxy color, and star color).
- Lists to store all generated objects, enabling real-time updates and scene resetting.


## How to Run  

1. Ensure **Python 3** is installed along with the required libraries.
   
   To install **VPython**, run the following command in your terminal:
   ```
   pip install vpython
    ```

2. Run the application by executing `main.py`.
   
   After installing the necessary libraries, run the following command:
   ```
   python main.py
   ```
   This will open two windows:
   - **VPython Canvas:** Displays a 3D visualization of the cosmic web.
   - **Tkinter GUI:** Offers controls to adjust fractal parameters in real time, such as the number of iterations or density.


## Important Notes

This project is intended for educational and illustrative purposes only.  
It does not represent an accurate simulation of the universe's actual formation.


## Credits

Fae Jordaan, Camila Medrano, Anastasiia Korolenko and Raya Mouri.  
If you have any questions, feel free to reach out!
