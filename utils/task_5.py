from functools import reduce

def age(data: list):
    summ = reduce(lambda x, y: x + y, [member['age'] for member in data])
    young = min(data, key=lambda x: list(x.values())[0])
    old = max(data, key=lambda x: list(x.values())[0])
    return summ, young, old

