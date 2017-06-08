#!/usr/bin/env python


from math import sqrt, acos, pi
from decimal import Decimal, getcontext


getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        return Decimal(sqrt(dot_product))


    def normalized(self):
        try:
            inverse_magnitude = Decimal('1.0')/self.magnitude()
            return self.times_scalar(inverse_magnitude)
            
        except ZeroDivisionError:
            raise Exception(CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


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
        product = [Decimal(c)*x for x in self.coordinates]
        return Vector(product)


    def dot(self, v):
        coordinates_multiplied = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(coordinates_multiplied)


    def angle_with(self, v, in_degrees=False):
        try:
            dot_product = self.normalized().dot(v.normalized())
            angle_in_radians = acos(dot_product)

            if in_degrees:
                radians_to_degrees = 180. / pi
                return angle_in_radians * radians_to_degrees
            else:
                return angle_in_radians
            
        except Exception as e:
            if str(e) == CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot calculate an angle with the zero vector')
            else:
                raise e


    def is_parallel_to(self, v, tolerance=1e-10):
        try:
            remainders = [x/y for x,y in zip(self.coordinates, v.coordinates)]
            return reduce( (lambda x,y: abs(x-y) < tolerance), remainders )
        except ZeroDivisionError:
            return True


    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance
