from exercise_utilities import *
from line import *
from plane import *
from linsys import *


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

print_question('Intersection 2')
print mgep_2_a.intersection_with_arr([mgep_2_b, mgep_2_c])

print_question('Intersection 3')
print mgep_3_a.intersection_with_arr([mgep_3_b, mgep_3_c])


def test(i, system, expression):
    print
    print 'BEFORE test {}: {}'.format(i, system)
    print

    if expression():
        print 'test case {} passed'.format(i)
    else:
        print 'test case {} failed'.format(i)

    print
    print 'AFTER test {}: {}'.format(i, system)
    print


print_quiz('Coding Row Operations')

cro_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
cro_b = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
cro_c = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
cro_d = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

print_question('Test Cases')
cro_s = LinearSystem([cro_a,cro_b,cro_c,cro_d])

cro_s.swap_rows(0,1)
test(1, cro_s, (lambda: cro_s[0] == cro_b and cro_s[1] == cro_a and cro_s[2] == cro_c and cro_s[3] == cro_d))

cro_s.swap_rows(1,3)
test(2, cro_s, (lambda: cro_s[0] == cro_b and cro_s[1] == cro_d and cro_s[2] == cro_c and cro_s[3] == cro_a))

cro_s.swap_rows(3,1)
test(3, cro_s, (lambda: cro_s[0] == cro_b and cro_s[1] == cro_a and cro_s[2] == cro_c and cro_s[3] == cro_d))

cro_s.multiply_coefficient_and_row(1,0)
test(4, cro_s, (lambda: cro_s[0] == cro_b and cro_s[1] == cro_a and cro_s[2] == cro_c and cro_s[3] == cro_d))

cro_s.multiply_coefficient_and_row(-1,2)
test(5, cro_s, (lambda: cro_s[0] == cro_b and
     cro_s[1] == cro_a and
     cro_s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
     cro_s[3] == cro_d))

cro_s.multiply_coefficient_and_row(10,1)
test(6, cro_s, (lambda: cro_s[0] == cro_b and
     cro_s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
     cro_s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
     cro_s[3] == cro_d))

cro_s.add_multiple_times_row_to_row(0,0,1)
test(7, cro_s, (lambda: cro_s[0] == cro_b and
     cro_s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
     cro_s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
     cro_s[3] == cro_d))

cro_s.add_multiple_times_row_to_row(1,0,1)
test(8, cro_s, (lambda: cro_s[0] == cro_b and
     cro_s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
     cro_s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
     cro_s[3] == cro_d))

cro_s.add_multiple_times_row_to_row(-1,1,0)
test(9, cro_s, (lambda: cro_s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
     cro_s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
     cro_s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
     cro_s[3] == cro_d))


print_info('END')
