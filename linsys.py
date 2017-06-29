from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane


getcontext().prec = 30


class LinearSystem(object):


    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'
    NO_NONZERO_EQS_BELOW_MSG = 'No equations below specified row have a non-zero coefficient for the specified variable'


    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        c = Decimal(coefficient)

        result_vector = self[row].normal_vector.times_scalar(c)
        result_constant = self[row].constant_term * c

        self[row] = Plane(result_vector, result_constant)


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        c = Decimal(coefficient)

        # Multiply equation 1 by coefficient
        vector_to_add = self[row_to_add].normal_vector.times_scalar(c)
        constant_to_add = self[row_to_add].constant_term * c
        
        # Add equations 1 and 2
        result_vector = self[row_to_be_added_to].normal_vector.plus(vector_to_add)
        result_constant = self[row_to_be_added_to].constant_term + constant_to_add

        # Replace equation 2 with the result
        self[row_to_be_added_to] = Plane(result_vector, result_constant)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def compute_rref(self):
        result_system = self.compute_triangular_form()
        
        num_equations = len(result_system)
        num_variables = result_system.dimension

        current_var = num_variables - 1
        current_eq = num_equations - 1

        while current_eq >= 0 and current_var >= 0:
            current_coe = MyDecimal(result_system[current_eq].normal_vector.coordinates[current_var])

            if current_coe.is_near_zero():
                current_eq -= 1
                continue

            result_system.clear_coe_in_preceding_eqs(current_eq, current_var)

            inverted_current_coe = Decimal('1') / current_coe
            result_system.multiply_coefficient_and_row(inverted_current_coe, current_eq)

            current_var -= 1

        return result_system


    def compute_triangular_form(self):
        result_system = deepcopy(self)

        num_equations = len(result_system)
        num_variables = result_system.dimension

        current_var = 0

        for current_eq in range(num_equations):

            while current_var < num_variables:
                current_coe = MyDecimal(result_system[current_eq].normal_vector.coordinates[current_var])

                if current_coe.is_near_zero():
                    try:
                        result_system.swap_for_next_eq_with_nonzero_coe(current_eq, current_var)

                    except Exception as e:
                        if str(e) == self.NO_NONZERO_EQS_BELOW_MSG:
                            current_var += 1
                            continue

                result_system.clear_coe_in_remaining_eqs(current_eq, current_var)

                current_var += 1
                break

        return result_system


    def swap_for_next_eq_with_nonzero_coe(self, eq_to_swap, var_with_zero_coe):
        num_equations = len(self)
        first_nonzero_vars = self.indices_of_first_nonzero_terms_in_each_row()

        for current_eq in range(eq_to_swap + 1, num_equations):

            if first_nonzero_vars[current_eq] <= var_with_zero_coe:
                self.swap_rows(eq_to_swap, current_eq)
                return

        raise Exception(self.NO_NONZERO_EQS_BELOW_MSG)


    def clear_coe_in_remaining_eqs(self, eq_to_do_clearing, var_to_clear):
        num_equations = len(self)
        coe_to_do_clearing = self[eq_to_do_clearing].normal_vector.coordinates[var_to_clear]

        for eq_to_be_cleared in range(eq_to_do_clearing + 1, num_equations):
            coe_to_be_cleared = self[eq_to_be_cleared].normal_vector.coordinates[var_to_clear]

            scalar_to_do_clearing = coe_to_be_cleared / coe_to_do_clearing * -1
            self.add_multiple_times_row_to_row(scalar_to_do_clearing, eq_to_do_clearing, eq_to_be_cleared)


    def clear_coe_in_preceding_eqs(self, eq_to_do_clearing, var_to_clear):
        coe_to_do_clearing = self[eq_to_do_clearing].normal_vector.coordinates[var_to_clear]

        for eq_to_be_cleared in reversed(range(eq_to_do_clearing)):
            coe_to_be_cleared = self[eq_to_be_cleared].normal_vector.coordinates[var_to_clear]

            scalar_to_do_clearing = coe_to_be_cleared / coe_to_do_clearing * -1
            self.add_multiple_times_row_to_row(scalar_to_do_clearing, eq_to_do_clearing, eq_to_be_cleared)


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
