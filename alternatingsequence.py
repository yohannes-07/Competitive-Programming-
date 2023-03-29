for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    # add the negation of the last element to handle if the last element is valid in the sequence
    arr.append(arr[-1]*-1)
    summ=0
    lastAlternatingSequenceIdx = 0

    for i in range(1,n+1):
        if((arr[i]>0 and arr[i-1]<0) or (arr[i]<0 and arr[i-1]>0)):
            
            #chooose the max element so far from the last alternating seqence element till now excluding the current one
            summ+=max(arr[lastAlternatingSequenceIdx:i])

            #update it
            lastAlternatingSequenceIdx = i

        
    print(summ)
