import Tuiles
import Images

taille=8

def subsurface(img,x,y,w,h):
    return [i[x:x+w] for i in(img[y:y+h])]

All = []

for y in range(0,16*taille,taille):
    for x in range(0,8*taille,taille):
        All.append(subsurface(Images.Tilesheet_B,x,y,taille,taille))

for y in range(0,16*taille,taille):
    for x in range(8*taille,8*taille*2,taille):
        All.append(subsurface(Images.Tilesheet_B,x,y,taille,taille))

for y in range(0,16*taille,taille):
    for x in range(0,8*taille,taille):
        All.append(subsurface(Images.Tilesheet_C,x,y,taille,taille))

for y in range(0,16*taille,taille):
    for x in range(8*taille,8*taille*2,taille):
        All.append(subsurface(Images.Tilesheet_C,x,y,taille,taille))

while len(All)<1536:
    All.append(None)


for y in range(0,16*taille,taille):
    for x in range(0,8*taille,taille):
        All.append(subsurface(Images.Tilesheet_A5,x,y,taille,taille))

while len(All)<2048:
    All.append(None)

All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,0,0,taille*2,taille*3))
All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,0,taille*3,taille*2,taille*3))

All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,taille*6,0,taille*2,taille*3))
All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,taille*6,taille*3,taille*2,taille*3))

All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,taille*8,0,taille*2,taille*3))

All+=Tuiles.WaterfallType(subsurface(Images.Tilesheet_A1,taille*14,0,taille*2,taille*3))
All+=[None]*(47-3)

All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,taille*8,taille*3,taille*2,taille*3))

All+=Tuiles.WaterfallType(subsurface(Images.Tilesheet_A1,taille*14,taille*3,taille*2,taille*3))
All+=[None]*(47-3)



All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,0,taille*6,taille*2,taille*3))

All+=Tuiles.WaterfallType(subsurface(Images.Tilesheet_A1,taille*6,taille*6,taille*2,taille*3))
All+=[None]*(47-3)

All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,0,taille*9,taille*2,taille*3))

All+=Tuiles.WaterfallType(subsurface(Images.Tilesheet_A1,taille*6,taille*9,taille*2,taille*3))
All+=[None]*(47-3)

All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,taille*8,taille*6,taille*2,taille*3))
All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A1,taille*8,taille*9,taille*2,taille*3))

All+=Tuiles.WaterfallType(subsurface(Images.Tilesheet_A1,taille*14,taille*6,taille*2,taille*3))
All+=[None]*(47-3)
All+=Tuiles.WaterfallType(subsurface(Images.Tilesheet_A1,taille*14,taille*9,taille*2,taille*3))
All+=[None]*(47-3)


for y in range(0,12*taille,taille*3):
    for x in range(0,16*taille,taille*2):
        All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A2,x,y,taille*2,taille*3)) 

for y in range(0,8*taille,taille*2):
    for x in range(0,16*taille,taille*2):
        All+=Tuiles.WallType(subsurface(Images.Tilesheet_A3,x,y,taille*2,taille*2))
        All+=[None]*(47-15)
        


for x in range(0,16*taille,taille*2):
        All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A4,x,taille*5*0,taille*2,taille*3)) 
for x in range(0,16*taille,taille*2):
        All+=Tuiles.WallType(subsurface(Images.Tilesheet_A4,x,taille*3+(taille*5*0),taille*2,taille*2))
        All+=[None]*(47-15)
    
for x in range(0,16*taille,taille*2):
        All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A4,x,taille*5*1,taille*2,taille*3)) 
for x in range(0,16*taille,taille*2):
        All+=Tuiles.WallType(subsurface(Images.Tilesheet_A4,x,taille*3+(taille*5*1),taille*2,taille*2))
        All+=[None]*(47-15)
      
for x in range(0,16*taille,taille*2):
        All+=Tuiles.FloorType(subsurface(Images.Tilesheet_A4,x,taille*5*2,taille*2,taille*3)) 
for x in range(0,16*taille,taille*2):
        All+=Tuiles.WallType(subsurface(Images.Tilesheet_A4,x,taille*3+(taille*5*2),taille*2,taille*2))
        All+=[None]*(47-15)



for i in range(len(All)):
    if All[i]==None:
        All[i] = All[0]
