from exercise_utilities import *
from line import *


print_info('BEGIN')


print_quiz('Coding Functions for Lines')

print_question('Intersection 1')
print Line(Vector(['4.046', '2.836']), '1.21').intersection_with(Line(Vector(['10.115', '7.09']), '3.025'))

print_question('Intersection 2')
print Line(Vector(['7.204', '3.182']), '8.68').intersection_with(Line(Vector(['8.172', '4.114']), '9.883'))

print_question('Intersection 3')
print Line(Vector(['1.182', '5.562']), '6.744').intersection_with(Line(Vector(['1.773', '8.343']), '9.525'))


print_info('END')
