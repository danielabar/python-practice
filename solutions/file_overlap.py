import sys


def convert_to_numbers(file):
    with open(file, 'r') as file_data:
        file_lines = file_data.readlines()
        return {int(file_line.strip('\n')) for file_line in file_lines}


def find_overlap(file1, file2):
    file1_numbers = convert_to_numbers(file1)
    file2_numbers = convert_to_numbers(file2)
    return file1_numbers.intersection(file2_numbers)


if __name__ == '__main__':
    result = find_overlap(sys.argv[1], sys.argv[2])
    print(result)
