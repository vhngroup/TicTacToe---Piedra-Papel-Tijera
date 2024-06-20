import pygame


pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Piedra, Papel o Tijera")

#Colores para el mensaje
green = (0, 255, 0)
blue = (0, 0, 128)
text_font = pygame.font.SysFont("Arial", 30)
#ubicaciones del mensaje
mgs_X= 150
mgs_Y= 150

def draw_text(text, font, text_col, x, y):
    screen.fill((255, 255, 255))
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))