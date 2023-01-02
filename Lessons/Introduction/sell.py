# Mensaje guía
print('Valor de venta de un producto, con el IGV aplicado...')

# Entradas
productPrice = float(input('Ingrese el valor de venta del producto: $'))

# Operaciones
igv = productPrice * 0.18
finalPrice = round(productPrice + igv, 2)

# Salidas
print(f'Precio de venta del producto, con IGV aplicado: ${finalPrice}')
