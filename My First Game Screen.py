print("\033c")

import pygame

pygame.init()

display_title = "My First Game Screen"
display_size = (500, 700)
display_color = (255, 255, 255)
display = pygame.display.set_mode(display_size)

image_filename = "Photo.jpg"
image_size = (300, 300)
image_dest = (100, 100)
image_surface = pygame.image.load(image_filename)
image = pygame.transform.scale(image_surface, image_size)

font_size = 100
font_text = "Saifan"
font_antialias = True
font_dest = (100, 500)
font_color = (0, 0, 0)
font = pygame.font.SysFont(pygame.font.get_default_font(), font_size)
text = font.render(font_text, font_antialias, font_color)

clock_framerate = 30
clock = pygame.time.Clock()

pygame.display.set_caption(display_title)

while True:
    display.fill(display_color)
    
    display.blit(image, image_dest)
    display.blit(text, font_dest)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    clock.tick(clock_framerate)