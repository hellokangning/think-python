def do_n(f, n):
    for i in range(n):
        f()

def print_foo():
    print('foo')

do_n(print_foo, 5)