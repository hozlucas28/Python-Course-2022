# Ingresar Monto
def getAmount():
    amount = float(input("Ingrese el monto a convertir: "))
    amount = round(amount, 2)
    return amount


# Conversor
def converter(fromCurrency, fromCurrencyAmount, toCurrency, toCurrencyAmount):
    convertedAmount = round(fromCurrencyAmount / toCurrencyAmount, 2)
    return f"• ${fromCurrencyAmount} ({fromCurrency}) --> ${convertedAmount} ({toCurrency})"


# Función Principal
def main():
    menu = """
        0 - Salir
        1 - Pesos argentinos --> Dolares estadounidenses
        2 - Dolares estadounidenses --> Pesos argentinos
        3 - Pesos mexicanos --> Dolares estadounidenses
        4 - Dolares estadounidenses --> Pesos mexicanos
        5 - Pesos colombianos --> Dolares estadounidenses
        6 - Dolares estadounidenses --> Pesos colombianos
        
        Ingrese una opción: """

    while True:
        optionSelected = int(input(menu))

        if optionSelected == 1:
            # ARS --> USD
            amount = getAmount()
            message = converter("ARS", amount, "USD", 156.14)
        elif optionSelected == 2:
            # USD --> ARS
            amount = getAmount()
            message = converter("USD", amount, "Pesos Argentinos", 0.0064)
        elif optionSelected == 3:
            # MXN --> USD
            amount = getAmount()
            message = converter("MXN", amount, "USD", 19.83)
        elif optionSelected == 4:
            # USD --> MXN
            amount = getAmount()
            message = converter("USD", amount, "MXN", 0.050)
        elif optionSelected == 5:
            # COP --> USD
            amount = getAmount()
            message = converter("COP", amount, "USD", 4835.01)
        elif optionSelected == 6:
            # USD --> COP
            amount = getAmount()
            message = converter("USD", amount, "COP", 0.00021)
        elif optionSelected == 0:
            # Salir
            break
        else:
            message = "¡La opción ingresada no es valida!, vuelva a intentar..."
        print(message)


# Punto de Entrada
if __name__ == "__main__":
    main()
