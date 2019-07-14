# Molybdenum 2019
# https://app.codility.com/cert/view/certUUMHYW-HPDCWJ7WVGD2BXQC/

def solution(K, M, A):
    N = len(A)
    for k in range(K):
        A[k] += 1
            
    rec = [0]*(M+2)
    for a in A:
        rec[a] += 1
    
    res = set()
    for i in range(1, M+2):
        if rec[i] > N//2:
            res.add(i)
    
    for j in range(1, N-K+1):
        L, R = A[j-1], A[j+K-1]
        rec[L] -= 1
        rec[L-1] += 1
        rec[R] -= 1
        rec[R+1] += 1
        if rec[L-1] > N//2:
            res.add(L-1)
        if rec[R+1] > N//2:
            res.add(R+1)
        A[j-1] -= 1
        A[j+K-1] += 1
    
    res = list(res)
    res.sort()
    return  res

#K, M = 3, 5
#A = [2,1,3,1,2,2,3]
K, M = 4, 2
A = [1,2,2,1,2]
print(solution(K, M, A))
