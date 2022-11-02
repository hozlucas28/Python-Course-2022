# Importación
import myPackage.arithmetic as arit

# Función Principal
def main():
    add = arit.add(1, 5, 6, 7, 3, 2)
    substraction = arit.substraction(10, 3)
    potency = arit.potency(2, 3)

    print("• La suma es:", add)
    print("• La resta es:", substraction)
    print("• La potencia es:", potency)


# Punto de Entrada
if __name__ == "__main__":
    main()
