file = open("code.txt","r")
string = file.read()
list = string.split()
count = dict()
for words in list:
    if words in count:
        count[words] += 1
    else:
        count[words] = 1
for i in count:
    print(i,' ',count[i],'times')
