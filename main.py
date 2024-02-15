import os.path
import read_ext_file as rf


if __name__ == '__main__':
    input_string = input('> ')
    elements = input_string.split()
    donor = os.path.splitext(elements[0])
    sign = elements[1]
    recipient = os.path.splitext(elements[2])
