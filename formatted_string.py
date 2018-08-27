import argparse
import json


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-st', '--string', help='Input a string')
    return parser.parse_args()


def get_raw_string(raw_string):
    try:
        formatted_string = json.dumps(raw_string)
        return formatted_string
    except (TypeError, ValueError):
        return None

def get_converted_dict(formatted_string):
    converted_dict = json.loads(formatted_string)
    return converted_dict

def print_dict(converted_dict):
    print('{}'.format(converted_dict))


if __name__ == '__main__':
    args = get_parser()

    entered_string = get_raw_string(args.string)

    new_dict = get_converted_dict(entered_string)

    print_dict(new_dict)
