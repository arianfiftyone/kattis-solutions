import math
def eos():

    inpString = input()

    if inpString[(len(inpString) // 2)] == ')' and int(len(inpString)) % 2 == 0:
        return print('correct')
        
    print('fix')

if __name__ == '__main__':
    eos()