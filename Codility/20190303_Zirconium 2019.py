# Zirconium 2019
# https://app.codility.com/cert/view/certVB92F3-AE2WMHWWZYRRSSCU/

def solution(A, B, F):
    N = len(A)
    V = []
    for i in range(N):
        V.append([A[i], B[i], A[i]-B[i]])
    V.sort(key=lambda x:x[2], reverse=True)
    res = 0
    for i in range(F):
        res += V[i][0]
    for i in range(F, N):
        res += V[i][1]
    return res

