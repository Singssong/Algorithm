"""
DP - 기업투자 문제
"""


def DP_maxProfit(M,N,profit): # 투자액 M, 기업의 수 N
    max_profit = [[0] * 5 for i in range(5)]
    for i in range(1,N+1): # 기업의 수
        for j in range(1,M+1): # 투자액 1만원..2만원..
            maxValue = 0
            for k in range(j+1):
                maxValue = max(maxValue, max_profit[i-1][j-k] + profit[i-1][k])
            max_profit[i][j] = maxValue
        
    return max_profit[N][M]

profit = [
    [0,2,4,6,9], # 기업 0
    [0,3,5,6,8], # 기업 1
    [0,1,3,7,9]  # 기업 2
]

value = DP_maxProfit(1,1,profit)
print(value)

