def mysplit(strng):
    s = str()
    li = []
    for i in strng:
        if strng.isspace() == True:
            return li
        else:
            if i != " ":
                s += i
            else:
                li.append(s)
                s = str()
    return li



