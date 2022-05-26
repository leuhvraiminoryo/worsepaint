from res.utils import *

pressed = {}

active_color = WHITE
mouse_pos = (0,0)
PCANVAS = [CANVAS.copy()]

while True:
    SCR.fill(BLACK)
    checkForQuit()
    #verifKeyPresses(pressed)
    last_mouse_pos = mouse_pos
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            try:
                if not pygame.image.tostring(PCANVAS[-1],'RGB') == pygame.image.tostring(CANVAS,'RGB'):
                    PCANVAS.append(CANVAS.copy())
            except IndexError:
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

    try :
        if pressed["mleft"]:
            pygame.draw.line(CANVAS,active_color,last_mouse_pos,mouse_pos,width=5)
    except KeyError:
        pass

    try :
        if pressed["mright"]:
            pygame.draw.circle(CANVAS,BLACK,mouse_pos,10)
    except KeyError:
        pass
        
    try :
        if pressed["\x1a"]:
            if PCANVAS != []:
                CANVAS = PCANVAS.pop()
                pressed["\x1a"] = False
    except KeyError:
        pass

    SCR.blit(CANVAS,(0,0))

    pygame.display.update()
    FPSCLOCK.tick(FPS)