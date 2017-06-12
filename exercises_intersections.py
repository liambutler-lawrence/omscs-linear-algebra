from exercise_utilities import *
from line import *


def print_intersection(v1, v2):
    try:
        print v1.intersection_with(v2)
    except Exception as e:
        if (str(e) == Line.NO_UNIQUE_INTERSECTION_COINCIDENT_LINES or
            str(e) == Line.NO_UNIQUE_INTERSECTION_PARALLEL_LINES):
            print e
        else:
            raise e


print_info('BEGIN')


print_quiz('Coding Functions for Lines')

print_question('Intersection 1')
print_intersection(Line(Vector([4.046, 2.836]), 1.21), Line(Vector([10.115, 7.09]), 3.025))

print_question('Intersection 2')
print_intersection(Line(Vector([7.204, 3.182]), 8.68), Line(Vector([8.172, 4.114]), 9.883))

print_question('Intersection 3')
print_intersection(Line(Vector([1.182, 5.562]), 6.744), Line(Vector([1.773, 8.343]), 9.525))


print_info('END')
