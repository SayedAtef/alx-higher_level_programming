#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0
    for x in range(len(sys.argv) - 1):
        sums += int(sys.argv[x + 1])
    print("{}".format(sums))	
