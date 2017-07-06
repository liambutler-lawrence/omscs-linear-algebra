from decimal import Decimal, getcontext

from hyperplane import Hyperplane
from line import Line


getcontext().prec = 30


class Plane(Hyperplane):


    def __init__(self, normal_vector=None, constant_term=None):
        super(Plane, self).__init__(normal_vector, constant_term, dimension=3)


    def intersection_with(self, p):
        if self == p:
            return self
        elif self.is_parallel_to(p):
            return None
        else:
            return Line()
