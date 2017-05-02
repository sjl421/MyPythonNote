def countChars(filename):
    count = {}

    with open(filename) as info:  # inputFile Replaced with filename
        readFile = info.read()
        for character in readFile.upper():
            count[character] = count.get(character, 0) + 1

    return count


if __name__ == '__main__'
    inputFile = input("File Name : ")
    print(countChars(inputFile))
