from res.utils import *

pressed = {
    "mleft" : False,
    "mright" : False,
    "ctrl" : False,
}

active_color = WHITE
mouse_pos = (0,0)

while True:
    SCR.fill(BLACK)
    checkForQuit()
    verifKeyPresses(pressed)
    last_mouse_pos = mouse_pos
    mouse_pos = pygame.mouse.get_pos()

    if pressed["mleft"]:
        pygame.draw.line(CANVAS,active_color,last_mouse_pos,mouse_pos,width=5)
    if pressed["mright"]:
        pygame.draw.circle(CANVAS,BLACK,mouse_pos,10)

    SCR.blit(CANVAS,(0,0))

    pygame.display.update()
    FPSCLOCK.tick(FPS)