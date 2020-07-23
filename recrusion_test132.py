optimized_list = []
def optimizedBookShelves(books):
    #ここから書きましょう
    counter = int(books**0.5+1)
    while counter <= books:
        if books % counter == 0:
            optimized_list.append(counter)
            counter += 1
        else:
            counter += 1
    return book_shalves_list(optimized_list,books)

answer_list = []

def book_shalves_list(optimized_list,books):
    for num in optimized_list:
        answer_list.append(num)
        answer_list.append(int(books/num))
    else:
        return answer_list