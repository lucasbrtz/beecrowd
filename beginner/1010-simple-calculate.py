def simple_calculate():
    user_input = input()
    values = user_input.split()
    code_1 = int(values[0])
    units_1 = int(values[1])
    price_1 = float(values[2])

    user_input = input()
    values = user_input.split()
    code_2 = int(values[0])
    units_2 = int(values[1])
    price_2 = float(values[2])

    total = units_1 * price_1 + units_2 * price_2
    print(f"VALOR A PAGAR: R$ {total:.2f}")


simple_calculate()
