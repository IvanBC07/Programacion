decimales = [2.2, 3.4, 5.5]

def redondeo(d):
    return (round(d))

redondeos = list(map(redondeo, decimales))
print(redondeos)