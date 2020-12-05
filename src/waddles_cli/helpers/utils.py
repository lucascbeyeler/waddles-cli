def merge_two_dictionaries(object_1: dict, object_2: dict) -> dict:
    """ Merge the second dict inside the first dict

    :param object_1: The first dictionary
    :param object_2: The second dictionary
    :return: An updated object_1 with the values from object_2
    """
    if isinstance(object_1, dict) and isinstance(object_2, dict):
        new_dict = {}
        dict_keys = list(object_1.keys()) + list(object_2.keys())
        for key in dict_keys:
            new_dict[key] = merge_two_dictionaries(object_1=object_1.get(key, None), object_2=object_2.get(key, None))
        return new_dict
    elif not object_2:
        return object_1
    return object_2