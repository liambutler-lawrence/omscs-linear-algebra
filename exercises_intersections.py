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
print LinearSystem([gep_1_a, gep_1_b, gep_1_c]).compute_solution()


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
print LinearSystem([mgep_1_a, mgep_1_b, mgep_1_c]).compute_solution()

print_question('Intersection 2')
print LinearSystem([mgep_2_a, mgep_2_b, mgep_2_c]).compute_solution()

print_question('Intersection 3')
print LinearSystem([mgep_3_a, mgep_3_b, mgep_3_c]).compute_solution()


def test(i, system, expression):
    print

    if expression():
        print 'test case {} PASSED: {}'.format(i, system)
    else:
        print 'test case {} FAILED: {}'.format(i, system)


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


print_quiz('Coding Triangular Form')

ctf_1_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
ctf_1_b = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')

ctf_2_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
ctf_2_b = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')

ctf_3_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
ctf_3_b = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
ctf_3_c = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
ctf_3_d = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

ctf_4_a = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
ctf_4_b = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
ctf_4_c = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')

print_question('Test Cases')

ctf_s = LinearSystem([ctf_1_a, ctf_1_b]).compute_triangular_form()
test(1, ctf_s, (lambda: ctf_s[0] == ctf_1_a and
                        ctf_s[1] == ctf_1_b))

ctf_s = LinearSystem([ctf_2_a, ctf_2_b]).compute_triangular_form()
test(2, ctf_s, (lambda: ctf_s[0] == ctf_2_a and
                        ctf_s[1] == Plane(constant_term='1')))

ctf_s = LinearSystem([ctf_3_a, ctf_3_b, ctf_3_c, ctf_3_d]).compute_triangular_form()
test(3, ctf_s, (lambda: ctf_s[0] == ctf_3_a and
                        ctf_s[1] == ctf_3_b and
                        ctf_s[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
                        ctf_s[3] == Plane()))

ctf_s = LinearSystem([ctf_4_a, ctf_4_b, ctf_4_c]).compute_triangular_form()
test(4, ctf_s, (lambda: ctf_s[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
                        ctf_s[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
                        ctf_s[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')))


print_quiz('Coding RREF')

crref_1_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
crref_1_b = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')

crref_2_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
crref_2_b = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')

crref_3_a = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
crref_3_b = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
crref_3_c = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
crref_3_d = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

crref_4_a = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
crref_4_b = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
crref_4_c = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')

print_question('Test Cases')

crref_1_s = LinearSystem([crref_1_a, crref_1_b]).compute_rref()
test(1, crref_1_s, (lambda: crref_1_s[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
                            crref_1_s[1] == crref_1_b))

crref_2_s = LinearSystem([crref_2_a, crref_2_b]).compute_rref()
test(2, crref_2_s, (lambda: crref_2_s[0] == crref_2_a and
                            crref_2_s[1] == Plane(constant_term='1')))
                          
crref_3_s = LinearSystem([crref_3_a, crref_3_b, crref_3_c, crref_3_d]).compute_rref()
test(3, crref_3_s, (lambda: crref_3_s[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
                            crref_3_s[1] == crref_3_b and
                            crref_3_s[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
                            crref_3_s[3] == Plane()))

crref_4_s = LinearSystem([crref_4_a, crref_4_b, crref_4_c]).compute_rref()
test(4, crref_4_s, (lambda: crref_4_s[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
                            crref_4_s[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
                            crref_4_s[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))))


print_quiz('Coding GE Solution')

cges_1_a = Plane(normal_vector=Vector(['5.862','1.178','-10.366']), constant_term='-8.15')
cges_1_b = Plane(normal_vector=Vector(['-2.931','-0.589','5.183']), constant_term='-4.075')

cges_2_a = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.133')
cges_2_b = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.795')
cges_2_c = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')

cges_3_a = Plane(normal_vector=Vector(['5.262','2.739','-9.878']), constant_term='-3.441')
cges_3_b = Plane(normal_vector=Vector(['5.111','6.358','7.638']), constant_term='-2.152')
cges_3_c = Plane(normal_vector=Vector(['2.016','-9.924','-1.367']), constant_term='-9.278')
cges_3_d = Plane(normal_vector=Vector(['2.167','-13.543','-18.883']), constant_term='-10.567')

print_question('1')
print LinearSystem([cges_1_a, cges_1_b]).compute_solution()

print_question('2')
print LinearSystem([cges_2_a, cges_2_b, cges_2_c]).compute_solution()

print_question('3')
print LinearSystem([cges_3_a, cges_3_b, cges_3_c, cges_3_d]).compute_solution()


print_quiz('Coding Parametrization')

cp_1_a = Plane(normal_vector=Vector(['0.786','0.786','0.588']), constant_term='-0.714')
cp_1_b = Plane(normal_vector=Vector(['-0.138','-0.138','0.244']), constant_term='0.319')

cp_2_a = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113')
cp_2_b = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.775')
cp_2_c = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')

cp_3_a = Plane(normal_vector=Vector(['0.935','1.76','-9.365']), constant_term='-9.955')
cp_3_b = Plane(normal_vector=Vector(['0.187','0.352','-1.873']), constant_term='-1.991')
cp_3_c = Plane(normal_vector=Vector(['0.374','0.704','-3.746']), constant_term='-3.982')
cp_3_d = Plane(normal_vector=Vector(['-0.561','-1.056','5.619']), constant_term='5.973')

print_question('1') # Input is incorrect for this exercise
print LinearSystem([cp_1_a, cp_1_b]).compute_solution()

print_question('2')
print LinearSystem([cp_2_a, cp_2_b, cp_2_c]).compute_solution()

print_question('3')
print LinearSystem([cp_3_a, cp_3_b, cp_3_c, cp_3_d]).compute_solution()


print_info('END')
