def sum_digits(digits):
    total = 0
    for i, digit in enumerate(digits, start=1):
        # Se o índice (iniciando em 1) for ímpar, o valor do dígito é o dígito
        # original multiplicado por dois, com os dígitos resultantes somados,
        # o que equivale a subtrair 9 se o valor for maior que 9.
        # Se for par, o próprio dígito é utilizado, que já está entre 0 e 9.
        d = int(digit)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total


def check(digits):
    total = sum_digits(digits)
    return total % 10 == 0


def check_softnex(digits):
    total = sum_digits(digits[:15])
    # A Softnex diverge do Luhn tradicional no cálculo do último dígito.
    # Enquanto o Luhn apenas requer que a soma em módulo 10 seja 0, a Softnex
    # modifica o dígito para 1 se o mesmo for 0, o que faz com que o Luhn recuse
    # o número resultante.
    dv = 10 - total % 10
    if dv > 9:
        dv = 1
    return int(digits[-1]) == dv
