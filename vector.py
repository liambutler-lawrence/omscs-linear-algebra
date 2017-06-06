#!/usr/bin/env python


from math import sqrt
from math import acos
from math import pi


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def magnitude(self):
        dot_product = self.dot(self)
        return sqrt(dot_product)


    def normalized(self):
        try:
            inverse_magnitude = 1./self.magnitude()
            return self.times_scalar(inverse_magnitude)
            
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


    def plus(self, v):
        if self.dimension != v.dimension:
            raise ValueError('The vectors to add must be in the same dimension')

        sum = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(sum)


    def minus(self, v):
        if self.dimension != v.dimension:
            raise ValueError('The vectors to subtract must be in the same dimension')

        difference = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(difference)


    def times_scalar(self, c):
        product = [c*x for x in self.coordinates]
        return Vector(product)


    def dot(self, v):
        coordinates_multiplied = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(coordinates_multiplied)


    def angle_from(self, v):
        try:
            dot_product = self.normalized().dot(v.normalized())
            return acos(dot_product)
            
        except Exception:
            raise Exception('Cannot calculate the angle from/to the zero vector')


    def angle_degrees_from(self, v):
        angle_radians = self.angle_from(v)
        return angle_radians * 180 / pi
