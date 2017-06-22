from decimal import Decimal, getcontext

from vector import Vector
from line import Line


getcontext().prec = 30


class Plane(object):


    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'
    SYSTEM_EQUATIONS_IS_INCONSISTENT_MSG = 'This system of equations is inconsistent'


    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
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
            initial_index = Plane.first_nonzero_index(n)
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
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


    def is_parallel_to(self, p):
        return self.normal_vector.is_parallel_to(p.normal_vector)


    def __eq__(self, p):
        if not self.is_parallel_to(p):
            return False

        link = self.basepoint.minus(p.basepoint)
        return link.is_orthogonal_to(self.normal_vector)


    def times_scalar(self, c):
        return Plane(
            self.normal_vector.times_scalar(c),
            self.constant_term * c
        )


    def plus(self, p):
        return Plane(
            self.normal_vector.plus(p.normal_vector),
            self.constant_term + p.constant_term
        )


    def intersection_with_arr(self, arr_p):
        # assume all same dimension
        # assume unique intersection point or inconsistent
        # assume dimension == number of equations

        equations = [self] + arr_p
        Plane.print_equations(equations, 'BEFORE')

        try:
            Plane.iterate_for_intersections(equations, False)
            Plane.print_equations(equations, 'PARTWAY')

            Plane.iterate_for_intersections(equations, True)
            Plane.print_equations(equations, 'AFTER')

            Plane.normalize_for_intersections(equations)
            Plane.print_equations(equations, 'FINAL')

            return Vector([e.constant_term for e in equations])

        except Exception as e:
            Plane.print_equations(equations, 'FAILED')

            if str(e) == self.SYSTEM_EQUATIONS_IS_INCONSISTENT_MSG:
                return None
            else:
                return str(e)


    @staticmethod
    def print_equations(equations, title):
        print title

        for e in equations:
            print e

        print


    @staticmethod
    def iterate_for_intersections(equations, reverse):
        eq_range = range(len(equations))

        for i in eq_range:
        
            # TODO: Determine if this swapping might ever need to happen on the reversed iteration, and if so, how to support that here.
            if equations[i].normal_vector.coordinates[i] == 0:
                equation_to_move_down = equations[i]
                equations[i] = equations[i+1]
                equations[i+1] = equation_to_move_down
                
            for j in eq_range:
#                 print 'I=' + str(i) + ' J=' + str(j)
                if (not reverse and i < j) or (reverse and j < i):
#                     print 'YES'
                    cancel_first_term = equations[i].normal_vector.coordinates[i]
                    
                    cancel_second_term = equations[j].normal_vector.coordinates[i]
                    cancel_scalar = -1 * cancel_second_term / cancel_first_term

                    eq_doing_canceling = equations[i].times_scalar(cancel_scalar)
                    eq_to_be_canceled = equations[j]

                    eq_canceled = eq_to_be_canceled.plus(eq_doing_canceling)
                    equations[j] = eq_canceled

                    coordinates_are_zero = [e==0 for e in eq_canceled.normal_vector.coordinates]
                    if reduce( (lambda a,b: a and b), coordinates_are_zero ):
                        if eq_canceled.constant_term == 0:
                            raise Exception('EQUATIONS RESOLVE TO AN EQUALITY')
                        else:
                            raise Exception(Plane.SYSTEM_EQUATIONS_IS_INCONSISTENT_MSG)
#                 else:
#                     print 'NO'


    @staticmethod
    def normalize_for_intersections(equations):
        for i, eq in enumerate(equations):
            coordinates = list(eq.normal_vector.coordinates)            
            normalizer = 1 / coordinates[i]

            coordinates[i] = coordinates[i] * normalizer
            eq.normal_vector = Vector(coordinates)

            eq.constant_term = eq.constant_term * normalizer


    def intersection_with(self, p):
        if self == p:
            return self
        elif self.is_parallel_to(p):
            return None
        else:
            return Line()


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
