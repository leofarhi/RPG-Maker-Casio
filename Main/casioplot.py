import pygame
pygame.init()
pygame.mixer.init()
surfaceW = 127
surfaceH = 63
t=6
fullscreenW = 127*t
fullscreenH = 63*t
fullscreen=True
surface = pygame.display.set_mode((fullscreenW,fullscreenH),)

###
def creaTexteObj(texte, Police, couleur):
    texteSurface = Police.render(texte, True, couleur)
    return texteSurface, texteSurface.get_rect()

def message(texte, taille, col, x, y, police, trans=255):
    font_Texte = pygame.font.Font(police, taille)
    font_TexteSurf, font_TexteRect = creaTexteObj(texte, font_Texte, (col[0], col[1], col[2], 255))
    font_TexteRect.center = x, y
    surface.blit(font_TexteSurf, font_TexteRect)
def message_left(texte, taille, col, x, y, police, trans=255):
    font_Texte = pygame.font.Font(police, taille)
    font_TexteSurf, font_TexteRect = creaTexteObj(texte, font_Texte, (col[0], col[1], col[2], 255))
    font_TexteRect.topleft = x, y
    surface.blit(font_TexteSurf, font_TexteRect)
    return font_TexteSurf, font_TexteRect

def taille_texte_left(texte, taille, couleur, x, y, police):
    font_Texte = pygame.font.Font(police, taille)
    font_TexteSurf, font_TexteRect = creaTexteObj(texte, font_Texte, couleur)
    font_TexteRect.topleft = x, y
    return font_TexteSurf, font_TexteRect

KEYDOWN=[]
KEYPRESS=[]
KEYUP=[]
def GetKey(key):
    return key in KEYPRESS
def GetKeyDOWN(key):
    return key in KEYDOWN
def GetKeyUP(key):
    return key in KEYUP
def Keyboard():
    global KEYDOWN, _quit
    KEYDOWN.clear()
    KEYUP.clear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _quit = True
        if event.type == pygame.KEYDOWN:
            KEYDOWN.append(event.key)
            if not event.key in KEYPRESS:
                KEYPRESS.append(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            KEYDOWN.append(event.button)
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.KEYUP:
            KEYUP.append(event.key)
            if event.key in KEYPRESS:
                KEYPRESS.remove(event.key)
def Mouse():
    x, y = pygame.mouse.get_pos()
    if fullscreen:
        # zoom_surface=(surfaceW/fullscreenW)
        x, y = x * (surfaceW / fullscreenW), y * (surfaceH / fullscreenH)
    return x, y

def print_surface():
    global surface
    if fullscreen:
        zoom_surface=(fullscreenW/surfaceW)*2
        #a=pygame.surfarray.array3d(surface)
        #img = pygame.surfarray.make_surface(a)
        W = fullscreenW
        H = fullscreenH
        img = pygame.surfarray.make_surface(pygame.surfarray.array3d(surface))
        img=pygame.transform.scale(img, (int(W*(fullscreenW/surfaceW)),int(H*(fullscreenH/surfaceH))))
        #print(img.get_size())
        surface.blit(img,(0,0))
    pygame.display.update()
###

def set_pixel(x,y,color):
    surface.set_at((x, y), color)


def show_screen():
    #pygame.display.update()
    Keyboard()
    print_surface()

def clear_screen():
    surface.fill((255,255,255))


def get_pixel(x, y):
    return surface.get_at((x, y))

def draw_string(x, y, text, color, size):
    if size=="small":
        taille=8
    message_left(text, taille, color, int(x), int(y), "Lib/Fonts/Calibri.ttf")


clear_screen()
