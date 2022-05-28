from res.utils import *

pressed = {}

active_color = WHITE
mouse_pos = (0,0)
state = "writing"
PCANVAS = [CANVAS.copy()]

while True:
    SCR.fill(BLACK)
    checkForQuit()
    #verifKeyPresses(pressed)
    last_mouse_pos = mouse_pos
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            PCANVAS.append(CANVAS.copy())
            if len(PCANVAS)>1:
                if pygame.image.tostring(PCANVAS[-1],'RGB') == pygame.image.tostring(PCANVAS[-2],'RGB'):
                    PCANVAS.pop()
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
            if event.key == 1073742048 or event.key == 1073742053:
                state = "ctrl"
            if not event.unicode == '':
                pressed[event.unicode] = True
        if event.type == KEYUP:
            if event.key == 1073742048 or event.key == 1073742053:
                state = "writing"
            if not event.unicode == '':
                pressed[event.unicode] = False

    try :
        if pressed["mleft"]:
            if state == "writing":
                pygame.draw.line(CANVAS,active_color,mousePosCorrection(last_mouse_pos),mousePosCorrection(mouse_pos),width=5)
    except KeyError:
        pass

    try :
        if pressed["mright"]:
            if state == "writing":
                pygame.draw.circle(CANVAS,BLACK,mouse_pos,10)
            if state == "ctrl":
                CANVAS.fill(BLACK)
                PCANVAS = []
    except KeyError:
        pass
        
    try :
        if pressed["\x1a"]:
            if PCANVAS != []:
                CANVAS = PCANVAS.pop()
                pressed["\x1a"] = False
    except KeyError:
        pass

    SCR.blit(CANVAS,((WX-CX)/2,(WY-CY)/2))

    pygame.display.update()
    FPSCLOCK.tick(FPS)