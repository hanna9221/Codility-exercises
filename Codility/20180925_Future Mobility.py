# Future Mobility

def solution(A, B):
    l = len(A)
    C = []
    for i in range(l):
        C.append(A[i]-B[i])
    if sum(C)!=0:
        return -1
    if l==2:
        return abs(C[0])    
    
    def moveRight(C):
        count = 0
        f = 0
        for i in range(l-2):
            if C[i]+f>0:
                temp = C[i]+f #number of stones to change
                count += temp
                f = 0
                if C[i+1]<0:
                    if abs(C[i+1])<=temp: # e.g. [5,-2,-3]
                        C[i] -= temp
                        C[i+2] += (temp+C[i+1])
                        C[i+1] = 0
                    else: # e.g. [1,-2,1]
                        C[i+1] += temp
                        C[i] -= temp
                else: # e.g. [3,0,-1,-2]
                    C[i+2] += temp
                    C[i] -= temp
            else:
                f += C[i]
        if C[l-2]>0 and C[l-1]<0:
            count += -C[l-1]
            C[l-2] += C[l-1]
            C[l-1] = 0
        return C, count
    
    D, r1 = moveRight(C)
    E, r2 = moveRight(D[::-1])
    return (r1+r2)%1000000007
