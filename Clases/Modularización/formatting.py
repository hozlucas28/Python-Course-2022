# Importaciones
from sys import argv

if len(argv) == 4:
    name = argv[1]
    age = int(argv[2])
    height = float(argv[3])

    # Primer método de formateo
    # print(f"• Nombre: {name}\n• Edad: {age}\n• Altura: {height}")

    # Segundo método de formateo
    # print("• Nombre: {}\n• Edad: {}\n• Altura: {}".format(name, age, height))

    # Tercer método de formateo
    # print("• Nombre: {n}\n• Edad: {a}\n• Altura: {h}".format(a=age, h=height, n=name))

    # Cuarto método de formateo
    print("• Nombre: %s \n• Edad: %d \n• Altura: %.2f"%(name, age, height))
else:
    print("¡Error! No se has enviado tres argumentos.")
    print(
        "• Por ejemplo: C:/Python310/python.exe c:/Users/hozlu/Documents/Workspace/Python-Course-2022/Clases/Modularización/formatting.py 'Lucas' 20 1.73"
    )
