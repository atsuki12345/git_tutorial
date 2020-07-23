def lengthOfLongestPalindrome(string):
    # ここから書きましょう
    word_list = []
    for i in sorted(string):
        if i == '.' or i == ',' or i == ' ':
            continue
        else:
            word_list.append(i)
    return counter(word_list)

count = 0
pass_list = []

def counter(word_list):
    global count
    if len(word_list) > 1:
        if word_list[0] == word_list[1]:
            count += 2
            counter(word_list[int(2):])
        else:
            pass_list.append(word_list[0])
            counter(word_list[int(1):])
    elif len(word_list) == 1:
        pass_list.append(word_list[0])
        counter(word_list[int(1):])
    else:
        if len(pass_list) > 0:
            count += 1
    return count