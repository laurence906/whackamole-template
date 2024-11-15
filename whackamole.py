import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        molepospix = (0, 0)
        moleposgrid = (0, 0)
        while running:
            screen.fill("light green")
            for i in range(1,20):
                pygame.draw.line(screen, (0,50,255), (i * 32, 0), (i * 32, 512), 1) #draw columns
            for i in range(1,16):
                pygame.draw.line(screen, (0,50,255), (0, i * 32), (640, i * 32), 1) #draw rows

            screen.blit(mole_image, mole_image.get_rect(topleft= molepospix))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: #when click occurs
                    xpos, ypos = event.pos #get the position, floor dividing by 32 to align with the grid squares
                    row = xpos // 32
                    col = ypos // 32
                    clicktuple = (row, col)
                    if clicktuple == moleposgrid: #if a tuple of the click's aligned coordinates equal that of the mole's position, generate a new position for it and redraw it
                        randrow = random.randrange(0, 20) * 32
                        randcol = random.randrange(0, 16) * 32
                        molepospix = (randrow,randcol) #use the pixel values to redraw the mole at the correct positions
                        moleposgrid = (randrow // 32, randcol // 32) #use the grid values to correctly match with click grid values
            pygame.display.flip()#update the board after each iteration
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
