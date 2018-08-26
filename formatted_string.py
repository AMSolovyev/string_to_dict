import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-st', '--string', help='Input a string')
    return parser.parse_args()


def get_raw_string(raw_string):
    formatted_string = {}
    try:
        formatted_string = eval(raw_string)
        return formatted_string
    except (TypeError, ValueError):
        return None


def print_string(formatted_string):
    print('{}'.format(formatted_string))


if __name__ == '__main__':
    args = get_parser()

    entered_string = get_raw_string(args.string)
    print_string(entered_string)
