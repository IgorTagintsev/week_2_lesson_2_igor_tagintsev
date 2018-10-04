from re import search

def name_filter(data: list):
    return list(filter(lambda x: search(r'o',x['name']), data))