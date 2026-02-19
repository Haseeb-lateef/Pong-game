# 🏓 Pong Game

A classic two-player Pong game built with Python's Turtle graphics library. Challenge a friend in this timeless arcade game with smooth paddle controls and dynamic ball physics!

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Turtle](https://img.shields.io/badge/Library-Turtle-green.svg)
![Players](https://img.shields.io/badge/Players-2-orange.svg)

## 📖 About

This is a faithful recreation of the classic Pong arcade game featuring two-player gameplay, real-time score tracking, and increasingly challenging ball speeds. Perfect for competitive play or learning Python game development!

## ✨ Features

- **Two-Player Gameplay**: Classic left vs. right paddle action
- **Responsive Controls**: Smooth and intuitive paddle movement
- **Dynamic Ball Physics**: 
  - Ball bounces off paddles and top/bottom borders
  - Speed increases with each paddle hit for progressive difficulty
- **Live Scoreboard**: 
  - Real-time score tracking for both players
  - Centered dividing line for authentic Pong aesthetics
- **Auto-Reset**: Ball automatically resets after each point
- **Collision Detection**: Accurate paddle-to-ball collision system

## 🎮 How to Play

### Controls

**Left Player (Left Paddle):**
- **W**: Move paddle up
- **S**: Move paddle down

**Right Player (Right Paddle):**
- **↑ (Up Arrow)**: Move paddle up
- **↓ (Down Arrow)**: Move paddle down

### Rules

1. The ball bounces between the two paddles
2. Hit the ball with your paddle to send it back to your opponent
3. If the ball passes your paddle, your opponent scores a point
4. The ball speed increases slightly with each successful paddle hit
5. First to... well, there's no limit - play as long as you want!

## 🚀 Installation

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics library (comes pre-installed with Python)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/Haseeb-lateef/Pong-game.git
```

2. Navigate to the project directory:
```bash
cd Pong-game
```

3. Run the game:
```bash
python main.py
```

## 📂 Project Structure

```
Pong-game/
│
├── main.py          # Main game loop and screen setup
├── paddle.py        # Paddle class with movement controls
├── ball.py          # Ball class with physics and collision detection
└── scoreboard.py    # Scoreboard class for score tracking and display
```

## 🛠️ Technical Details

### Classes

**Paddle** (`paddle.py`)
- Creates paddle objects at specified positions
- Handles up/down movement with boundary detection
- Prevents paddles from moving off-screen

**Ball** (`ball.py`)
- Manages ball movement and trajectory
- Implements bounce physics for walls and paddles
- Detects collisions with paddles and boundaries
- Handles out-of-bounds detection
- Progressive speed increase on paddle hits

**Scoreboard** (`scoreboard.py`)
- Displays scores for both players
- Draws the center dividing line
- Updates score in real-time
- Clean, centered score display

### Game Configuration
- **Screen Size**: 800x600 pixels
- **Background**: Black
- **Paddle Size**: 5x1 (stretched vertically)
- **Ball**: White circle
- **Initial Ball Speed**: 0.1 seconds per movement
- **Speed Multiplier**: 0.9x (10% faster) per paddle hit

## 🎯 Game Mechanics

- Ball moves continuously in its current direction
- Ball bounces off top and bottom borders
- Ball reverses horizontal direction when hitting paddles
- Ball speed increases by 10% each time it hits a paddle
- Points are awarded when the ball passes an opponent's paddle
- Ball resets to center after each point with a brief pause
- Paddles have movement boundaries to stay on screen

## 🔧 Customization Ideas

Want to enhance the game? Try these modifications:
- Add AI for single-player mode
- Implement a winning score limit
- Add sound effects
- Create different difficulty levels
- Add power-ups or obstacles
- Customize colors and themes

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Haseeb-lateef/Pong-game/issues).

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

**Haseeb Lateef**
- GitHub: [@Haseeb-lateef](https://github.com/Haseeb-lateef)

## 🎉 Acknowledgments

- Built with Python's Turtle graphics library
- Inspired by the original Pong arcade game from 1972
- A classic game that started it all!

---

*Game on! May the best player win!* 🏓✨