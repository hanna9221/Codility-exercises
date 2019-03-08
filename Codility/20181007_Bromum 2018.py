# Bromum 2018
# https://app.codility.com/cert/view/cert7N4E6K-A8V9RCXQ4UK6D7WS/

def solution(N,Q,B,C):
    rec = {}
    for i in range(len(B)):
        if (B[i], C[i]) in rec:
            rec[(B[i], C[i])] += 1
        else:
            rec[(B[i], C[i])] = 1
        if rec[(B[i], C[i])]==Q:
            return i
    return -1


B = [1, 2, 0, 1, 1, 0, 0, 1]
C = [0, 3, 0, 2, 0, 3, 0, 0]
N, Q = 3, 2
print(solution(N,Q,B,C))
