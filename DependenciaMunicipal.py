'''
def municipalidad(nombre):
	dep = {'excorreo': ['san martin 36','354732823'],'palacio':['pj concepcion 30','5435645645'],'promocion social':['bv alma fuerte 50','34234534534']}
	return dep[nombre]

nombre = input('ingrese el nombre de la dependecia municipal: ')

print(municipalidad(nombre))

'''



'''
def maximo(numero1,numero2):
		if numero1 >= numero2:
			return numero1
		else:
			return numero2

numero1 = input('ingrese un numero: ')

int(numero1)			
while type(numero1) != 'int':
	numero1 = input('ingrese un numero: ')

numero2 = input('ingrese otro numero: ')

int(numero2)	
while type(numero2) != 'int':
	numero2 = input('ingrese otro numero: ')


print(maximo(numero1,numero2))			
'''

'''
def maximo_de_tres(numero1,numero2,numero3):
	lista = [numero1,numero2,numero3]
	lista.sort()
	return lista[-1]



numero11 = input('ingrese el primer numero: ')
numero22 = input('ingrese el segundo numero: ')
numero33 = input('ingrese el tercer numero: ')	

print(maximo_de_tres(numero11,numero22,numero33))
'''

'''
def calcula_longitud(lista):

	for x in lista:
		x =+ 1
	return x



lista = ['hola','hola']

print(calcula_longitud(lista))
'''

