def do_twice(f, arg):
    f(arg)
    f(arg)

def print_string(s):
    print(s)

do_twice(print_string, 'spam1')

def print_twice(s):
    print(s)
    print(s)

def do_four(f, arg):
    print_twice(arg)
    print_twice(arg)

do_four(print_twice, 'spam2')
