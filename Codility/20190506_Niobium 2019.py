# Niobium 2019
# https://app.codility.com/cert/view/certEYYJGV-KCPFURCV54GFASJK/

def solution(A):
    N = len(A)
    
    def transform(arr):
        s1 = ''.join(str(a) for a in arr)
        s2 = ''.join(str(a^1) for a in arr)
        return max(s1, s2)
        
    record = {}
    for i in range(N):
        temp = transform(A[i])
        if temp in record:
            record[temp] += 1
        else:
            record[temp] = 1
    
    res = 0
    for key in record:
        res = max(res, record[key])
    
    return res

A = [[0, 1, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0]]
#A = [[0,0,0,0],
#     [0,1,0,0],
#     [1,0,1,1]]
print(solution(A))
