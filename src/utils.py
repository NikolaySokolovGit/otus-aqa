def validate_size(*args):
    for arg in args:
        if not isinstance(arg, (float, int)):
            raise ValueError('size argument must be float or int')
        if arg <= 0:
            raise ValueError('size argument must be > 0')
