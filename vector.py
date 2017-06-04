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


    def __add__(self, v):
        if self.dimension != v.dimension:
            raise ValueError('The vectors to add must be in the same dimension')

        sum = []
        for i in range(0, self.dimension):
            sum.append(self.coordinates[i] + v.coordinates[i])

        return Vector(sum)


    def __sub__(self, v):
    	if self.dimension != v.dimension:
    		raise ValueError('The vectors to subtract must be in the same dimension')

    	difference = []
    	for i in range(0, self.dimension):
    		difference.append(self.coordinates[i] - v.coordinates[i])

    	return Vector(difference)


    def __mul__(self, scalar):
    	product = []
    	for i in range(0, self.dimension):
    		product.append(self.coordinates[i] * scalar)

    	return Vector(product)
