# Asteroids Game

Welcome to the Asteroids Game, a 2D arcade-style game where the player must navigate through space, avoiding and destroying asteroids. This project is an implementation of a classic game, created using Python and Pygame. 🚀🌟✨

## Table of Contents

1. [Game Overview](#game-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Controls](#controls)
5. [Code Structure](#code-structure)
6. [Future Improvements](#future-improvements)
7. [Credits](#credits)

---

## Game Overview

In this game, the player controls a spaceship that can rotate and move in space. The goal is to survive by avoiding collisions with asteroids and shooting them to split or destroy them. Each asteroid can split into smaller ones until it reaches a minimum size. 🎮🌌🪐

## Features

- **Player Movement:** Rotate and move the spaceship in any direction.
- **Shooting Mechanism:** Fire shots to destroy asteroids.
- **Asteroid Splitting:** Asteroids split into smaller ones upon being hit until they reach the minimum size.
- **Collision Detection:** Collisions between the player and asteroids result in game over.
- **Dynamic Asteroid Field:** Asteroids spawn dynamically from screen edges with randomized velocity and direction.

## Installation

To play this game, you need to have Python and Pygame installed on your system. 🛠️📥💻

### Steps:
1. Clone the repository or download the source code.
2. Install the required library:
   ```bash
   pip install pygame
   ```
3. Run the `main.py` file:
   ```bash
   python main.py
   ```

## Controls

- **`W`**: Move forward.
- **`S`**: Move backward.
- **`A`**: Rotate left.
- **`D`**: Rotate right.
- **`SPACE`**: Shoot.

## Code Structure

The project is organized into multiple Python files for modularity: 🗂️📜📋

- **`main.py`**: Entry point of the game. Handles the game loop and overall logic.
- **`player.py`**: Contains the `Player` class, defining the spaceship's behavior and actions.
- **`shot.py`**: Contains the `Shot` class for handling the player's projectiles.
- **`asteroid.py`**: Contains the `Asteroid` class for defining asteroid behavior.
- **`asteroidfield.py`**: Spawns and manages the asteroids dynamically.
- **`circleshape.py`**: Base class for circular objects, including collision detection.
- **`constants.py`**: Holds configuration constants such as screen dimensions, player speed, etc.

## Future Improvements

- Add a scoring system to track player achievements.
- Implement levels with increasing difficulty.
- Add sound effects for player actions and asteroid collisions.
- Introduce power-ups and additional challenges.
- Improve graphics and animations. 🎯🔊🎨

## Credits

Created by **Fabricio González Guasque** as part of my studies at **Boot.Dev**. Special thanks to the Pygame community for their excellent resources and tutorials. 🙌📚✨

---

Enjoy the game and feel free to suggest improvements or report issues! 🌟👍🚀

