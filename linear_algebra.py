from vector import Vector

def print_info(caption):
    print
    print
    print caption + ' LINEAR ALGEBRA QUIZ LOG'
    print

def print_quiz(name):
    print
    print '*****'
    print 'Quiz: ' + name


def print_question(name):
    print
    print name + ':'


print_info('BEGIN')


print_quiz('Plus, Minus, Scalar Multiply')

print_question('1')
print Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111]))

print_question('2')
print Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878]))

print_question('3')
print Vector([1.671, -1.012, -0.318]).times_scalar(7.41)


print_quiz('Coding Magnitude & Direction')

print_question('Magnitude 1')
print Vector([-0.221, 7.437]).magnitude()

print_question('Magnitude 2')
print Vector([8.813, -1.331, -6.247]).magnitude()

print_question('Normalization 1')
print Vector([5.581, -2.136]).normalized()

print_question('Normalization 2')
print Vector([1.996, 3.108, -4.554]).normalized()


print_quiz('Coding Dot Product & Angle')

print_question('Dot Product 1')
print Vector([7.887, 4.138]).dot(Vector([-8.802, 6.776]))

print_question('Dot Product 2')
print Vector([-5.955, -4.904, -1.874]).dot(Vector([-4.496, -8.755, 7.103]))

print_question('Angle in Radians')
print Vector([3.183, -7.627]).angle_with(Vector([-2.668, 5.319]))

print_question('Angle in Degrees')
print Vector([7.35, 0.221, 5.188]).angle_with(Vector([2.751, 8.259, 3.985]), True)


print_quiz('Checking Parallel, Orthogonal')

cpo_1_a = Vector([-7.579, -7.88])
cpo_1_b = Vector([22.737, 23.64])

cpo_2_a = Vector([-2.029, 9.97, 4.172])
cpo_2_b = Vector([-9.231, -6.639, -7.245])

cpo_3_a = Vector([-2.328, -7.284, -1.214])
cpo_3_b = Vector([-1.821, 1.072, -2.94])

cpo_4_a = Vector([2.118, 4.827])
cpo_4_b = Vector([0, 0])

print_question('1 is Parallel')
print cpo_1_a.is_parallel_to(cpo_1_b)

print_question('1 is Orthogonal')
print cpo_1_a.is_orthogonal_to(cpo_1_b)

print_question('2 is Parallel')
print cpo_2_a.is_parallel_to(cpo_2_b)

print_question('2 is Orthogonal')
print cpo_2_a.is_orthogonal_to(cpo_2_b)

print_question('3 is Parallel')
print cpo_3_a.is_parallel_to(cpo_3_b)

print_question('3 is Orthogonal')
print cpo_3_a.is_orthogonal_to(cpo_3_b)

print_question('4 is Parallel')
print cpo_4_a.is_parallel_to(cpo_4_b)

print_question('4 is Orthogonal')
print cpo_4_a.is_orthogonal_to(cpo_4_b)


print_quiz('Coding Vector Projections')

cvp_1_v = Vector([3.039, 1.879])
cvp_1_b = Vector([0.825, 2.036])

cvp_2_v = Vector([-9.88, -3.264, -8.159])
cvp_2_b = Vector([-2.155, -9.353, -9.473])

cvp_3_v = Vector([3.009, -6.172, 3.692, -2.51])
cvp_3_b = Vector([6.404, -9.144, 2.759, 8.718])

print_question('Projection of 1 onto a Base')
print cvp_1_v.projection_onto(cvp_1_b)

print_question('Component of 2 Orthogonal to a Base')
print cvp_2_v.component_orthogonal_to(cvp_2_b)

print_question('Projection of 3 onto a Base')
print cvp_3_v.projection_onto(cvp_3_b)

print_question('Component of 3 Orthogonal to a Base')
print cvp_3_v.component_orthogonal_to(cvp_3_b)


print_info('END')
