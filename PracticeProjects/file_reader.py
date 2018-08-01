"""with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print (contents)
"""
def filereader(filename):
    with open(filename) as file_object:
        contents = file_object.read()
        print contents
        for i in contents:
            print i
        for i in file_object:
            print i

filereader('pi_digits.txt')