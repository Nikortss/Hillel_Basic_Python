def deleter(dictionary):
    new_dic = {k: v for k, v in dictionary.items() if v is not None}
    return new_dic

