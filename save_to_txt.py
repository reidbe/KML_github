import time


def create_file(filename):
    save_measure_file = open(filename + '.txt', 'w')
    save_measure_file.close()


def save_to_txt(string, filename):
    save_measure_file = open(filename + '.txt', 'a')
    save_measure_file.write(string)
    save_measure_file.close()