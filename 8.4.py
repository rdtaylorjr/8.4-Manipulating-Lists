fname = input("Enter file name: ")
fhand = open(fname)
flist = list()
for line in fhand:
    fline = line.split()
    for fword in fline:
        if fword not in flist:
            flist.append(fword)
flist.sort()
print(flist)
