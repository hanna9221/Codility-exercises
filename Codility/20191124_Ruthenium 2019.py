# Ruthenium 2019
# https://app.codility.com/cert/view/certMUEPHH-XSGNTJQNKXJCJEH4/

from collections import defaultdict as dfd
def solution(A, K):
    if len(A) <= K:
        return len(A)
    res = 0
    tail = 0
    book = dfd(int)
    M = 0
    for i in range(len(A)):
        book[A[i]] += 1
        M = max(M, book[A[i]])
        if M+K <= res:
            book[A[tail]] -= 1
            tail += 1
        else:
            res += 1
    return res

A = [1,1,4,2,7,3,3]
K = 2
print(solution(A, K))
