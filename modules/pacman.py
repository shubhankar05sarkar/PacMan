import pygame
from modules.maze import TILE_SIZE
import os

YELLOW = (255, 255, 0)

class Pacman:
    def __init__(self, col, row):
        self.col = col  
        self.row = row  
        self.direction = (0, 0)       
        self.next_direction = (0, 0)  
        self.speed = 1               
        self.current_direction = "right"
        self.frames = self.load_frames(self.current_direction)
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 5  # Adjust to slow down or speed up animation

    def update(self, maze):
        
        new_col = self.col + self.next_direction[0]
        new_row = self.row + self.next_direction[1]
        if self.can_move(new_col, new_row, maze):
            self.direction = self.next_direction
        
            if self.next_direction == (1, 0):
                self.current_direction = "right"
            elif self.next_direction == (-1, 0):
                self.current_direction = "left"
            elif self.next_direction == (0, -1):
                self.current_direction = "up"
            elif self.next_direction == (0, 1):
                self.current_direction = "down"

        new_col = self.col + self.direction[0]
        new_row = self.row + self.direction[1]
        if self.can_move(new_col, new_row, maze):
            self.col = new_col
            self.row = new_row

        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.animation_timer = 0

    def can_move(self, col, row, maze):
        
        if col < 0 or col >= maze.width or row < 0 or row >= maze.height:
            return False
        if maze.layout[row][col] == '#':
            return False
        return True

    def load_frames(self, direction):
        
        frames = []
        path = os.path.join("assets", "images", f"pacman-{direction}")
        for filename in sorted(os.listdir(path)):
            if filename.endswith(".png"):
                image = pygame.image.load(os.path.join(path, filename)).convert_alpha()
                image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                frames.append(image)
        if not frames:
            
            temp = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(temp, YELLOW, (TILE_SIZE // 2, TILE_SIZE // 2), TILE_SIZE // 2 - 2)
            frames.append(temp)
        return frames

    def draw(self, surface):
        # If direction has changed, reload frames for the new direction.
        current_loaded_direction = getattr(self, "loaded_direction", None)
        if current_loaded_direction != self.current_direction:
            self.frames = self.load_frames(self.current_direction)
            self.loaded_direction = self.current_direction
            self.current_frame = 0
            self.animation_timer = 0
        x = self.col * TILE_SIZE
        y = self.row * TILE_SIZE
        surface.blit(self.frames[self.current_frame], (x, y))
