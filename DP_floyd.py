global INF 
INF = 9999

def floyd(W):
    D = W
    for k in range(1,5):
        for i in range(1,5):
            for j in range(1,5):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D




W = [[INF,INF,INF,INF,INF],
[INF,INF,INF,2,INF],
[INF,1,INF,INF,INF],
[INF,INF,8,INF,3],
[INF,6,4,INF,INF]]

result = floyd(W)
print(result)