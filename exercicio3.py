n=int(input('Digite quantos números terá a sequência: '))
numero_anterior=1
numero_bem_anterior=0
primeiro=numero_bem_anterior
segundo=numero_anterior
print('fib({}) = {}'.format('0',primeiro))
print('fib({}) = {}'.format('1',segundo))
indice=1
while indice<n:
	indice+=1
	numero_novo=numero_anterior+numero_bem_anterior
	print('fib({}) = {}'.format(indice,numero_novo))
	numero_bem_anterior=numero_anterior
	numero_anterior=numero_novo
	
	
