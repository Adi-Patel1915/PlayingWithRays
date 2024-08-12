import pygame as game
#--------------------
#================================================

class POINT:
    def __init__(self, center : list, Layer):
        self.layer = Layer
        self.center = center
        self.radius = 5
        self.draging = False
        self.offsetxpos = 0
        self.offsetypos = 0
        self.color = "white"
        self.updateHitbox()

    def updateHitbox(self):
        self.hitbox = game.rect.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius*2, self.radius*2)

    def Draw(self):
        game.draw.circle(self.layer, self.color, tuple(self.center), self.radius)
        #game.draw.rect(Canvas, "light green", self.hitbox, 1)

#================================================
#================================================

def MouseActivity(Event):
    if Event.type == game.MOUSEBUTTONDOWN:
        if Event.button == 1:
            return (1, 1)
    elif Event.type == game.MOUSEBUTTONUP:
        if Event.button == 1:
            return (1, -1)
    elif Event.type == game.MOUSEMOTION:
        return (1, 0)
    
#================================================

def Dragger(Point, Events, AlreadyDragging):
        for event in Events:
            tempVal = MouseActivity(event)
            if tempVal == (1, 1):
                mouseXpos, mouseYpos = event.pos
                if Point.hitbox.collidepoint(event.pos):
                    if AlreadyDragging is None:
                        AlreadyDragging = Point
                        Point.draging = True
                    Point.offsetxpos = Point.center[0] - mouseXpos
                    Point.offsetypos = Point.center[1] - mouseYpos
            
            elif tempVal == (1, -1):
                AlreadyDragging = None
                Point.draging = False
            
            elif tempVal == (1, 0):
                if Point.draging:
                    mouseXpos, mouseYpos = event.pos
                    Point.center[0] = mouseXpos + Point.offsetxpos
                    Point.center[1] = mouseYpos + Point.offsetypos
                    Point.updateHitbox()
#================================================
#--------------------
game.init()
Width = 500
Height = 500
Canvas = game.display.set_mode((Width, Height))
game.display.set_caption("Canvas")
Switch = True
Clock = game.time.Clock()
FPS = 144 #FPS here
DraggingPoint = None
pointtest = POINT([250, 250], Canvas)
#--------------------
while Switch:
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            Switch = False

    #Main code here...
    Canvas.fill("black")
    Dragger(pointtest, events, DraggingPoint)
    pointtest.Draw()

    game.display.update()
    Clock.tick(FPS)