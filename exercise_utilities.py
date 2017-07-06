def print_lesson_begin(name):
    print_info('BEGIN LESSON ' + name)


def print_lesson_end(name):
    print_info('END LESSON ' + name)


def print_info(caption):
    print
    print
    print caption
    print


def print_quiz(name):
    print
    print '*****'
    print 'Quiz: ' + name


def print_question(name):
    print
    print name + ':'
