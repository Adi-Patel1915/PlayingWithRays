import pygame as game
import numpy
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