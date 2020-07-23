sum_price_list = []
def howManyPairsOf3Sum0(intArr):
    #ここから書きましょう
    sum_price = 0
    for i in range(int(len(intArr))):
        for j in range(1,int(len(intArr))):
            for k in range(2,int(len(intArr))):
                cost_combination = []
                if i != j and i != j and j != k and i < j and i < k and j < k:
                    cost_combination.append(intArr[i])
                    cost_combination.append(intArr[j])
                    cost_combination.append(intArr[k])
                    sum_price_list.append(sorted(cost_combination))
    else:
        return removed_list(sorted(sum_price_list))



removed_lists = []

def removed_list(sum_price_list):
    for each_list in sum_price_list:
        if each_list not in removed_lists:
            removed_lists.append(each_list)
    else:
        return each_how_much(removed_lists)

def each_how_much(removed_list):
    counter = 0
    for each in removed_lists:
        sum_price = 0
        for price in sorted(each):
            sum_price += price
        else:
            if sum_price == 0:
                counter += 1
    else:
        return counter


print(howManyPairsOf3Sum0([-16,-7,-9,15,-19,4,17,18,-11,5,18,6]))