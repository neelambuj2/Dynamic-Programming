def findQualifiedNumbers(numberArray):
    numberArray.sort()
    res = " "
    for num in numberArray:
        num = str(num)
        if '1' in num and '2' in num and '3' in num:
            res = res + ','
    if bool(res) is False:
        return "-1"
    else:
        return res


findQualifiedNumbers([123, 456])