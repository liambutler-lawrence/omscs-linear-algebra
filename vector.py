from math import sqrt, acos, pi
from decimal import Decimal, getcontext


getcontext().prec = 30


class Vector(object):


    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    CANNOT_FIND_UNIQUE_PARALLEL_COMPONENT_MSG = 'Cannot find a unique parallel component'
    CANNOT_FIND_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'Cannot find a unique orthogonal component'
    ONLY_DEFINED_IN_2D_AND_3D_MSG = 'Only defined in the 2nd and 3rd dimensions'


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
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


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
        # ranges are always exclusive; this generates a range containing 2 and 3
        if self.dimension != v.dimension or self.dimension not in range(2, 4):
            raise ValueError(self.ONLY_DEFINED_IN_2D_AND_3D_MSG)

        elif self.dimension == 2:
            zero = (Decimal('0'),)
            (x1, y1, z1) = self.coordinates + zero
            (x2, y2, z2) = v.coordinates + zero

        else:
            (x1, y1, z1) = self.coordinates
            (x2, y2, z2) = v.coordinates

        x = (y1 * z2) - (z1 * y2)
        y = (z1 * x2) - (x1 * z2)
        z = (x1 * y2) - (y1 * x2)

        return Vector([x, y, z])


    def area_of_parallelogram_with(self, v):
        return self.cross(v).magnitude()


    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')


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
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
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
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_FIND_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def component_orthogonal_to(self, b):
        try:
            return self.minus(self.component_parallel_to(b))

        except Exception as e:
            if str(e) == self.CANNOT_FIND_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.CANNOT_FIND_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e
