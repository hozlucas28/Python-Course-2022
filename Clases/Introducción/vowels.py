# ------------------------------------------------------------------------- #
# APUNTES:
# 		   <elif>: se traduce a 'sino', como si se tratase de un <case> en un
#                  switch.
#
#
# IMPORTANTE:
#  			  - XXX.
# ------------------------------------------------------------------------- #

# Entrada
character = input('Ingrese un carácter: ')

# Salidas
if character == 'a' or character == 'A':
    print(f'El carácter {character} es vocal')
elif character == 'e' or character == 'E':
    print(f'El carácter {character} es vocal')
elif character == 'i' or character == 'I':
    print(f'El carácter {character} es vocal')
elif character == 'o' or character == 'O':
    print(f'El carácter {character} es vocal')
elif character == 'e' or character == 'U':
    print(f'El carácter {character} es vocal')
else:
    print(f'El carácter {character} no es vocal')