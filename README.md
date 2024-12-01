# Ping Pong Game 🎮

A classic two-player Ping Pong game built with Python's `turtle` module. Players control paddles to hit a ball back and forth, aiming to score points by making the opponent miss.

## Features
- Smooth animations using Python's `turtle` graphics.
- Real-time collision detection with walls and paddles.
- Scoring system to keep track of points for both players.
- Progressive difficulty as the ball speeds up with each paddle hit.

## Gameplay Instructions
- **Player 1 (Right Paddle)**:  
  - Move Up: Press the **Up Arrow** key.  
  - Move Down: Press the **Down Arrow** key.  
- **Player 2 (Left Paddle)**:  
  - Move Up: Press the **W** key.  
  - Move Down: Press the **S** key.  

The game starts with the ball moving automatically. Hit the ball with your paddle to bounce it back. A point is scored when the opponent misses the ball.

## Requirements
- Python 3.x
- Turtle graphics module (pre-installed with Python).

## How to Run
1. Clone this repository or download the game files:
   ```bash
   git clone https://github.com/your-username/ping-pong-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ping-pong-game
   ```
3. Run the game:
   ```bash
   python ping_pong_game.py
   ```

## Project Structure
- `ping_pong_game.py`: Main game script to initialize and run the game.
- `paddle.py`: Defines the `Paddle` class for controlling the paddles.
- `ball.py`: Defines the `Ball` class for ball movement and collision logic.
- `score.py`: Defines the `ScoreBoard` class for tracking and displaying scores.

## Screenshots
![Ping Pong Game Screenshot](https://via.placeholder.com/800x400.png?text=Screenshot+of+Ping+Pong+Game)

## Features for Possiple Future Development
- Add sound effects for collisions and scoring.
- Introduce a single-player mode with AI-controlled paddle.
- Add customization options for paddle and ball colors.
- Include difficulty settings for varied gameplay.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to Python's `turtle` library for making this project simple and fun to build.
