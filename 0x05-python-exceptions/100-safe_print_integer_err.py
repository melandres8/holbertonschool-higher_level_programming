from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return False
    else:
        return True
