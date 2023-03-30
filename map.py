from log import *

map =  [
    "WWWWWWWWWWWWWWWWWWWW",
    "....................",
    "WWWWWWWWWWWWWWWWWWW.",
    "....................",
    "....................",
    "WWWWWWWWWWWWWWWWWWWW",
]

_W,_H = W//len(map[0])*2,H//len(map)*2
coords = []
for item in range(0,len(map)):
    for i,j in enumerate(map[item]):
        if j == "W":
            coords.append((i*_W,item*_H))
        
