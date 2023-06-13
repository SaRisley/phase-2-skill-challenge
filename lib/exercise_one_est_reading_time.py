def estimated_reading_time(text):
    if text is None:
        raise Exception("No text given")
    elif text == "":
        return "Pick up a book!"
    else:
        text_in_words = text.split(' ')
        length = len(text_in_words)
        return round(length / 200, 2)
