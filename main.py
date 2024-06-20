import pygame


pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Tricky, Terna, TictacToe") # Asignamos titulo del juego

fondo = pygame.image.load(f'static/tictactoe_background.png')
circulo = pygame.image.load(f'static/circle.png')
equis = pygame.image.load(f'static/x.png')

fondo = pygame.transform.scale(fondo, (450,450))
circulo = pygame.transform.scale(circulo, (125,125))
equis = pygame.transform.scale(equis, (125,125))
#Colores para el mensaje
green = (0, 255, 0)
blue = (0, 0, 128)
text_font = pygame.font.SysFont("Arial", 30)
#ubicaciones del mensaje
mgs_X= 150
mgs_Y= 150

#creamos mapa de coordenadas
coor = [[(40,50),(165,50),(290,50)],
        [(40,175),(165,175),(290,175)],
        [(40,300),(165,300),(290,300)]]

tablero = [["","",""],
           ["","",""],
           ["","",""]]
turno = 'X'
game_over = False
clock = pygame.time.Clock()

def grafic_board():
    screen.blit(fondo, (0,0))
    for fila in range(3):
     for col in range(3):
         if tablero[fila][col] == 'X':
             dibujar_x(fila,col)
         elif tablero[fila][col] == 'O':
             dibujar_y(fila,col)
         
def dibujar_x(fila, col): #Dibujamos la imagen de X en la posicion indicada
    screen.blit(equis, coor[fila][col])

def dibujar_y(fila, col): #Dibujamos la imagen de Y en la posicion indicada
    screen.blit(circulo, coor[fila][col])

def draw_text(text, font, text_col, x, y):
    screen.fill((255, 255, 255)) #Blanqueamos el fondo.
    img = font.render(text, True, text_col)
    screen.blit(img,(x // 2 ,y // 2 )) #imprimimos y centramos el mensaje
    pygame.display.update() #Actualizamos para que aparezca
    pygame.time.wait(3000) # Que se mantenga por x Segundos

def who_won():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "":
            return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
            return True
    return False
    

while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            #Validamos que usuario haga click en nuestra area de interez y descartamos periferias
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425): 
                fila = (mouseY - 50) // 125
                col = (mouseX - 40) // 125 
                if tablero[fila][col] == "":
                    tablero[fila][col] = turno
                    fin_juego = who_won()
                    if fin_juego:
                        draw_text(f"El jugador {turno} ha ganado!!", text_font, blue, mgs_X, mgs_Y)
                        game_over = True #Cambiamos el estado de juego ganado
                    turno = 'O' if turno == 'X' else 'X'
            #print(mouseX, mouseY) Nos sirve para saber donde hacemos click
        grafic_board()
    pygame.display.update()

pygame.quit()