from vector import Vector


def print_quiz(name):
    print
    print '*****'
    print 'Quiz: ' + name


def print_question(name):
    print
    print name + ':'


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
