answer_list = []
def reverseInteger(intArr,i):
    #ここから書きましょう
    for num in intArr[:i]:
        answer_list.append(num)
    else:
        for rev_num in reversed(intArr[i:]):
            answer_list.append(rev_num)
    return answer_list