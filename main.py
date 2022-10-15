import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Very Accessible Game')

font = pygame.font.Font('freesansbold.ttf', 32)


yes = font.render('yes', True, (0,0,0))
yesRect = yes.get_rect()
yesRect.center = (WIDTH// 2, HEIGHT// 2)

no = font.render('no', True, (0,0,0))
noRect = no.get_rect()
noRect.center = (WIDTH// 2, HEIGHT// 2)

welcome = font.render('Welcome to Game', True, (0,255,0))
welcRect = welcome.get_rect()
welcRect.center = (WIDTH// 2, HEIGHT// 2)

def main():

    run = True
    WIN.blit(welcome, welcRect)
    while run:
        for event in pygame.event.get():
            
            
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    WIN.fill((0,255,0))
                    WIN.blit(yes, yesRect)

                elif event.button == 3:
                    WIN.fill((255,0,0))
                    WIN.blit(no, yesRect)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()