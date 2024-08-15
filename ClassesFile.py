import pygame as game
import numpy
class BOUNDARY:
    def __init__(self, x1, y1, x2, y2, color, Layer):
        self.p1 = game.Vector2(x1, y1)
        self.p2 = game.Vector2(x2, y2)
        self.color = color
        self.layer = Layer

    def Draw(self):
        game.draw.line(self.layer, self.color, self.p1, self.p2)

class POINT:
    def __init__(self, center, Layer):
        self.layer = Layer
        self.center = center
        self.radius = 3.5
        self.draging = False
        self.offsetxpos = 0
        self.offsetypos = 0
        self.color = "white"
        self.updateHitbox()
        self.rays = []

        #rays:
        for angle in range(-30, 30):
            self.rays.append(RAY(self.center[0], self.center[1], angle, self.layer))

    def UpdateRays(self):
        for ray in self.rays:
            ray.position.x = self.center[0]
            ray.position.y = self.center[1]

    def updateHitbox(self):
        self.hitbox = game.rect.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius*2, self.radius*2)

    def Draw(self):
        game.draw.circle(self.layer, self.color, tuple(self.center), self.radius)
        #game.draw.rect(Canvas, "light green", self.hitbox, 1)

    def CheckWall(self, walls : list, color):
        self.position = game.Vector2(self.center[0], self.center[1])
        for ray in self.rays:
            closestPoint = self.position
            closestDist = numpy.Infinity
            for wall in walls:
                Intersect = ray.CheckCasting(wall)
                if Intersect != None:
                    distance = self.position.distance_to(Intersect)
                    if distance < closestDist:
                        closestDist = distance
                        closestPoint = Intersect
            game.draw.line(self.layer, color, tuple(self.center), closestPoint)

class RAY:
    def __init__(self, x, y, angle, Layer):
        self.position = game.Vector2(x, y)
        self.angle = angle
        self.direction = game.Vector2(numpy.cos(numpy.deg2rad(self.angle)), numpy.sin(numpy.deg2rad(self.angle)))
        self.layer = Layer
        self.color = "green"

    def Draw(self):
        game.draw.line(self.layer, self.color, self.position, (self.position + (self.direction * 10)))

    def SetDirection(self, x, y):
        self.direction.x = x - self.position.x
        self.direction.y = y - self.position.y
        self.direction.normalize_ip()

    def CheckCasting(self, Boundry : BOUNDARY):
        x1 = Boundry.p1.x
        y1 = Boundry.p1.y
        x2 = Boundry.p2.x
        y2 = Boundry.p2.y

        x3 = self.position.x
        y3 = self.position.y
        x4 = self.position.x + self.direction.x
        y4 = self.position.y + self.direction.y

        #MATH TIME:

        denom = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
        if denom == 0:
            return
        
        tValue = (((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4))) / denom

        uValue = -((((x1 - x2) * (y1 - y3)) - ((y1 - y2) * (x1 - x3))) / denom)

        if tValue > 0 and tValue < 1 and uValue > 0:
            IntersectionPoint = game.Vector2(0, 0)
            IntersectionPoint.x = x1 + tValue*(x2 - x1)
            IntersectionPoint.y = y1 + tValue*(y2 - y1)

            return IntersectionPoint
        else:
            return None