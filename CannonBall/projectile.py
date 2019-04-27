from math import sin, cos, radians 

class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height 
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel 
        yveli =self.yvel - 9.8 * time 
        self.ypos = self.ypos + time * (self.yvel + yveli) / 2.0 
        self.yvel = yveli 

    def getY(self):
        return self.ypos 

    def getX(self):
        return self.xpos 
