# Pac-Man Game (Python + Pygame)

This project is a faithful recreation of the classic arcade game Pac-Man, built using Python and Pygame. The game captures the nostalgic feel of the original while demonstrating key programming concepts such as game loops, sprite animations, collision detection, and basic artificial intelligence using Breadth-First Search (BFS) for enemy movement.

## Objective:
The main goal of the game is to navigate Pac-Man through a maze, eat all the small pellets (dots) and power pellets (bigger dots), and ultimately win the level by clearing the maze.

## Controls:
The game is controlled via the keyboard's arrow keys:

Up Arrow: Move Pac-Man up.

Down Arrow: Move Pac-Man down.

Left Arrow: Move Pac-Man left.

Right Arrow: Move Pac-Man right.

Esc/Q: Quit the game or exit once the game is over.

## Game Mechanics:

### Maze Layout:
The maze is designed using a grid-based layout where walls, pellets, and power pellets are defined by a set of characters. Walls (#) block movement, while pellets (.) and power pellets (o) are items to be collected.

### Pellet Collection:
As Pac-Man moves through the maze, he collects pellets. Each normal pellet increases your score by 10 points, and each power pellet gives 50 points.

### Ghosts and AI:
The maze is also populated with ghosts. These ghosts use a simple AI based on BFS to chase Pac-Man. This means that the ghosts constantly calculate the shortest path to Pac-Man while navigating around walls. If a ghost catches Pac-Man (i.e., occupies the same grid cell), the game is over.

### Winning and Losing:

Win Condition: The game is won when Pac-Man successfully collects all the pellets in the maze.

Lose Condition: The game is lost if any ghost catches Pac-Man before all pellets are eaten.

## Scoring:
Points are awarded for collecting pellets. Normal pellets and power pellets contribute different point values to your overall score.

## Game Flow

### Start:
When you launch the game, Pac-Man appears near the bottom center of the maze. The maze, complete with walls and pellets, is fully visible on the screen.

### Navigation:
Using the arrow keys, you guide Pac-Man through the maze. The game continuously checks for user input and updates Pac-Man’s position based on valid moves (i.e., moves that do not hit walls).

### Pellet Consumption:
As Pac-Man moves over a pellet’s location, the pellet is removed from the maze, and your score increases accordingly.

### Ghost Chase:
Meanwhile, the ghosts are actively chasing Pac-Man using BFS. They determine the shortest route to Pac-Man and move one tile at a time. If a ghost and Pac-Man occupy the same cell, the game is over.

### End Game:
The game ends in one of two ways:

Victory: If you manage to eat all pellets, you win the game.

Defeat: If a ghost catches Pac-Man, the game is over.

Overall, this Pac-Man project is not only a fun game to play but also an excellent learning resource for understanding the core mechanics behind classic arcade games and basic AI algorithms in a grid-based environment.

---

## Features

- **Classic Maze Layout:**  
  A grid-based maze is defined using a text layout, where `#` represents walls, `.` represents normal pellets, and `o` represents power pellets.

- **Intelligent Ghosts:**  
  Ghosts use a BFS (Breadth-First Search) algorithm to find the shortest path to Pac-Man, making their movement smart and challenging.

- **Pac-Man Animation:**  
  Pac-Man’s sprite changes depending on the direction of movement. The game uses separate image folders for up, down, left, and right animations.

- **Pellet Collection and Scoring:**  
  Pellets are tracked in the maze. The score increases as Pac-Man collects pellets, and when all pellets are eaten, the game is won.

- **Win and Lose Conditions:**  
  If a ghost catches Pac-Man, the game is over. If all pellets are collected, you win the game.

---

## How It Works

### Maze Layout and Pellets

- **Maze Layout:**  
  The maze is defined as a list of strings. Each character represents an element in the maze:
  - `#` = wall  
  - `.` = normal pellet  
  - `o` = power pellet

- **Pellet Tracking:**  
  The `Maze` class initializes a dictionary with pellet positions (keyed by `(col, row)` coordinates) and updates this dictionary when Pac-Man eats a pellet.


### Ghost AI & BFS

- **Breadth-First Search (BFS):**  
  Ghosts use BFS to find the shortest path from their current position to Pac-Man’s position. Here’s how it works in simple terms:
  1. **Start:** Begin at the ghost’s current tile.
  2. **Explore Neighbors:** Look at all adjacent tiles (up, down, left, right) that aren’t walls.
  3. **Layer by Layer:** Continue exploring outward, step-by-step, until Pac-Man’s tile is found.
  4. **Shortest Path:** Once found, the path that was built is the shortest route.
  5. **First Step:** The ghost then moves one tile in the direction of the first step of that path.
  
- **Implementation:**  
  The BFS is implemented in the `bfs_next_move()` function inside `ghost.py`. It uses a queue to explore all possible moves until it finds Pac-Man’s tile, then reconstructs the path back to the ghost’s position.

### Pac-Man Animation

- **Direction-Based Sprites:**  
  Pac-Man’s images are stored in separate folders for each direction (`pacman-up`, `pacman-down`, `pacman-left`, `pacman-right`).
- **Animation Logic:**  
  When Pac-Man changes direction (via keyboard input), the game reloads the corresponding sprite frames. An animation timer cycles through these frames to create a smooth animated effect.

---

## Controls

| Key         | Action         |
|-------------|----------------|
| Arrow Keys  | Move Pac-Man   |
| Esc         | Quit Game      |

---

## Screenshots

### Main Screen / UI

![Pac-Man UI](https://github.com/shubhankar05sarkar/Pac-Man/blob/e0478e9ec01515bd91ac5320009d88e2e1284ba5/Screenshot%202025-04-04%20125724.png)

### Game Over Screen

![Game Over Screen](https://github.com/shubhankar05sarkar/Pac-Man/blob/e0478e9ec01515bd91ac5320009d88e2e1284ba5/Screenshot%202025-04-04%20125743.png)

### Victory Screen

![Victory Screen](https://github.com/shubhankar05sarkar/Pac-Man/blob/e0478e9ec01515bd91ac5320009d88e2e1284ba5/Screenshot%202025-04-04%20125849.png)

---

## Learnings and Future Improvements

### Learnings

- **Game Development:**  
  Learned the basics of creating a game loop, handling events, and rendering graphics with Pygame.
- **AI Pathfinding:**  
  Implemented a simple BFS algorithm for ghost movement, ensuring ghosts always take the shortest path to Pac-Man.
- **Sprite Animation:**  
  Managed directional sprite animations for Pac-Man based on user input.

### Future Improvements

- Add a scoring system with lives and levels.
- Implement ghost modes (scatter, frightened) for more dynamic AI.
- Introduce sound effects and background music.
- Enhance UI with menus and instructions.
- Add more visual polish with better sprites and animated effects.

---

## **Author**

Created with ❤️ by **Shubhankar Sarkar**.  
[GitHub Profile](https://github.com/shubhankar05sarkar)

---

*Enjoy playing and happy coding!*

---

