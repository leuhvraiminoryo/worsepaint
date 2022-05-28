from res.utils import *

pressed = {}

active_color = WHITE
mouse_pos = (0,0)
state = "writing"
pensize = 5
PCANVAS = [CANVAS.copy()]

while True:
    SCR.fill(SPEGREEN)
    checkForQuit()
    #verifKeyPresses(pressed)
    last_mouse_pos = mouse_pos
    mouse_pos = mousePosCorrection(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == MOUSEWHEEL:
            if state == "writing":
                print(event.y)
                pensize += event.y
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

    if pensize < 1:
        pensize = 1
    if pensize > 50:
        pensize = 50

    try :
        if pressed["mleft"]:
            if state == "writing":
                pygame.draw.line(CANVAS,active_color,last_mouse_pos,mouse_pos,width=pensize)
    except KeyError:
        pass

    try :
        if pressed["mright"]:
            if state == "writing":
                pygame.draw.circle(CANVAS,BLACK,mouse_pos,pensize*2)
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