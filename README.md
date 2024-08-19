# Snake Game using Python

## Description

This project is a modern take on the classic Snake game, developed in Python using the Turtle graphics library for rendering and Pygame for sound effects. The game features multiple levels, dynamic gameplay, and an immersive experience with integrated sound effects.

## Features

1. **Classic Gameplay**: Navigate a snake to eat food, grow longer, and avoid collisions.

2. **Sound Effects**: Includes sound effects for key actions:
   - **Eating Food**: A sound plays when the snake eats food.
   - **Changing Direction**: A sound plays when the snake changes direction.
   - **Collisions**: A sound plays when the snake collides with itself or an obstacle.
   - **Level Up**: A sound plays when advancing to a new level.

3. **Level Progression**:
   - **Level 1**: Basic gameplay with an increasing snake speed as the score rises.
   - **Level 2**: Introduces static obstacles, adding more challenge to the gameplay. This level unlocks when the score reaches 100.

4. **Score Tracking**: Displays the current and high scores on the screen, updating in real-time.

5. **Collision Detection**:
   - **Borders**: The game ends if the snake collides with the screen borders.
   - **Self-Collision**: The game ends if the snake collides with its own body.
   - **Obstacle Collision**: In Level 2, the game ends if the snake collides with obstacles.

6. **Speed Adjustment**: The snake’s speed increases as the score increases, making the game progressively harder.

7. **Controls**:
   - **Up Arrow**: Move the snake up.
   - **Down Arrow**: Move the snake down.
   - **Left Arrow**: Move the snake left.
   - **Right Arrow**: Move the snake right.

## Dependencies

- **Python 3.8+**: Make sure you have Python version 3.8 or later installed on your system.

- **Turtle Graphics**: This library is included with Python and used for rendering the game graphics.

- **Pygame**: Required for sound effects. 
