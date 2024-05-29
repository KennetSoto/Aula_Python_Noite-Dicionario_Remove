pessoa = {
    'Nome': 'Mazza',
    'Idade': 35,
    'Profissão': 'Gerente',
    'Empresa': 'Maraba',
    'Genero': 'Fluido',
    'Cidade': 'São Paulo'
}
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

del pessoa[input('Informe o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')