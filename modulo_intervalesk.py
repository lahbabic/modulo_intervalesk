def modulo_in_interval(number, lower_limit, upper_limit, modulo):
    while number < lower_limit:
        number += modulo
    while number > upper_limit:
        number -= modulo
    return number
