"""
등수매기기 알고리즘(Ranking Alogorithm)
시험 점수들을 값이 큰 순서대로 등수를 매기려고 한다.
예를 들면, 5명의 시험 점수가 82, 75, 98, 63, 40이라면 
각 점수의 등수는 2등, 3등, 1등, 4등, 5등이 된다. 
시험 점수들의 갯수는 N(> 0)이다.
시험 점수들은 크기가 N인 Score라는 배열에 저장되어 있다.
각 점수의 등수는 크기가 N인 Rank라는 배열에 저장해야 한다. 
등수를 매기는 알고리즘을 작성하라
"""

#input

Score = [82, 75, 98, 63, 40]
Rank = [1 for i in range(len(Score))] # Rank 배열을 1로 초기화

#process

for i in range(len(Score)):
    for j in range(len(Score)):
        if Score[i] < Score[j]: # 자신의 점수와 비교할 대상을 전체 비교하여 자신의 점수보다 높은 점수가 있을 때 마다
            Rank[i] = Rank[i] + 1 # 자신의 Rank배열에 해당하는 등수를 하나씩 증가

#output
print(Rank)