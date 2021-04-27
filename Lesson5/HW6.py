def deleter(dictionary):
    an_dic = dictionary.copy()
    for key, values in dictionary.items():
        if not values:
            an_dic.pop(key)
    return an_dic
