# Variables
counter = 0

# Salida
while counter < 10:
    counter += 1
    print(counter)

    if counter == 5:
        # print('El while ha sido interrumpido.')
        # break
        continue
    print('Iteración...')
else:
    print('El while ha terminado su recorrido.')