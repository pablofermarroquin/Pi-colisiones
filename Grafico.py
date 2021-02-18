import pygame
import pygame.freetype  # Import the freetype module.

def text_objects(text, font):
    textSurface = font.render(text, True, "black")
    return textSurface, textSurface.get_rect()


#==========================================================
#Constantes y valores iniciales
espera =10
digitos = 4

x0=40
xA = 300
xB=200
y = 160
width = 50
height = 50
VAo=-10
VBo=0
MA=100**(digitos-1)
MB=1

VAf=VAo
VBf=VBo
run = True
colisiones=0
mover=True
#==========================================================

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

while run:
    pygame.time.delay(espera)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (220,220,220), (30, 110, 10, 100)) #pared
    pygame.draw.rect(win, (220,220,220), (30, 210, 500, 10)) #suelo
    if(xA<=93):
        posxA=93
    else:
        posxA=xA
    pygame.draw.rect(win, (255,0,0), (posxA, y, width, height))  
    if(xB<=40 or xA<=93):
        if(mover):
            posxB=40
        else:
            posxB=43
        mover = not mover
    else:
        posxB=xB
    pygame.draw.rect(win, (0,255,0), (posxB, y, width, height)) 
    
    pygame.draw.rect(win, (255,255,255), (20, 280, 400, 100)) #suelo
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(str(colisiones), largeText)
    TextRect.center = ((250),(340))
    win.blit(TextSurf, TextRect)
    
    pygame.display.update() 
    #pygame.time.delay(1)
    if(VBf > 0 and VAf >0 and VAf>VBf and xB > x0+100):
        pygame.time.delay(3000)
        run = False

    VAo=VAf
    VBo=VBf

    if xB<x0:
        VBf=-VBf
        colisiones+=1
        
    if xB+50>=xA:
        VAf=(VAo*(MA-MB)+2*MB*VBo)/(MA+MB)
        VBf=VAo-VBo+VAf
        colisiones+=1
    
    xA += VAf
    xB+= VBf
    
    
    
    
print(colisiones)
pygame.quit()





