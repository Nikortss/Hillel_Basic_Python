def combination(coin: tuple, code: tuple):
    dict_result = {}
    for k, v in zip(coin, code):
        dict_result[k] = v
    return dict_result

