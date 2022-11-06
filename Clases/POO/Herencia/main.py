# Importación
from person import Client, Employee

firstClient = Client("Lucas", 20)
secondClient = Client("Juan", 36)

firstClient.showData()
print(secondClient)


firstEmployee = Employee("Manuel", 26, 1250)
secondEmployee = Employee("Carlos", 42, 2650)

firstEmployee.showData()
print(secondEmployee)
