def improve_grammar(text):
    if text == "":
        return False
    elif text == None:
        raise Exception("No text given")
    elif text[-1] in '!?.':
        return text.istitle()
    else:
        return False
    