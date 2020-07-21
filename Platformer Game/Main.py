import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
from RectangleCollision import collision

Texture = 'Textures/'
Level = 0
# Window
window = pyglet.window.Window(caption='Platformer Game' ,width=600,height=600)
window.set_location(window.screen.width//2-window.width//2, window.screen.height//2-window.height//2)
window.set_icon(pyglet.image.load(Texture+ 'Icon.ico'))

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Key handler
key_handler = key.KeyStateHandler()
window.push_handlers(key_handler)

# Mouse handler
mouse_handler = mouse.MouseStateHandler()
window.push_handlers(mouse_handler)
# Start menu True or False
Start = True

# Object
Base = pyglet.graphics.Batch()
Level0 = pyglet.graphics.Batch()
Level1 = pyglet.graphics.Batch()
Level2 = pyglet.graphics.Batch()
# Start Menu
StartButton = pyglet.image.load(Texture+ 'Start button.png')
StartLabel = pyglet.text.Label('Platformer game', x=50,y=500,color=(0,128,0,255), font_size=50)
# Player
PlayerImage1 = pyglet.image.load(Texture+ 'Player=Left.png')
PlayerImage2 = pyglet.image.load(Texture+ 'Player=Right.png')
Player = pyglet.sprite.Sprite(PlayerImage2 ,x=100,y=200)
PlayerOldPosY = 0
Jump = False
# Blocks
BlockImage1 = pyglet.image.load(Texture+ 'Grass.png')
# Base
BBlock1 = pyglet.sprite.Sprite(BlockImage1 ,x=0,y=100, batch=Base)
BBlock2 = pyglet.sprite.Sprite(BlockImage1 ,x=32,y=100, batch=Base)
BBlock3 = pyglet.sprite.Sprite(BlockImage1 ,x=64,y=100, batch=Base)
BBlock4 = pyglet.sprite.Sprite(BlockImage1 ,x=96,y=100, batch=Base)
BBlock5 = pyglet.sprite.Sprite(BlockImage1 ,x=128,y=100, batch=Base)
BBlock6 = pyglet.sprite.Sprite(BlockImage1 ,x=160,y=100, batch=Base)
BBlock7 = pyglet.sprite.Sprite(BlockImage1 ,x=192,y=100, batch=Base)
BBlock8 = pyglet.sprite.Sprite(BlockImage1 ,x=224,y=100, batch=Base)
BBlock9 = pyglet.sprite.Sprite(BlockImage1 ,x=256,y=100, batch=Base)
BBlock10 = pyglet.sprite.Sprite(BlockImage1 ,x=288,y=100, batch=Base)
BBlock11 = pyglet.sprite.Sprite(BlockImage1 ,x=320,y=100, batch=Base)
BBlock12 = pyglet.sprite.Sprite(BlockImage1 ,x=352,y=100, batch=Base)
BBlock13 = pyglet.sprite.Sprite(BlockImage1 ,x=384,y=100, batch=Base)
BBlock14 = pyglet.sprite.Sprite(BlockImage1 ,x=416,y=100, batch=Base)
BBlock15 = pyglet.sprite.Sprite(BlockImage1 ,x=448,y=100, batch=Base)
BBlock16 = pyglet.sprite.Sprite(BlockImage1 ,x=480,y=100, batch=Base)
BBlock17 = pyglet.sprite.Sprite(BlockImage1 ,x=512,y=100, batch=Base)
BBlock18 = pyglet.sprite.Sprite(BlockImage1 ,x=544,y=100, batch=Base)
BBlock19 = pyglet.sprite.Sprite(BlockImage1 ,x=576,y=100, batch=Base)
# level1
l1Block1 = pyglet.sprite.Sprite(BlockImage1 ,x=192,y=132, batch=Level1)
l1Block2 = pyglet.sprite.Sprite(BlockImage1 ,x=288,y=196, batch=Level1)
l1Block3 = pyglet.sprite.Sprite(BlockImage1 ,x=384,y=196, batch=Level1)
l1Block4 = pyglet.sprite.Sprite(BlockImage1 ,x=416,y=196, batch=Level1)
l1Block5 = pyglet.sprite.Sprite(BlockImage1 ,x=448,y=196, batch=Level1)
l1Block6 = pyglet.sprite.Sprite(BlockImage1 ,x=544,y=196, batch=Level1)
# level2
l2Block1 = pyglet.sprite.Sprite(BlockImage1 ,x=192,y=164, batch=Level2)
l2Block2 = pyglet.sprite.Sprite(BlockImage1 ,x=256,y=196, batch=Level2)
l2Block3 = pyglet.sprite.Sprite(BlockImage1 ,x=160,y=256, batch=Level2)
l2Block4 = pyglet.sprite.Sprite(BlockImage1 ,x=288,y=288, batch=Level2)
l2Block5 = pyglet.sprite.Sprite(BlockImage1 ,x=416,y=288, batch=Level2)
l2Block6 = pyglet.sprite.Sprite(BlockImage1 ,x=512,y=288, batch=Level2)
l2Block7 = pyglet.sprite.Sprite(BlockImage1 ,x=560,y=352, batch=Level2)
def BlockSolid(BlockX, BlockY):
    global Jump, PlayerOldPosY
    if collision.rectangle(Player.x,Player.y ,BlockX+5,BlockY+30 ,32,32 ,22,2):
        Player.y += 1
        if key_handler[key.W]:
            PlayerOldPosY = Player.y
            Jump = True
    if collision.rectangle(Player.x,Player.y+0.1 ,BlockX,BlockY ,32,32 ,32,2):
        Jump = False
    if collision.rectangle(Player.x,Player.y ,BlockX,BlockY+1 ,32,32 ,2,30):
        Player.x -= 1
    if collision.rectangle(Player.x,Player.y ,BlockX+30,BlockY+1 ,32,32 ,2,30):
        Player.x += 1
# Enemy
EnemyImage1 = pyglet.image.load(Texture+ 'Enemy.png')
# level0
l0Enemy1 = pyglet.sprite.Sprite(EnemyImage1 ,x=220,y=132, batch=Level0)
# level1
l1Enemy1 = pyglet.sprite.Sprite(EnemyImage1 ,x=416,y=228, batch=Level1)
# Goal
GoalImage1 = pyglet.image.load(Texture+ 'Goal.png')
# level0
l0Goal1 = pyglet.sprite.Sprite(GoalImage1 ,x=544,y=132, batch=Level0)
# level1
l1Goal1 = pyglet.sprite.Sprite(GoalImage1 ,x=544,y=228, batch=Level1)
# level2
l2Goal1 = pyglet.sprite.Sprite(GoalImage1 ,x=560,y=384, batch=Level2)
# yoy won
WinLabel = pyglet.text.Label('You have won welldone :)', x=50,y=300,font_size=30)
# Mouse Position
MouseX = 0
MouseY = 0
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global MouseX, MouseY
    MouseX = x
    MouseY = y
@window.event
def on_mouse_motion(x, y, dx, dy):
    global MouseX, MouseY
    MouseX = x
    MouseY = y

# Update function
def update(dt):
    global Start, Jump, Level
    # If Start = True
    if Start == True:
        pyglet.gl.glClearColor(0.5,1,1,0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        if collision.rectangle(MouseX,MouseY ,200,300 ,1,1 ,183,65):

            if mouse_handler[mouse.LEFT]: Start = False

    # If start = False
    if Start == False:
        pyglet.gl.glClearColor(0,1,1,0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        if Player.x >= 569: Player.x -= 1
        if Player.x <= -1: Player.x += 1

        Player.y -= 1

        if key_handler[key.A]:
            Player.x -= 1
            Player.image = PlayerImage1
        if key_handler[key.D]:
            Player.x += 1
            Player.image = PlayerImage2
        if Jump == True:
            Player.y += 3
            if Player.y >= PlayerOldPosY + 80: Jump = False
        BlockSolid(BBlock1.x,BBlock1.y)
        BlockSolid(BBlock2.x,BBlock2.y)
        BlockSolid(BBlock3.x,BBlock3.y)
        BlockSolid(BBlock4.x,BBlock4.y)
        BlockSolid(BBlock5.x,BBlock5.y)
        BlockSolid(BBlock6.x,BBlock6.y)
        BlockSolid(BBlock7.x,BBlock7.y)
        BlockSolid(BBlock8.x,BBlock8.y)
        BlockSolid(BBlock9.x,BBlock9.y)
        BlockSolid(BBlock10.x,BBlock10.y)
        BlockSolid(BBlock11.x,BBlock11.y)
        BlockSolid(BBlock12.x,BBlock12.y)
        BlockSolid(BBlock13.x,BBlock13.y)
        BlockSolid(BBlock14.x,BBlock14.y)
        BlockSolid(BBlock15.x,BBlock15.y)
        BlockSolid(BBlock16.x,BBlock16.y)
        BlockSolid(BBlock17.x,BBlock17.y)
        BlockSolid(BBlock18.x,BBlock18.y)
        BlockSolid(BBlock19.x,BBlock19.y)
        if Level == 1:
            BlockSolid(l1Block1.x,l1Block1.y)
            BlockSolid(l1Block2.x,l1Block2.y)
            BlockSolid(l1Block3.x,l1Block3.y)
            BlockSolid(l1Block4.x,l1Block4.y)
            BlockSolid(l1Block5.x,l1Block5.y)
        if Level == 2:
            BlockSolid(l2Block1.x,l2Block1.y)
            BlockSolid(l2Block2.x,l2Block2.y)
            BlockSolid(l2Block3.x,l2Block3.y)
            BlockSolid(l2Block4.x,l2Block4.y)
            BlockSolid(l2Block5.x,l2Block5.y)
            BlockSolid(l2Block6.x,l2Block6.y)
            BlockSolid(l2Block7.x,l2Block7.y)
        if collision.rectangle(Player.x,Player.y ,l0Enemy1.x,l0Enemy1.y ,32,32 ,32,32) and Level == 0:
                Player.x = 100
                Player.y = 200
        if collision.rectangle(Player.x,Player.y ,l0Goal1.x,l0Goal1.y ,32,32 ,32,32) and Level == 0:
                Player.x = 100
                Player.y = 200
                Level = 1
        if collision.rectangle(Player.x,Player.y ,l1Enemy1.x,l1Enemy1.y ,32,32 ,32,32) and Level == 1:
                Player.x = 100
                Player.y = 200
        if collision.rectangle(Player.x,Player.y ,l1Goal1.x,l1Goal1.y ,32,32 ,32,32) and Level == 1:
                Player.x = 100
                Player.y = 200
                Level = 2
        if collision.rectangle(Player.x,Player.y ,l2Goal1.x,l2Goal1.y ,32,32 ,32,32) and Level == 2:
                Player.x = 100
                Player.y = 200
                Level = 3
# Draw the objects on screen
@window.event
def on_draw():
    window.clear()
    if Start == True:
        StartLabel.draw()
        StartButton.blit(200,300)
    if Start == False:
        Player.draw()
        Base.draw()
        if Level == 0: Level0.draw()
        if Level == 1: Level1.draw()
        if Level == 2: Level2.draw()
        if Level == 3: WinLabel.draw()


# update the update function
pyglet.clock.schedule_interval(update, 1/120)
# Makes it work
pyglet.app.run()