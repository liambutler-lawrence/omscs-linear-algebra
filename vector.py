#!/usr/bin/env python


from math import sqrt, acos, pi
from decimal import Decimal, getcontext


CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
CANNOT_FIND_UNIQUE_PARALLEL_COMPONENT_MSG = 'Cannot find a unique parallel component'
CANNOT_FIND_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'Cannot find a unique orthogonal component'

VECTORS_TO_CROSS_MUST_BE_3D_MSG = 'The vectors to cross must be in the 3rd dimension'
CAN_ONLY_FIND_PARALLELOGRAM_AREA_IN_2D_OR_3D_MSG = 'Can only find parallelogram area for vectors in the 2nd or 3rd dimensions'
CAN_ONLY_FIND_TRIANGLE_AREA_IN_2D_OR_3D_MSG = 'Can only find triangle area for vectors in the 2nd or 3rd dimensions'


getcontext().prec = 30


class Vector(object):


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
        return dot_product**Decimal('0.5')


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


    def cross(self, v):
        if self.dimension != 3 or self.dimension != v.dimension:
            raise ValueError(VECTORS_TO_CROSS_MUST_BE_3D_MSG)

        (x1, y1, z1) = self.coordinates
        (x2, y2, z2) = v.coordinates

        x = (y1 * z2) - (z1 * y2)
        y = (z1 * x2) - (x1 * z2)
        z = (x1 * y2) - (y1 * x2)

        r = Vector([x, y, z])
        print r.is_parallel_to(self)
        print r.is_parallel_to(v)
        print r.is_orthogonal_to(self)
        print r.is_orthogonal_to(v)
        return r


    def area_of_parallelogram_with(self, v):
        try:
            return self.cross(v).magnitude()
            
        except Exception as e:
            if str(e) == VECTORS_TO_CROSS_MUST_BE_3D_MSG:
                if self.dimension == 2 and self.dimension == v.dimension:
                    (self_x, self_y) = self.coordinates
                    (v_x, v_y) = v.coordinates

                    self_in_3d = Vector([self_x, self_y, 0])
                    v_in_3d = Vector([v_x, v_y, 0])

                    return self_in_3d.cross(v_in_3d).magnitude()
                else:
                    raise Exception(CAN_ONLY_FIND_PARALLELOGRAM_AREA_IN_2D_OR_3D_MSG)
            else:
                raise e


    def area_of_triangle_with(self, v):
        try:
            return self.area_of_parallelogram_with(v) / 2

        except Exception as e:
            if str(e) == CAN_ONLY_FIND_PARALLELOGRAM_AREA_IN_2D_OR_3D_MSG:
                raise Exception(CAN_ONLY_FIND_TRIANGLE_AREA_IN_2D_OR_3D_MSG)
            else:
                raise e


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
        return (
            self.is_zero() or 
            v.is_zero() or 
            self.angle_with(v) == pi or 
            self.angle_with(v) == 0
        )


    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance


    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance


    def component_parallel_to(self, b):
        try:
            unit_b = b.normalized()
            return unit_b.times_scalar(self.dot(unit_b))

        except Exception as e:
            if str(e) == CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(CANNOT_FIND_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def component_orthogonal_to(self, b):
        try:
            return self.minus(self.component_parallel_to(b))
            
        except Exception as e:
            if str(e) == CANNOT_FIND_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(CANNOT_FIND_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e
