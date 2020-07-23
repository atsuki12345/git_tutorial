def determineMedian(income):
    #ここから書きましょう
    sorted_list = sorted(income)
    length = len(income)
    if length % 2 == 0:
        return float((sorted_list[int(length/2-1)]+sorted_list[int(length/2)]) /2)
    else:
        return float(sorted_list[int(length/2)])