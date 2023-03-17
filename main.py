# python3
def isFull(theards, n):
    for i in range(0,n):
        if theards[i][0] is None:
            return False
    return True

def isEmpty(theards,n):
    for i in range(0,n):
        if theards[i][0] is not None:
            return False
    return True

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    time=0
    threads = []
    for i in range(0,n):
        threads.append([None,i,time])
    for i in range(0,m):
        for j in range(0,n):
            if threads[j][0] is None:
                threads[j][0] = data[i]
                threads[j][2] = time
                break
        if isFull(threads,n) is False:
            continue
        dt = min(threads)[0]
        for j in range(0,n):
            threads[j][0]-=dt
        for thr in threads:
            if thr[0] <= 0:
                output.append([threads[threads.index(thr)][1],threads[threads.index(thr)][2]])
                threads[threads.index(thr)][0]=None
        time+=dt
    if isEmpty(threads,n) is False:
        for thr in threads:
            if thr[0] is not None:
                output.append([threads[threads.index(thr)][1],threads[threads.index(thr)][2]])

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    line = list(map(int, input().split()))
    n = line[0]
    m = line[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for reslt in result:
        print(reslt[0], reslt[1])


if __name__ == "__main__":
    main()
