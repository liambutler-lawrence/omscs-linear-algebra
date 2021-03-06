from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane
from parametrization import Parametrization


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

        pivot_vars = result_system.indices_of_first_nonzero_terms_in_each_row()

        for current_eq in reversed(range(num_equations)):

            pivot_var = pivot_vars[current_eq]
            if pivot_var < 0:
                continue

            result_system.scale_eq_to_make_coe_equal_one(current_eq, pivot_var)
            result_system.clear_coe_in_preceding_eqs(current_eq, pivot_var)

        return result_system


    def scale_eq_to_make_coe_equal_one(self, eq_to_scale, pivot_var):
        pivot_var_coe = self[eq_to_scale].normal_vector.coordinates[pivot_var]
        pivot_var_inverted_coe = Decimal('1') / pivot_var_coe
        
        self.multiply_coefficient_and_row(pivot_var_inverted_coe, eq_to_scale)


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
                        else:
                            raise e

                result_system.clear_coe_in_remaining_eqs(current_eq, current_var)

                current_var += 1
                break

        return result_system


    def swap_for_next_eq_with_nonzero_coe(self, eq_to_swap, var_with_zero_coe):
        num_equations = len(self)
        first_nonzero_vars = self.indices_of_first_nonzero_terms_in_each_row()

        for current_eq in range(eq_to_swap + 1, num_equations):
            current_eq_first_nonzero_var = first_nonzero_vars[current_eq]

            # If current_eq_first_nonzero_var is less than 0...
            # ...then there are no variables with non-zero coefficients in this equation.
            if 0 <= current_eq_first_nonzero_var and current_eq_first_nonzero_var <= var_with_zero_coe:
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


    def compute_solution(self):
        list_contains = (lambda list, element: list.count(element) > 0)

        rref = self.compute_rref()

        # Get list of pivot var positions 
        pivot_vars = [i for i in rref.indices_of_first_nonzero_terms_in_each_row() if i >= 0]

        try:
            rows = rref.compute_rows_for_parametrization(pivot_vars)
        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG:
                return None
            else:
                raise e

        # Get basepoint vector by slicing the constant term from each equation
        basepoint = Vector([p.constant_term for p in rows])

        # Get direction vectors by slicing "vertically" through the equation list
        rows_coords = [[x * Decimal('-1') for x in p.normal_vector.coordinates] for p in rows]
        columns = [Vector(v) for v in zip(*rows_coords)]

        # Remove direction vectors at pivot var positions
        direction_vectors = [column for column_index, column in enumerate(columns) if not list_contains(pivot_vars, column_index)]

        return Parametrization(basepoint, direction_vectors)


    def compute_rows_for_parametrization(self, pivot_vars):
        list_contains_all_zeros = (lambda list: reduce((lambda a,b: a and b), [MyDecimal(x).is_near_zero() for x in list]))

        rows = deepcopy(self.planes)

        # Get list of free var positions
        all_vars = range(self.dimension)
        free_vars = set(all_vars).difference(set(pivot_vars))

        # Fill out list of equations by inserting an 'x - x = 0' equation for each free var
        for free_var_position in free_vars:
            normal_vector = ['-1' if i == free_var_position else '0' for i in all_vars]
            rows.insert(free_var_position, Plane(Vector(normal_vector), '0'))

        # Check each redundant (0 = 0) equation to make sure it is not an invalid (0 = k) equation
        for redundant_eq in rows[self.dimension:]:
            is_lhs_zero = list_contains_all_zeros(redundant_eq.normal_vector.coordinates)
            is_rhs_zero = MyDecimal(redundant_eq.constant_term).is_near_zero()

            if is_lhs_zero and not is_rhs_zero:
                raise Exception(self.NO_SOLUTIONS_MSG)

        return rows[:self.dimension]


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
