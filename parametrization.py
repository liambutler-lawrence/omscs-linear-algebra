from decimal import Decimal, getcontext

from vector import Vector


getcontext().prec = 30


class Parametrization(object):


    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = 'The basepoint and direction vectors should all live in the same dimension'


    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        equations = ['Parametrization:']

        for current_var in range(self.dimension):
            constant = self.basepoint.coordinates[current_var]
            rounded_constant = round(constant, 3)
            
            constant_term = '{}'.format(rounded_constant)
            equation_terms = [constant_term]

            for (vector_index, vector) in enumerate(self.direction_vectors):
                coefficient = vector.coordinates[current_var]
                rounded_coefficient = round(coefficient, 3)

                coefficient_term = '{} t_{}'.format(rounded_coefficient, vector_index + 1)
                equation_terms.append(coefficient_term)

            equation_right_side = ' + '.join(equation_terms)
            current_equation = 'x_{} = {}'.format(current_var + 1, equation_right_side)
            equations.append(current_equation)

        description = '\n'.join(equations)
        return description
