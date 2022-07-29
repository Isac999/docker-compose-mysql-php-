import mysql.connector

insert = '''
INSERT INTO pessoa (cpf, nome, saldo)
VALUES (%s, %s, %s)
'''

while True:
	cpf = str(input('Cpf: '))
	nome = str(input('Nome: '))
	saldo = str(input('Saldo: '))
	values = (cpf, nome, saldo)
	try:
		db = mysql.connector.connect(
		        host = 'localhost',
		        user = 'isac',
		        password = ' ',
		        database = 'teste'
		)
	except:
		print('Algo deu errado!')

	else:
		cursor = db.cursor()
		cursor.execute(insert, values)
		db.commit()
		print('----commit feito-----')

