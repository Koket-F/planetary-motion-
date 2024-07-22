Planet Simulation
This repository contains a Python script to simulate the orbits of planets around the sun using the Pygame library. The simulation models the gravitational forces between celestial bodies and their resulting motion in a 2D space.

Features
Realistic simulation of planetary motion using Newton's law of gravitation.
Visualization of planets and their orbits in a window.
Adjustable parameters for each planet, such as mass, velocity, and position.
Display of the distance from each planet to the sun.
Requirements
Python 3.x
Pygame
Installation
Clone the repository:
sh
Copy code
git clone https://github.com/yourusername/planet-simulation.git
Navigate to the project directory:
sh
Copy code
cd planet-simulation
Install the required dependencies:
sh
Copy code
pip install pygame
Usage
Run the script using Python:

sh
Copy code
python planet_simulation.py
Code Overview
Constants and Initial Setup
AU (Astronomical Unit): Average distance from the Earth to the Sun in meters.
G: Gravitational constant.
SCALE: Scale factor to fit the simulation within the window.
TIMESTEP: Time step for each simulation update in seconds.
Planet Class
The Planet class defines the properties and behaviors of each celestial body:

__init__: Initializes the planet with position, velocity, mass, radius, and color.
draw: Renders the planet and its orbit on the window.
force: Calculates the gravitational force exerted by another planet.
update_position: Updates the planet's position based on the forces acting on it.
distancefromsun: Calculates the maximum distance from the sun.
Main Simulation Loop
The main function runs the simulation:

Initializes the window and clock.
Creates instances of the Planet class for the Sun, Earth, Mars, Mercury, and Venus.
Runs the main loop to update positions, draw planets, and handle events
