'''
Q2. Google
今あなたは不動産を購入しようとしています。配列housesに含まれるそれぞれの要素は1軒あたりの価格を示しています。配列houses、予算budgetが与えられるので、
あなたが買える最大軒数を返す、maximumNumberOfHousesという関数を定義してください。ただしそれぞれの家の価格は1000以下とします。
必要知識
配列
input
[1,2,3,4] , 10
output
4
input
[6,1,2], 5
output
2
input
[30,10,20,30,30] ,100
output
4
input
[30,10,20,30,30] ,5
output
0
'''
def maximumNumberOfHouses(houses,budget):
    count = 0
    sum = 0
    for house in sorted(houses):
        if sum < budget:
            sum += house
            count += 1
        else:
            break
    else:
        return count

print(maximumNumberOfHouses([6,1,2] ,5))