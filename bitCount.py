#Write an efficient program to count number of 1s in the binary representation of an integer.

def countBits(num):
    #right shift number and keep increasing count by 1 until number itself is 0
    count = 0
    while(num):
        count += num & 1
        #print(count)
        num >>= 1
        #print(num)

    return count

def kernighanAlgo(n):
    # bitwise and with number and number -1 . With number -1, right most set bit(1)
    # and subsequent bits get flipped. Then number & (number - 1) reduces num of
    # 1 from original number by 1. This method brings out number of loop.
    count = 0
    while(n):
        n &= (n-1)
        count += 1
    return count
        

def main():
    i = 9
    print(countBits(i))
    print(kernighanAlgo(i))


if __name__ == "__main__":
    main()
