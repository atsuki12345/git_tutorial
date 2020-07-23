'''
Q3 Amazon
今あなたは階段を登ろうとしています。この階段では一度に1段、もしくは2段しか登ることができません。頂上までの段数stepsが与えられるので、頂上までの登り方が何通りあるかを返す、numberOfWaysという関数を作成してください。
input
1
output
1
input
2
output
2
input
4
output
5
'''

def numberOfWays(n):
    counter = 0
    for i in range(0,n):
        steps = 0
        for j in range(0,2):
            steps += j
            if steps == n:
                counter += 1
    return counter

print(numberOfWays(2))