def letras_favoritas(letra,frase):
	vezes=0
	for le in frase:
		if le.lower()==letra.lower():
			vezes+=1
	print('Sua letra favorita: ',letra)
	print('Uma frase importante: ',frase)
	print('Sua letra favorita é a letra {} e ela aparece {} vezes na frase "{}"'.format(letra.upper(),vezes,frase))
	
l=input('Digite sua letra favorita: ')
f=input('Digite uma frase: ')

letras_favoritas(l,f)
