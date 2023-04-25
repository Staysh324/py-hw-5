def rle(string):
    sumstr = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i+1]:
            count = count + 1
            i += 1
        if count == 1:
            sumstr += string[i]
        else:
            sumstr += string[i] + str(count)
        i += 1
    return sumstr

asd = str(input("введите строку: "))
print(rle(asd))

