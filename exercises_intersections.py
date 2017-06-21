from exercise_utilities import *
from line import *
from plane import *


print_info('BEGIN')


print_quiz('Coding Functions for Lines')

print_question('Intersection 1')
print Line(Vector(['4.046', '2.836']), '1.21').intersection_with(Line(Vector(['10.115', '7.09']), '3.025'))

print_question('Intersection 2')
print Line(Vector(['7.204', '3.182']), '8.68').intersection_with(Line(Vector(['8.172', '4.114']), '9.883'))

print_question('Intersection 3')
print Line(Vector(['1.182', '5.562']), '6.744').intersection_with(Line(Vector(['1.773', '8.343']), '9.525'))


print_quiz('Planes in Three Dimensions')

print_question('Intersection 1')
print Plane(Vector(['-0.412', '3.806', '0.728']), '-3.46').intersection_with(Plane(Vector(['1.03', '-9.515', '-1.82']), '8.65'))

print_question('Intersection 2')
print Plane(Vector(['2.611', '5.528', '0.283']), '4.6').intersection_with(Plane(Vector(['7.715', '8.306', '5.342']), '3.76'))

print_question('Intersection 3')
print Plane(Vector(['-7.926', '8.625', '-7.212']), '-7.952').intersection_with(Plane(Vector(['-2.642', '2.875', '-2.404']), '-2.443'))


print_quiz('Gaussian Elimination Practice')

gep_1_a = Plane(Vector(['-1', '1', '1']), '-2')
gep_1_b = Plane(Vector(['1', '-4', '4']), '21')
gep_1_c = Plane(Vector(['7', '-5', '-11']), '0')

print_question('Intersection')
print gep_1_a.intersection_with_arr([gep_1_b, gep_1_c])


print_quiz('More Gaussian Elimination Practice')

mgep_1_a = Plane(Vector(['1', '-2', '1']), '-1')
mgep_1_b = Plane(Vector(['1', '0', '-2']), '2')
mgep_1_c = Plane(Vector(['-1', '4', '-4']), '0')

mgep_2_a = Plane(Vector(['0', '1', '-1']), '2')
mgep_2_b = Plane(Vector(['1', '-1', '1']), '2')
mgep_2_c = Plane(Vector(['3', '-4', '1']), '1')

mgep_3_a = Plane(Vector(['1', '2', '1']), '-1')
mgep_3_b = Plane(Vector(['3', '6', '2']), '1')
mgep_3_c = Plane(Vector(['-1', '-2', '-1']), '1')

print_question('Intersection 1')
print mgep_1_a.intersection_with_arr([mgep_1_b, mgep_1_c])

print_question('Intersection 1')
print mgep_2_a.intersection_with_arr([mgep_2_b, mgep_2_c])

print_question('Intersection 1')
print mgep_3_a.intersection_with_arr([mgep_3_b, mgep_3_c])


print_info('END')
