def media_final(a1,p1,a2,p2):
	mf=(a1*2+p1*4+a2*3+p2*3)/(2+4+3+3)
	round(mf,2)
	print('A1:{} \t P1:{}'.format(a1,p1))
	print('A2:{} \t P2:{}'.format(a2,p2))
	print('MF:{}'.format(mf))
	
a1=float(input('Digite a nota da Atividade 1: '))
a2=float(input('Digite a nota da Atividade 2: '))
p1=float(input('Digite a nota da Prova 1: '))
p2=float(input('Digite a nota da Prova 2: '))

media_final(a1,p1,a2,p2)
