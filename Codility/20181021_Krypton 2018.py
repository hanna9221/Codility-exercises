# Krypton 2018

def helper(n):
    output = [0]*3
    if n==0:
        return [0,0,1]
    else:
        while not n&1:
            output[0] += 1
            n = n>>1
        while n%5==0:
            output[1] += 1
            n //= 5
        return output

def compare(this, up, left):
    if this[2]>0 or (up[2]>0 and left[2]>0):
        return [0,0,1]
    elif up[2]>0:
        return [this[0]+left[0], this[1]+left[1], 0]
    elif left[2]>0:
        return [this[0]+up[0], this[1]+up[1], 0]
    else:
        return [min(this[0]+up[0], this[0]+left[0]), 
                min(this[1]+up[1], this[1]+left[1]), 0]

def solution(A):
    N = len(A)
    dp = [[0]*N for i in range(N)]
    if A[0][0]==0:
        return 1
    dp[0][0] = helper(A[0][0])
    zero_exists = False
    for i in range(1, N): # the first column
        if A[i][0]==0:
            zero_exists = True
        dp[i][0] = compare(helper(A[i][0]), dp[i-1][0], [0,0,1])
    for j in range(1, N): # thie first row
        if A[0][j]==0:
            zero_exists = True
        dp[0][j] = compare(helper(A[0][j]), [0,0,1], dp[0][j-1])
    for i in range(1, N):
        for j in range(1, N):
            if A[i][j]==0:
                zero_exists = True
            dp[i][j] = compare(helper(A[i][j]), dp[i-1][j], dp[i][j-1])
    if zero_exists:
        return min(1, dp[N-1][N-1][0], dp[N-1][N-1][1])
    else:
        return min(dp[N-1][N-1][0], dp[N-1][N-1][1])
