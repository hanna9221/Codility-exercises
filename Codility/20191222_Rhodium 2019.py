# Rhodium 2019
# https://app.codility.com/cert/view/certPMWCPY-ZZKESBYE8MCNB8JD/

def solution(T):
    N = len(T)
    res = 0
    
    for i in range(N-1):
        bad = {}
        bad_count = 1
        if T[i] != i: # not a valid edge
            bad[T[i]] = 1
        
        for j in range(i+1, N):
            if j in bad:
                bad_count -= bad.pop(j)
                
            if not i <= T[j] <= j: # not a valid edge
                if T[j] in bad:
                    bad[T[j]] += 1
                else:
                    bad[T[j]] = 1
                bad_count += 1
            elif j == T[j]: # not an edge
                bad_count += 1
                
            if bad_count <= 1:
                res += 1
    return res+N

#T = [2,0,2,2,1,0] #12
#T = [2,4,3,3,0,0] #9
#T = [2,0,4,0,4] #9
T = [2,2,2] #5
print(solution(T))
