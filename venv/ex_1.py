def write_in_file():
    out_f = open('my_file.txt', 'w')

    how_much_str_write = input('How many str do you want to write into file?')

    try:
        how_much_str_write = int(how_much_str_write)

        for i in range(0,how_much_str_write):
            info_to_write = input('Input what you want to write in file?')
            out_f.write(info_to_write+'\n')
    except ValueError:
        print('Try again. Strings amount must be a number.')

    out_f.close()

if __name__ == '__main__':
    write_in_file()
