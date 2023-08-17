#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        mah = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[mah]:
                mah = key
        return mah
    return None
