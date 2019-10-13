# https://app.codility.com/cert/view/certX2W53D-TN93DYSUTVXVDABT/

def solution(A):
    N, M = len(A), len(A[0])
    path = set([(0,0)])
    res = str(A[0][0])
    for i in range(2, N+M):
        new_path = []
        max_n = 0
        for p1, p2 in path:
            if p1<N-1 and p2<M-1:
                a, b = A[p1][p2+1], A[p1+1][p2]
                if a>b:
                    if a>max_n:
                        max_n = a
                        new_path = [(p1, p2+1)]
                    elif a==max_n:
                        new_path.append((p1, p2+1))
                elif a<b:
                    if b>max_n:
                        max_n = b
                        new_path = [(p1+1, p2)]
                    elif b==max_n:
                        new_path.append((p1+1, p2))
                else:
                    if a>max_n:
                        max_n = a
                        new_path = [(p1, p2+1), (p1+1, p2)]
                    elif a==max_n:
                        new_path.append((p1, p2+1))
                        new_path.append((p1+1, p2))
            elif p1<N-1 and p2==M-1:
                b = A[p1+1][p2]
                if b>max_n:
                    max_n = b
                    new_path = [(p1+1, p2)]
                elif b==max_n:
                    new_path.append((p1+1, p2))
            elif p1==N-1 and p2<M-1:
                a = A[p1][p2+1]
                if a>max_n:
                    max_n = a
                    new_path = [(p1, p2+1)]
                elif a==max_n:
                    new_path.append((p1, p2+1))
        path = set(new_path)
        res += str(max_n)
    return res
                        
#A = [[9, 9, 7], [9, 7, 2], [6, 9, 5], [9, 1, 2]]
A = [[3]*4 for i in range(5)]
A[2][3] = 1
print(solution(A))


# silver solution
# https://app.codility.com/cert/view/cert43DAYQ-QNFJ6EK6NYNX8XDB/
def compare(p, q):
    for i in range(len(p)):
        if int(p[i]) > int(q[i]):
            return True
        elif int(p[i]) < int(q[i]):
            return False
    return True

def solution(A):
    N, M = len(A), len(A[0])
    dp = [[0]*M for i in range(N)]
    dp[0][0] = str(A[0][0])
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + str(A[i][0])
    for i in range(1, M):
        dp[0][i] = dp[0][i-1] + str(A[0][i])
    
    for i in range(1, N):
        for j in range(1, M):
            p, q = dp[i-1][j], dp[i][j-1]
            if compare(p, q):
                dp[i][j] = p + str(A[i][j])
            else:
                dp[i][j] = q + str(A[i][j])
    return dp[N-1][M-1]                 

