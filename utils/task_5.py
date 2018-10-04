from functools import reduce

def age(data: list):
    sum = reduce(lambda x, y: x + y, [member['age'] for member in data])
    young = reduce(lambda x, y: x if x['age'] < y['age'] else y, data)
    old = reduce(lambda x, y: x if x['age'] > y['age'] else y, data)
    return sum, young, old

