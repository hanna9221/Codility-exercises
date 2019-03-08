# Bromum 2018

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
