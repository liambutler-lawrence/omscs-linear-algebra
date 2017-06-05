#!/usr/bin/env python

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


    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]

        sum = 0
        for x in coordinates_squared:
            sum += x

        return sum**0.5


    def normalization(self):
        inverse_magnitude = 1 / self.magnitude()
        return self.times_scalar(inverse_magnitude)
