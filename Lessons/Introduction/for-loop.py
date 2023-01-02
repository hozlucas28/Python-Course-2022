# Variables
data = ['Lucas', 'Nahuel', 20, 157.56, True]
counter = 0

# Recorrido - Primer método
for element in data:
    print(f'{element}')

print('')

# Recorrido - Segundo método
while counter < len(data):
    print(f'{data[counter]}')
    counter += 1
