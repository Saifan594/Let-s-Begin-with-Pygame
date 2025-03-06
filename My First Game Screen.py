import pygame

pygame.init()

white = (255, 255, 255)

clock = pygame.time.Clock()

displaySurface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My First Game Screen")

image = pygame.image.load("Photo.jpg")

defaultImageSize = (200, 200)

image = pygame.transform.scale(image, defaultImageSize)

defaultImagePosition = (150, 150)

while True:
    displaySurface.fill(white)
    displaySurface.blit(image, defaultImagePosition)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    
    clock.tick(30)