taille=8

def subsurface(img,x,y,w,h):
    return [i[x:x+w] for i in(img[y:y+h])]

def FloorType(part):
    Parts=[]
    Sprites=[]
    for x in range(0,taille*2,taille):
        for y in range(0,taille*3,taille):
            Parts.append(subsurface(part,x,y,taille,taille))
    IDs = [ (5, 4, 2, 1),(3, 4, 2, 1),(5, 4, 3, 1),(3, 4, 3, 1),(5, 4, 2, 3),(3, 4, 2, 3),(5, 4, 3, 3),(3, 4, 3, 3),(5, 3, 2, 1),(3, 3, 2, 1),(5, 3, 3, 1),(3, 3, 3, 1),(5, 3, 2, 3),(3, 3, 2, 3),(5, 3, 3, 3),(3, 3, 3, 3),(2, 1, 2, 1),(2, 1, 3, 1),(2, 1, 2, 3),(2, 1, 3, 3),(4, 4, 1, 1),(4, 4, 1, 3),(4, 3, 1, 1),(4, 3, 1, 3),(5, 4, 5, 4),(5, 3, 5, 4),(3, 4, 5, 4),(3, 3, 5, 4),(5, 5, 2, 2),(3, 5, 2, 2),(5, 5, 3, 2),(3, 5, 3, 2),(2, 1, 5, 4),(4, 5, 1, 2),(0, 1, 1, 1),(0, 1, 1, 3),(4, 4, 4, 4),(4, 3, 0, 4),(5, 5, 5, 0),(3, 5, 5, 0),(2, 2, 2, 2),(2, 2, 3, 2),(1, 1, 0, 4),(1, 2, 1, 2),(2, 2, 5, 0),(4, 5, 0, 5),(0, 0, 0, 0),(0, 0, 0, 0)]
    
    for Index,part in enumerate(IDs):
        i1,i2,i3,i4 = Parts[part[0]],Parts[part[1]],Parts[part[2]],Parts[part[3]]
        HG = [i[:taille//2] for i in(i1[:taille//2])]
        HD = [i[taille//2:] for i in(i3[:taille//2])]
        BG = [i[:taille//2] for i in(i2[taille//2:])]
        BD = [i[taille//2:] for i in(i4[taille//2:])]
        H= [HG[i]+HD[i] for i in range(len(HG))]
        B= [BG[i]+BD[i] for i in range(len(BG))]
        IMG = H+B
        Sprites.append(IMG)
    return Sprites

def WaterfallType(part):
    IDs=[(5, 4, 2, 1),(2, 1, 2, 1),(3, 3, 3, 3),(2, 1, 3, 3)]
    
    Parts=[]
    Sprites=[]
    for x in range(0,taille*2,taille):
        for y in range(0,taille*3,taille):
            Parts.append(subsurface(part,x,y,taille,taille))
    for Index,part in enumerate(IDs):
        i1,i2,i3,i4 = Parts[part[0]],Parts[part[1]],Parts[part[2]],Parts[part[3]]
        HG = [i[:taille//2] for i in(i1[:taille//2])]
        HD = [i[taille//2:] for i in(i3[:taille//2])]
        BG = [i[:taille//2] for i in(i2[taille//2:])]
        BD = [i[taille//2:] for i in(i4[taille//2:])]
        H= [HG[i]+HD[i] for i in range(len(HG))]
        B= [BG[i]+BD[i] for i in range(len(BG))]
        IMG = H+B
        Sprites.append(IMG)
    return Sprites

def WallType(part):#2*2
    IDs=[(3, 2, 1, 0), (1, 0, 1, 0), (2, 2, 0, 0), (0, 0, 0, 0), (3, 2, 3, 2), (1, 0, 3, 2), (2, 2, 2, 2), (0, 0, 2, 2), (3, 3, 1, 1), (1, 1, 1, 1), (2, 3, 0, 1), (0, 1, 0, 1), (3, 3, 3, 3), (1, 1, 3, 3), (2, 3, 2, 3), (0, 1, 2, 3)]

    Parts=[]
    Sprites=[]
    for x in range(0,taille*2,taille):
        for y in range(0,taille*2,taille):
            Parts.append(subsurface(part,x,y,taille,taille))
    for Index,part in enumerate(IDs):
        i1,i2,i3,i4 = Parts[part[0]],Parts[part[1]],Parts[part[2]],Parts[part[3]]
        HG = [i[:taille//2] for i in(i1[:taille//2])]
        HD = [i[taille//2:] for i in(i3[:taille//2])]
        BG = [i[:taille//2] for i in(i2[taille//2:])]
        BD = [i[taille//2:] for i in(i4[taille//2:])]
        H= [HG[i]+HD[i] for i in range(len(HG))]
        B= [BG[i]+BD[i] for i in range(len(BG))]
        IMG = H+B
        Sprites.append(IMG)
    return Sprites
