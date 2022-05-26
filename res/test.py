from res.utils import *

pressed = {
    "mleft" : False,
    "mright" : False,
    "\x1a" : False, # ctrl + z
}

active_color = WHITE
mouse_pos = (0,0)
PCANVAS = []

while True:
    SCR.fill(BLACK)
    checkForQuit()
    #verifKeyPresses(pressed)
    last_mouse_pos = mouse_pos
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            PCANVAS.append(CANVAS.copy())
            if event.button == 1:
                pressed['mleft'] = True
            if event.button == 3:
                pressed['mright'] = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                pressed['mleft'] = False
            if event.button == 3:
                pressed['mright'] = False
        if event.type == KEYDOWN:
            if not event.unicode == '':
                pressed[event.unicode] = True
        if event.type == KEYUP:
            if not event.unicode == '':
                pressed[event.unicode] = False

    if pressed["mleft"]:
        pygame.draw.line(CANVAS,active_color,last_mouse_pos,mouse_pos,width=5)

    if pressed["mright"]:
        pygame.draw.circle(CANVAS,BLACK,mouse_pos,10)

    if pressed["\x1a"]:
        if PCANVAS != []:
            CANVAS = PCANVAS.pop()
            pressed["\x1a"] = False

    SCR.blit(CANVAS,(0,0))

    pygame.display.update()
    FPSCLOCK.tick(FPS)