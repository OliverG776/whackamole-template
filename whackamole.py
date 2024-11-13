import pygame, random


def main():
    #pygame.draw.line(screen, color, (1, 0), end_pos)
    LINE_COLOR = (0, 0, 0)

    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))


        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_pos = (0,0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    event.pos = pygame.mouse.get_pos()
                    print(event.pos)
                    print(mole_pos)


                    if event.pos[0] // 32  <= mole_pos[0] // 32 and mole_pos[0] < event.pos[0] and event.pos[1] // 32 <= mole_pos[1] // 32 and mole_pos[1] < event.pos[1]:
                        screen.fill("light green")
                        random1 = random.randrange(0, 609)
                        random2 = random.randrange(0, 481)
                        while random1 % 32 != 0:
                            random1 = random.randrange(0, 609)
                        while random2 % 32 != 0:
                            random2 = random.randrange(0, 481)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(random1, random2)))
                        mole_pos = (random1, random2)
            pygame.display.flip()
            clock.tick(60)

            # Drawing Vertical lines

            current = 33
            while current != 641:
                pygame.draw.line(screen, LINE_COLOR, (current, 0), (current, 513))
                current += 32
            # Drawing Horizontal lines
            current = 33
            while current != 513:
                pygame.draw.line(screen, LINE_COLOR, (0, current), (640, current))
                current += 32


    finally:
        pygame.quit()


#event.type == pygame.MOUSEBUTTONDOWN
#event.pos


#Use to randomly make a spot
#random.randrange(low, high)
#Last number not inclusive

if __name__ == "__main__":
    main()
