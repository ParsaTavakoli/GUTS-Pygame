import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720 #size of window
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #set window size
pygame.display.set_caption('Very Accessible Game') #title of game

font = pygame.font.Font('freesansbold.ttf', 32) #font used for the game

imp = pygame.image.load("forest.jpg").convert()
WIN.blit(imp, (0, 0)) #displays the image
pygame.display.flip()


yes = font.render('yes', True, (0,0,0))
yesRect = yes.get_rect() #yes writing
yesRect.center = (WIDTH// 2, HEIGHT// 2)

no = font.render('no', True, (0,0,0))
noRect = no.get_rect() # no writing
noRect.center = (WIDTH// 2, HEIGHT// 2)

welcome = font.render('Accessible Dungeon Game. Press Anywhere to start', True, (255,255,255))
welcRect = welcome.get_rect() #home screen welcome writing
welcRect.center = (WIDTH// 2, HEIGHT// 2)

def main():

    run = True
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect((WIDTH// 2) - 500 , (HEIGHT// 2)- 30, 1000, 60)) #dispkay rectangle
    WIN.blit(welcome, welcRect)
    

    while run:
        for event in pygame.event.get(): #listen for events
            
            
            if event.type == pygame.QUIT: #if quit end game
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN: #left click goes to next screen
                if event.button == 1:
                    WIN.blit(imp, (0, 0))
                    pygame.display.flip() 
                    WIN.blit(yes, yesRect)

                elif event.button == 3:
                    WIN.fill((255,0,0))
                    WIN.blit(no, yesRect)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()