# Entrada
price = float(input('Ingrese el consumo de la orden: '))

while price <= 0:
    print('¡Error!, el consumo debe ser mayor a cero')
    price = float(input('Ingrese el consumo de la orden: '))

# Procesos
if (price <= 100.00):
    discount = price * 0.1
elif (price > 100.00 and price <= 200.00):
    discount = price * 0.2
else:
    discount = price * 0.3
price -= discount

taxes = price * 0.19
price += taxes

price = round(price, 2)
taxes = round(taxes, 2)
discount = round(discount, 2)

# Salidas
print(
    f'• Descuento: ${discount}\n• Impuestos: ${taxes}\n• Importe a pagar: ${price}'
)
