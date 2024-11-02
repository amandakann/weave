def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        index = 0
        words = []
        while True:
            lines = []
            # read a block of 5 lines at a time
            for _ in range(5):
                lines.append(f.readline().strip().split(" "))
            if not lines[0][0]:
                break
            
            # control for oob index
            if index == -1:
                index = 0
            if index > len(lines[0]) - 1:
                index = -1
            
            # add one word per sentence to list
            words.append(lines[0][index])

            # update index for next sentence
            index = int(lines[2][index])
        print(" ".join(words))

if __name__ == "__main__":
    main("./en-es-short.txt")