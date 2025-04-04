import pygame
import random
from collections import deque
from modules.maze import TILE_SIZE
import os

class Ghost:
    def __init__(self, col, row, ghost_name):
        self.col = col  
        self.row = row  
        self.color = ghost_name  
        self.mode = 'chase'  
        self.speed = 1       
        # Load ghost image from assets using ghost_name
        image_path = os.path.join("assets", "images", "ghosts", f"{ghost_name}.png")
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        except Exception as e:
           
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 0, 0), (TILE_SIZE//2, TILE_SIZE//2), TILE_SIZE//2 - 2)

    def update(self, maze, pacman_pos):
        
        next_move = self.bfs_next_move(maze, pacman_pos)
        if next_move:
            self.col, self.row = next_move
        else:
            self.random_move(maze)

    def bfs_next_move(self, maze, target):
        """
        Perform a simple BFS to find a path to the target.
        Returns the next grid cell in the path.
        """
        start = (self.col, self.row)
        queue = deque([start])
        visited = {start: None}

        while queue:
            current = queue.popleft()
            if current == target:
                break  # Target found

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_pos = (current[0] + dx, current[1] + dy)
                
                if (next_pos[0] < 0 or next_pos[0] >= maze.width or
                    next_pos[1] < 0 or next_pos[1] >= maze.height):
                    continue
                if maze.layout[next_pos[1]][next_pos[0]] == '#':
                    continue
                if next_pos not in visited:
                    visited[next_pos] = current
                    queue.append(next_pos)
        else:
            # If target is unreachable, return None
            return None

        current = target
        path = []
        while current != start:
            path.append(current)
            current = visited[current]
        path.reverse()
        if path:
            return path[0]
        return None

    def random_move(self, maze):
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_col = self.col + dx
            new_row = self.row + dy
            if new_col < 0 or new_col >= maze.width or new_row < 0 or new_row >= maze.height:
                continue
            if maze.layout[new_row][new_col] != '#':
                self.col, self.row = new_col, new_row
                break

    def draw(self, surface):
        x = self.col * TILE_SIZE
        y = self.row * TILE_SIZE
        surface.blit(self.image, (x, y))
