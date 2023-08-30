import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PIECE_SIZE = 100
ROWS = 3
COLS = 3

# Colors
WHITE = (255, 255, 255)

# Load the image
original_image = pygame.image.load("image.jpg")
original_image = pygame.transform.scale(original_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Split the image into pieces
pieces = []
for row in range(ROWS):
    for col in range(COLS):
        piece = original_image.subsurface(
            pygame.Rect(col * PIECE_SIZE, row * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE)
        )
        pieces.append(piece)

# Shuffle the pieces
random.shuffle(pieces)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Picture Puzzle Game")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Display the shuffled pieces
    for index, piece in enumerate(pieces):
        row = index // COLS
        col = index % COLS
        screen.blit(piece, (col * PIECE_SIZE, row * PIECE_SIZE))

    pygame.display.flip()

pygame.quit()
