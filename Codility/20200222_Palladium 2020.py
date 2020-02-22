# Palladium 2020
# https://app.codility.com/cert/view/certGVGU2V-84XG39GD5KUPVRCJ/

def solution(H):
    N = len(H)
    leftstart, rightstart = [0]*N, [0]*N
    leftstart[0] = H[0]
    rightstart[-1] = H[-1]
    for i in range(1, N):
        if H[i] > leftstart[i-1]:
            leftstart[i] = H[i]
        else:
            leftstart[i] = leftstart[i-1]
        if H[N-i-1] > rightstart[N-i]:
            rightstart[N-i-1] = H[N-i-1]
        else:
            rightstart[-i-1] = rightstart[-i]

    res = rightstart[0]*N
    for i in range(1, N):
        res = min(res, leftstart[i-1]*i + rightstart[i]*(N-i))
    return res
