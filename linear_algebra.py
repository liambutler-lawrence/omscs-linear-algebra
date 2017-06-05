from vector import Vector

def print_quiz(name):
    print
    print '*****'
    print name
    print


print_quiz('Quiz: Plus, Minus, Scalar Multiply')

print 'Q1'
print Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111]))

print 'Q2'
print Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878]))

print 'Q3'
print Vector([1.671, -1.012, -0.318]).times_scalar(7.41)
