def halloween():
    differentDates = input().split()
    holidayMonth = differentDates[0]
    holidayDay = int(differentDates[1])

    isItHalloween = holidayMonth == 'OCT' and holidayDay == 31
    isItXmas = holidayMonth == 'DEC' and holidayDay == 25

    if isItHalloween or isItXmas:
        print('yup')
    else:
        print('nope')

if __name__ == '__main__':
    halloween()
    