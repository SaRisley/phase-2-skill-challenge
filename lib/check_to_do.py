def check_to_do(text):
    to_do_list = []
    if text == None:
        raise Exception("Nothing provided")
    else:
        if "#TODO" in text:
            to_do_list.append(text)
        return to_do_list


