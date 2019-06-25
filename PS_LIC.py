
#Exercicio 2
def valor(numero):
	tam=len(str(int(numero)))
	resto_caracteres=tam-1
	numero_um_digito=numero
	for i in range (0,resto_caracteres):
		numero_um_digito=numero_um_digito/10
	if resto_caracteres==0:
		unidade='Unidade(s)'
	elif resto_caracteres==1:
		unidade='Dezena(s)'
	elif resto_caracteres==2:
		unidade='Centena(s)'
	elif resto_caracteres==3:
		unidade='Milhar(es)'
	elif resto_caracteres==4:
		unidade='Dezena(s) de milhar'
	elif resto_caracteres==5:
		unidade='Centena(s) de milhar'
	elif resto_caracteres==6:
		unidade='Milhão(ões)'
	elif resto_caracteres==7:
		unidade='Dezena(s) de milhão'
	elif resto_caracteres==8:
		unidade='Centena(s) de milhão'
	elif resto_caracteres==9:
		unidade='Bilhão(ões)'
	elif resto_caracteres==10:
		unidade='Dezena(s) de bilhão'
	elif resto_caracteres==11:
		unidade='Centena(s) de bilhão'
	elif resto_caracteres==12:
		unidade='Trilhão(ões)'
	arredondado=round(numero_um_digito,2)
	numero_formatado=('{} {}'.format(arredondado,unidade))
	return numero_formatado

#teste	
print(valor(2596061015))


#Exercicio 4
linhas_tabela=['2013,Frozen,1276480335','2012,Marvel s The Avengers,1518812988','1997,Titanic,2187463944','2018,Black Panther,1346913161','2015,Avengers: Age of Ultron,1405403694','2009,Avatar,2787965087','2015,Star Wars: The Force Awakens,2068223624','2017,Star Wars: The Last Jedi,1332539889','2015,Furious 7,1516045911','2011,Harry Potter and the Deathly Hallows – Part 2,1341693157','2019,Avengers: Endgame,2750667499','2015,Jurassic World,1671713208','2018,Avengers: Infinity War,2048359754','2017,Beauty and the Beast,1263521126','2018,Jurassic World: Fallen Kingdom,1309484461']

ano_bilheteria={1997:0,2009:0,2011:0,2012:0,2013:0,2015:0,2017:0,2018:0,2019:0}
for linha in linhas_tabela:
	linha_separada=linha.split(',')
	ano=int(linha_separada[0])
	filme=linha_separada[1]
	bilheteria=float(linha_separada[2])
	if ano==1997:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2009:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2011:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2012:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2013:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2015:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2017:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2018:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria
	elif ano==2019:
		ano_bilheteria[ano]=ano_bilheteria[ano]+bilheteria

for ano in ano_bilheteria:
	print('Valor arrecadado em {}:	US$ {}'.format(ano,ano_bilheteria[ano]))

#Exercicio 5
linhas_tabela=['2013,Frozen,1276480335','2012,Marvel s The Avengers,1518812988','1997,Titanic,2187463944','2018,Black Panther,1346913161','2015,Avengers: Age of Ultron,1405403694','2009,Avatar,2787965087','2015,Star Wars: The Force Awakens,2068223624','2017,Star Wars: The Last Jedi,1332539889','2015,Furious 7,1516045911','2011,Harry Potter and the Deathly Hallows – Part 2,1341693157','2019,Avengers: Endgame,2750667499','2015,Jurassic World,1671713208','2018,Avengers: Infinity War,2048359754','2017,Beauty and the Beast,1263521126','2018,Jurassic World: Fallen Kingdom,1309484461']

maior_sucesso=0
for linha in linhas_tabela:
	linha_separada=linha.split(',')
	ano=int(linha_separada[0])
	filme=linha_separada[1]
	bilheteria=float(linha_separada[2])
	if bilheteria>maior_sucesso:
		maior_sucesso=bilheteria
		filme_sucesso=filme
		ano_sucesso=ano
		
print('Maior sucesso: {} \n {} \n US$ {} arrecadados'.format(filme_sucesso,ano_sucesso,valor(maior_sucesso)))
