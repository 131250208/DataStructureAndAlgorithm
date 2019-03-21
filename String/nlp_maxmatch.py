'''
自然语言处理的分词baseline算法——最大匹配算法
'''

def max_match(sentence, dictionary):
    if sentence == "":
        return []
    for l in range(len(sentence), 1, -1):
        first_word = sentence[:l]
        rest = sentence[l:]
        if first_word in dictionary:
            word_seq = [first_word, ]
            word_seq.extend(max_match(rest, dictionary))
            return word_seq

    # if no word found
    first_word = sentence[0]
    rest = sentence[1:]
    word_seq = [first_word, ]
    word_seq.extend(max_match(rest, dictionary))
    return word_seq


if __name__ == "__main__":
    sentence = "我特别喜欢北京烤鸭"
    dictionary = {"我", "特别", "喜欢", "北京", "北京烤鸭", "烤鸭"}
    print(max_match(sentence, dictionary))
