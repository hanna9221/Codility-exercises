# Yttrium 2019
# https://app.codility.com/cert/view/certZDWWY3-HSHMP7GHKQWC5777/

def checkOutside(A):
    res = 0
    for i in range(26):
        if A[i] != 0:
            res += 1
    return res

def solution(S, K):
    N = len(S)
    if K==0: return N
    A = [0]*26
    for c in S:
        A[ord(c)-97] += 1
    if checkOutside(A) < K:
        return -1
    elif checkOutside(A)==K:
        return 0
    
    res, head, tail = N, -1, 0
    while head < N:
        if checkOutside(A)==K:
            res = min(res, head-tail+1)
            A[ord(S[tail])-97] += 1
            tail += 1
        else: # checkOutside(A) > K
            head += 1
            if head==N: return res
            A[ord(S[head])-97] -= 1
    return res

S = "zaaaa"
K = 2
print(solution(S, K))
