
cache_list = []


def longestPalindromicSubstring(string):
    for i in range(int(len(string))):
        for j in range(1, int(len(string) + 1)):
            if not string[i:j] == '':
                cache_list.append(string[i:j])

    return palindromic(cache_list)


palindromic_list = []


def palindromic(cache_list):
    for each_string in cache_list:
        count = 0
        palindromic_string = ''
        for num in range(int(len(each_string))):
            if each_string[int(num)] == each_string[-(num + 1)]:
                palindromic_string += each_string[int(num)]
                count += 1
                if count == len(each_string):
                    palindromic_list.append(palindromic_string)
            else:
                break
    else:
        return longest_string(palindromic_list)

def longest_string(palindromic_list):
    answer_string = ''
    for string in palindromic_list:
        if len(answer_string) < len(string):
            answer_string = string
        else:
            continue
    else:
        return answer_string

print(longestPalindromicSubstring('google'))