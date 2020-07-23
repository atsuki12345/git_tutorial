def haveAllCharacters(string,word):
    #ここから書きましょう
    list = word_list(word)
    for i in list:
        if i in string:
            continue
        else:
            return False
    else:
        return True

def word_list(word):
    word_list = []
    for i in word:
        if i == ' ':
            continue
        else:
            word_list.append(i)
    return word_list