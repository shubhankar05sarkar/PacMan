import pygame

BLUE = (0, 0, 255)          # Wall color
BLACK = (0, 0, 0)           # Background color
WHITE = (255, 255, 255)     # Pellet color
PINK = (255, 184, 151)      # Power pellet color
TILE_SIZE = 24              # Pixel size for each grid cell

maze_layout = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.##### ## #####.#     ",
    "     #.##          ##.#     ",
    "     #.## ###--### ##.#     ",
    "######.## #      # ##.######",
    "      .  #      #  .       ",
    "######.## #      # ##.######",
    "     #.## ######## ##.#     ",
    "     #.##          ##.#     ",
    "     #.## ######## ##.#     ",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

class Maze:
    def __init__(self):
       
        expected_length = len(maze_layout[0])
        self.layout = []
        for row in maze_layout:
            
            if len(row) < expected_length:
                row = row.ljust(expected_length, '#')
            else:
                row = row[:expected_length]
            self.layout.append(row)
            
        self.width = len(self.layout[0])
        self.height = len(self.layout)
        self.tile_size = TILE_SIZE

        self.pellets = {}
        self.init_pellets()

    def init_pellets(self):
        
        for row_idx, row in enumerate(self.layout):
            for col_idx, ch in enumerate(row):
                if ch == '.' or ch == 'o':
                    self.pellets[(col_idx, row_idx)] = ch

    def draw(self, surface):
        
        for row_idx, row in enumerate(self.layout):
            for col_idx, ch in enumerate(row):
                x = col_idx * self.tile_size
                y = row_idx * self.tile_size
                if ch == '#':  
                    rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
                    pygame.draw.rect(surface, BLUE, rect)
                
                if (col_idx, row_idx) in self.pellets:
                    pellet_type = self.pellets[(col_idx, row_idx)]
                    center = (x + self.tile_size // 2, y + self.tile_size // 2)
                    if pellet_type == '.':
                        pygame.draw.circle(surface, WHITE, center, 3)
                    elif pellet_type == 'o':
                        pygame.draw.circle(surface, PINK, center, 6)

    def eat_pellet(self, pos):
        """
        Remove a pellet from the maze if Pac-Man is on that position.
        Returns the pellet type ('.' or 'o') if present, else None
        """
        if pos in self.pellets:
            pellet = self.pellets.pop(pos)
            return pellet
        return None
