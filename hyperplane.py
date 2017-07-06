from decimal import Decimal, getcontext

from vector import Vector


getcontext().prec = 30


class Hyperplane(object):


    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'
    DIM_PROVIDED_MUST_MATCH_NORMAL_VEC_DIM = 'The dimension provided must be equal to the normal vector\'s dimension'
    EITHER_DIM_OR_NORMAL_VEC_MUST_BE_PROVIDED = 'Either the dimension or the normal vector of the hyperplane must be provided'


    def __init__(self, normal_vector=None, constant_term=None, dimension=None):
        if not dimension and not normal_vector:
            raise Exception(self.EITHER_DIM_OR_NORMAL_VEC_MUST_BE_PROVIDED)
            
        elif not normal_vector:
            zero_vector = ['0'] * dimension
            normal_vector = Vector(zero_vector)
            
        elif not dimension:
            dimension = normal_vector.dimension
            
        else:
            if not dimension == normal_vector.dimension:
                raise Exception(self.DIM_PROVIDED_MUST_MATCH_NORMAL_VEC_DIM)

        self.normal_vector = normal_vector
        self.dimension = dimension

        if not constant_term:
            constant_term = '0'
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Hyperplane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Hyperplane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Hyperplane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Hyperplane.NO_NONZERO_ELTS_FOUND_MSG)


    def is_parallel_to(self, p):
        return self.normal_vector.is_parallel_to(p.normal_vector)


    def __eq__(self, p):
        if not self.is_parallel_to(p):
            return False

        if self.basepoint is None and p.basepoint is None:
            return True
        elif self.basepoint is None or p.basepoint is None:
            return False

        link = self.basepoint.minus(p.basepoint)
        return link.is_orthogonal_to(self.normal_vector)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
