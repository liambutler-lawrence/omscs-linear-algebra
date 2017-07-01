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
        summary = 'Parametrization:'
        basepoint = 'Basepoint: {}'.format(self.basepoint)
        direction_vectors = ['Direction Vector {}: {}'.format(i+1, v) for i,v in enumerate(self.direction_vectors)]
        
        description = '\n'.join([summary, basepoint] + direction_vectors)
        return description
