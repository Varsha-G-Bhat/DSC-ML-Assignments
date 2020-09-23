def CountPairs(box, x):
    """ Function to count the number of pairs
    box - input list
    x - number of Gloves in the given List"""
    
    j = 0
    count = 0
    box = sorted(box, reverse=False)
    while  j < x-1 :
        i = j
        j = i + 1
        if box[i] == box[j]:
            j = j + 1
            count = count + 1
    return count



if __name__ == "__main__":
    N = int(input())
    List = input().split()
    print(CountPairs(List,N))