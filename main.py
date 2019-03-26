from PIL import Image
import pygame
import random
import time
 
def setup_bw_image(color_image, bw_image):
   bw = color_image.convert('LA')
   bw.save(bw_image)
   return bw, bw.width, bw.height
 
if __name__ == '__main__':
    pygame.init()


    file_name = input("Please enter the filename: ")
    color_image = Image.open(file_name)
    bw_image, width, height = setup_bw_image(color_image, "bw_" + file_name)
    bw_image = bw_image.load()

    algorithm_type = input("Which algorithm would you like to run: ")

    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)

    screen = pygame.display.set_mode((width * 10, height * 10))
    screen.fill(white)

    # this algorithm fills in every 10x10 grid of pixels with a certain number of black circles based on the color of the original black and white image
    if (algorithm_type == '1'):
        for col in range(0, height):
            for row in range(0, width):
                if (bw_image[row, col][0] < 32):
                    for col2 in range(0, 5):
                        for row2 in range(0, 5):
                            pygame.draw.circle(screen, black, (10 * row + (2 * row2) + random.randint(-1, 1), 10 * col + (2 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 64):
                    for col2 in range(0, 4):
                        for row2 in range(0, 4):
                            pygame.draw.circle(screen, black, (10 * row + (3 * row2) + random.randint(-1, 1), 10 * col + (3 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 96):
                    for col2 in range(0, 5):
                        for row2 in range(0, 3):
                            pygame.draw.circle(screen, black, (10 * row + (4 * row2) + random.randint(-1, 1), 10 * col + (4 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 128):
                    for col2 in range(0, 2):
                        for row2 in range(0, 2):
                            pygame.draw.circle(screen, black, (10 * row + (5 * row2) + random.randint(-1, 1), 10 * col + (5 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 160):
                    for col2 in range(0, 2):
                        for row2 in range(0, 2):
                            pygame.draw.circle(screen, black, (10 * row + (6 * row2) + random.randint(-1, 1), 10 * col + (6 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 192):
                    for col2 in range(0, 2):
                        for row2 in range(0, 2):
                            pygame.draw.circle(screen, black, (10 * row + (7 * row2) + random.randint(-1, 1), 10 * col + (7 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 224):
                    for col2 in range(0, 2):
                        for row2 in range(0, 2):
                            pygame.draw.circle(screen, black, (10 * row + (8 * row2) + random.randint(-1, 1), 10 * col + (8 * col2) + random.randint(-1, 1)), 1)
                elif (bw_image[row, col][0] < 256):
                    for col2 in range(0, 2):
                        for row2 in range(0, 2):
                            pygame.draw.circle(screen, black, (10 * row + (9 * row2) + random.randint(-1, 1), 10 * col + (9 * col2) + random.randint(-1, 1)), 1)
            pygame.display.flip()
            time.sleep(0.01)
    elif (algorithm_type == '2'):
        for col in range(0, height):
            for row in range(0, width):
                if (bw_image[row, col][0] < 32):
                    for i in range(0, 20):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 64):
                    for i in range(0, 30):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 96):
                    for i in range(0, 40):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 128):
                    for i in range(0, 50):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 160):
                    for i in range(0, 60):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 192):
                    for i in range(0, 70):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 224):
                    for i in range(0, 80):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
                elif (bw_image[row, col][0] < 256):
                    for i in range(0, 90):
                        pygame.draw.circle(screen, black, (10 * row + (random.randint(0, 10)), 10 * col + (random.randint(0, 10))), 1)
            pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()