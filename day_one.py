+2
print(2+++2)


def right_justify(s):
    return((70-len(s)) * ' ') + s


print(right_justify('lorem ipsum'))


# How many Seconds in 21:35 ?
def convert_seconds(t):
    minutes = int(t[:2])
    seconds = int(t[3:])
    # print(minutes, type(minutes), seconds, type(seconds))
    return (minutes*60) + seconds


print(convert_seconds('21:15'))


def km_to_mi(km):
    conversion = 0.621371
    return km * conversion


print(km_to_mi(5))


def find_rate(distance, time):
    seconds = convert_seconds(time)
    miles = km_to_mi(distance)
    rate = miles/seconds
    print(1/((rate)*60))
    # add numbers to left of decimale to minutes, multiply decimal by 100 and capture modulo


print(find_rate(5, '21:35'))


def check_fermat(a, b, c, n):
    if(n < 2):
        return 'n must be greater than 2'
    elif(a**n + b**n == c**n):
        return 'Fermat was wrong.'
    else:
        return "No, that doesn't work"


print(check_fermat(4, 4, 4, 4))
