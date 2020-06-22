'''
Q1.Facebook
整数で構成される降順ソート済みの配列intArrが与えられるので、各要素を2乗し降順に並べ変えた配列を返す、sortedSquaredという関数を作成してください。
input
[-6, -3, -1, 2, 4, 5]
output
[1, 4, 9, 16, 25, 36]
input
[-5, -4, -2, 0, 1]
output
[0, 1, 4, 16, 25]
Hint:
時間計算量：O(n)
'''

def sortedSquared(num_list):
    squated_list = []
    for i in num_list:
        squated_list.append(i**2)
    return bubble_sort(squated_list)

def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr
print(sortedSquared([-5, -4, -2, 0, 1]))