def intToRoman(num: int) -> str:
    print(f'incoming number is {num}')
    if num >= 1000:
        return 'M' + str(intToRoman(num-1000))
    if num >= 900:
        return 'CM' + str(intToRoman(num-900))
    if num >= 500:
        return 'D' + str(intToRoman(num-500))
    if num >= 400:
        return 'CD' + str(intToRoman(num-400))
    if num >= 100:
        return 'C' + str(intToRoman(num-100))
    if num >= 90:
        return 'XC' + str(intToRoman(num-90))
    if num >= 50:
        return 'L' + str(intToRoman(num-50))
    if num >= 40:
        return 'XL' + str(intToRoman(num-40))
    if num >= 10:
        return 'X' + str(intToRoman(num-10))
    if num >= 9:
        return 'IX' + str(intToRoman(num-9))
    if num >= 5:
        return 'V' + str(intToRoman(num-5))
    if num >= 4:
        return 'IV' + str(intToRoman(num-4))
    if num >= 1:
        return 'I' + str(intToRoman(num-1))

    if num == 0:
        return ''
