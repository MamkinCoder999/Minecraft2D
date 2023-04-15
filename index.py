BLOCK_SIDE = 48
WIDTH_BLOCKS = 20
HEIGHT_BLOCKS = 15
WIDTH = WIDTH_BLOCKS * BLOCK_SIDE
HEIGHT = HEIGHT_BLOCKS * BLOCK_SIDE

from tkinter import Tk, Canvas, PhotoImage, NW
from random import randint
tk = Tk()
c = Canvas(tk, bg='#aaffff', width=WIDTH, height=HEIGHT,
           bd=0, highlightthickness=0)
c.pack()
tk.resizable(0, 0)
tk.title('Minecraft2D')

AIR_ID = 0
DIRT_ID = 1
GRASS_ID = 2
STONE_ID = 3
PLANKS_ID = 4
COBBLESTONE_ID = 5
COAL_ORE_ID = 6

textures = {
    AIR_ID: PhotoImage(file='air.png'),
    DIRT_ID: PhotoImage(file='dirt.png'),
    GRASS_ID: PhotoImage(file='grass.png'),
    STONE_ID: PhotoImage(file='stone.png'),
    PLANKS_ID: PhotoImage(file='planks.png'),
    COBBLESTONE_ID: PhotoImage(file='cobblestone.png'),
    COAL_ORE_ID: PhotoImage(file='coal_ore.png'),
}

world_map = [bytearray(b'\0' * HEIGHT_BLOCKS) for x in range(WIDTH_BLOCKS)]

for x in range(WIDTH_BLOCKS):
    for y in range(HEIGHT_BLOCKS):
        c.create_image(x * BLOCK_SIDE, y * BLOCK_SIDE, image=textures[world_map[x][y]], anchor=NW)

def redraw_world():
    for x in range(WIDTH_BLOCKS):
        for y in range(HEIGHT_BLOCKS):
            c.itemconfig(x * HEIGHT_BLOCKS + y + 1, image=textures[world_map[x][y]])
    tk.update()
redraw_world()

block = AIR_ID
def select_block(event):
    global block
    block = int(event.keysym)
def set_block(event):
    x = event.x // BLOCK_SIDE
    y = event.y // BLOCK_SIDE
    world_map[x][y] = block
    redraw_world()
c.bind_all('<Button-1>', set_block)
for i in range(AIR_ID, COAL_ORE_ID + 1):
    c.bind_all('<KeyPress-%s>' %i, select_block)
