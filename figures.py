import numpy as np
from intercept import Intercept


class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material
        self.type = "None"

    def ray_intersect(self, orig, dir):
        return None
    
class Sphere(Shape):
    def __init__(self, position, radius, material):
        super().__init__(position, material)
        self.radius = radius
        self.type = "Sphere"

    def ray_intersect(self, orig, direction):
        orig = np.array(orig)
        direction = np.array(direction)

        center = self.position
        radius = self.radius

        L = center - orig
        tca = np.dot(L, direction)


        d2 = np.dot(L, L) - (tca*tca)
        if d2 > (radius*radius):
            return None

        thc = np.sqrt((radius*radius) - d2)

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0 and t1 < 0:
            return None
        
        t = t0 if t0 > 0 else t1
        
        
        P = orig + direction * t

        nP = (P - center) / radius
        nP = nP / np.linalg.norm(nP)

        return Intercept(point=P, normal=nP, distance=t, rayDirection = direction, obj=self)
