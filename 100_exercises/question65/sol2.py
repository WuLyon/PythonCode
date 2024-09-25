def compute(n):
    if n == 1:
        return {'ex': '1', 'sum': 1}
    else:
        sum = n + compute(n-1)['sum']
        expen = f"{str(n)} + {compute(n-1)['ex']}"
        return {'ex': expen, 'sum': sum}


print(f"{compute(5)['ex']} = {compute(5)['sum']}")
