from decimal import Decimal, getcontext

from hyperplane import Hyperplane
from vector import Vector


getcontext().prec = 30


class Line(Hyperplane):


    def __init__(self, normal_vector=None, constant_term=None):
        super(Line, self).__init__(normal_vector, constant_term, dimension=2)


    def intersection_with(self, l):
        try:
            (a, b) = self.normal_vector.coordinates
            (c, d) = l.normal_vector.coordinates

            k1 = self.constant_term
            k2 = l.constant_term

            x = (d * k1) - (b * k2)
            y = (a * k2) - (c * k1)
            denominator = (a * d) - (b * c)

            return Vector([x, y]).divided_by_scalar(denominator)

        except ZeroDivisionError:
            if self == l:
                return self
            else:
                return None
