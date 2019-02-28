def import_file(filename):
    file = open(filename, "r")
    return list(file.read().split("\n"))

def unique(f):
    f.pop()
    final = []
    for eachline in f:
        if eachline[0] == "H" or eachline[0] == "V":
            temp = eachline.split(" ")
            presort = temp[2:]
            postsort = sorted(presort)
            final.append(temp[0:2] + postsort)
    return final

def points(sort, pos):
    print(pos)
    print(sort)
    temp = sort[pos]
    final = temp
    for i in range(len(sort)-1-pos):
        ntemp = sort[i+1+pos]
        count = 0
        picture = ntemp
        counter = 0
        for j in range(len(ntemp)-2):
            if ntemp[2:][j] in temp:
                counter += 1
        if counter <= count:
            count = counter
            final = ntemp

    return final


def sort(l):
    #print position of first
    positions = []
    sortLL = []

    for i in l:
        if i == l[0]:
            sortLL.append(i)
            positions.append(l.index(i))
        else:
            for j in l:
                if j not in sortLL:
                    sortLL.append(j)

            tag = points(sortLL, len(positions))
            sortLL[sortLL.index(tag)] = 0
            sortLL[len(positions)] = tag
            while (0 in sortLL):
                sortLL.remove(0)
            positions.append(l.index(sortLL[len(positions)]))

    #print(points(sortLL,len(positions)))
    # print(sortLL)
    #find position of nextt in input file

def main():
    inp = import_file("b.txt")
    u = (unique(inp))
    sort(u)

if __name__ == "__main__":
    main()
