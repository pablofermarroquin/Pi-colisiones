import pygame
#import pygame.freetype  # Import the freetype module.

#==========================================================
#Constantes y valores iniciales
espera =10
digitos = 6

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

while run:
    
    if(VBf > 0 and VAf >0 and VAf>VBf and xB > x0+100):
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
    
    
print(colisiones/10**(digitos-1))




