import math
def split_in_files(word):
    f = open(text, "r")
    if f.mode == 'r':
        contents = f.read()


    # split the string by spaces in a
    count = 0

    # search for pattern in a
    #for i in range(0, len(a)):
        # if match found increase count
    #    if (word == a[i]):
    #       count = count + 1

    for i in range(len(contents)):
        if contents[i] == "$":
            if contents[i+1] == "$":
                if contents[i+2] == "$":
                    if contents[i+3] == "$":
                        count = count + 1

    number_files = math.ceil(count/12688)
    i=0
    while i < number_files:
        f = open("drug{}.txt".format(i+1),"w+")
        i = i + 1
    i=1
    count = 0
    s=0
    while i <= number_files:
        text_to_append= ""
        f = open("drug{}.txt".format(i), "a+")
        while s < len(contents):
            if count < 12688:
                text_to_append += contents[s]
                if contents[s] == "$":
                    if contents[s+1] == "$":
                        if contents[s+2] == "$":
                            if contents[s+3] == "$":
                                count = count + 1
            else:
                break
            s += 1
        count = 0
        if i != number_files:
            text_to_append += "$$$"
        f.write(text_to_append)
        i = i + 1





# Driver code
text = input("Write the File: ")  # Python 3
print(split_in_files("0"))
