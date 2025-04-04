import pygame
import sys
from modules.maze import Maze, TILE_SIZE
from modules.pacman import Pacman
from modules.ghost import Ghost

BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 184, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 184, 82)

pygame.init()

maze = Maze()
screen_width = maze.width * TILE_SIZE
screen_height = maze.height * TILE_SIZE

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# initial position of pac-man
pacman = Pacman(14, 23)

ghosts = [
    Ghost(13, 11, "blinky"),    
    Ghost(14, 11, "pinky"),     
    Ghost(12, 14, "inky"),     
    Ghost(15, 14, "clyde")     
    ]

score = 0
game_over = False
game_won = False
font = pygame.font.SysFont("Arial", 24)


ghost_update_timer = 0
GHOST_UPDATE_THRESHOLD = 10  # used to change ghost's speed

# Main game loop
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                pacman.next_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                pacman.next_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                pacman.next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                pacman.next_direction = (1, 0)

    if not game_over and not game_won:
        
        pacman.update(maze)
        
        eaten = maze.eat_pellet((pacman.col, pacman.row))
        if eaten is not None:
            if eaten == '.':
                score += 10
            elif eaten == 'o':
                score += 50  

        # Check win condition: if there are no pellets left, the player wins
        if not maze.pellets:
            game_won = True

        
        ghost_update_timer += 1
        if ghost_update_timer >= GHOST_UPDATE_THRESHOLD:
            for ghost in ghosts:
                ghost.update(maze, (pacman.col, pacman.row))
                # Check collision: if a ghost catches Pac-Man, game over
                if ghost.col == pacman.col and ghost.row == pacman.row:
                    game_over = True
            ghost_update_timer = 0  # Reset timer

    
    screen.fill(BLACK)
    maze.draw(screen)
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, screen_height - 30))

    # Display win or game over message
    if game_over:
        over_text = font.render("Game Over! Press Q to Quit", True, RED)
        screen.blit(over_text, (screen_width // 2 - 150, screen_height // 2))
    if game_won:
        win_text = font.render("You Win! Press Q to Quit", True, (0, 255, 0))
        screen.blit(win_text, (screen_width // 2 - 150, screen_height // 2))
    
    pygame.display.flip()

    # Allow quitting with Q when game is over or won
    keys = pygame.key.get_pressed()
    if (game_over or game_won) and keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
