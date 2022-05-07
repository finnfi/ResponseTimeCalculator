#!/usr/bin/python3
from math import ceil

def calculateResponseTime(ID, C, T, Pr):
    # Sort arrays
    Pr, ID, C, T = map(list, zip(*sorted(zip(Pr, ID, C, T), reverse=True)))
    
    # dict of response time : from task to R 
    R = dict()
    
    n_tasks = len(ID)
    for i in range(n_tasks):
        w = C[i]
        while True:
            w_next = C[i]
            for j in range(i):
                w_next += ceil(w/T[j])*C[j]
            if w_next == w:
                R[ID[i]] = w
                break
            elif w_next > T[i]:
                R[ID[i]] = None
                break
            w = w_next
    return R
    
def main():
    # Fill in these arrays:
    ID = ['a', 'b', 'c'] # ID of task
    C = [40, 10, 5] # Computation time
    T = [80, 40, 20] # Period time
    Pr = [1, 2, 3] # Priority 

    R = calculateResponseTime(ID, C, T, Pr)

    print("Response times calculated are: ")
    for id, r in R.items():
        print(id, ": ", r)

    
if __name__ == "__main__":
    main()