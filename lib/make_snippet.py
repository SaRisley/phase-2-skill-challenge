def make_snippet(str):
    result = str.split(' ')
    if len(result) > 5:
        first_5 = result[:5]
        return f"{' '.join(first_5)} ..."
    else:
        return str