
def spavanac():
    data = input().split()

    hours = int(data[0])
    minutes = int(data[1])

    if minutes - 45 < 0:
        minutes = 60 + (minutes - 45)

        if hours <= 0:

            hours = 24

        hours -= 1
    
    else:
        minutes = minutes - 45
        hours = hours

    print(hours, minutes)



if __name__ == '__main__':
    spavanac()