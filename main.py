import os

def import_file(filename):
    file = open(filename, "r")
    return file.read()

def unique(f):
    for eachline in f:
        if (eachline[0] == "H" or eachline[0] == "V"):
            temp = eachline.split(" ")
            print(temp)

def main():
    inp = import_file("a_example.txt")
    unique(inp)

if __name__ == "__main__":
    main()
