
def DP_cutRod(p,n):
    maxSell = []
    maxSell.append(0)
    for j in range(1,n+1):
        maxVal = 0
        for k in range(1,j+1):
            maxVal = max(maxVal, p[k] + maxSell[j-k])
        maxSell.append(maxVal)
    
    return maxSell[n]

p = [0,1,5,8,9,10] # p[n] = 길이 n의 막대를 판매할 때 얻는 가격
value = DP_cutRod(p,4)
print(value)