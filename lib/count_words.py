def count_words(str):
    result = str.split(' ')
    if len(str) < 1:
        return 0
    else:
        return len(result)