def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    if len(line1) < len(line2):
        counter = len(line1)
        larger = line2
    else:
        counter = len(line2)
        larger = line1
    print(counter)
    for i in range(0,counter):
        print(line1[i],line2[i])
        print("larger--------->",larger.index(larger[i]),larger.index(larger[i+1]))
        if line1[i] == line2[i]:
            print("match")
            print("index ",line1.index(line1[i]),line2.index(line2[i]))
            try
        else:
            print(i)
            print("index ",line1.index(line1[i]),line2.index(line2[i]))
            return i
        pass
    return -1


line1="abc"
line2="abcd"
print(singleline_diff(line1,line2))
