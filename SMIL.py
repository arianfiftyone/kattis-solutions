def smil():

    line = input()
    smilies = set((':)', ';)', ':-)', ';-)'))


    for index in range(len(line)):
        # out of bounds check if three chars at end
        if index+2 < len(line):
            if line[index:index+3] in smilies:
                print(index)
        # if two chars at end
        if index+1 < len(line):
            if line[index:index+2] in smilies:
                print(index)


if __name__ == '__main__':
    smil()