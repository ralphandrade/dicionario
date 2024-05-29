import os

pessoa = {
    'Nome' :input('informe o seu nome: '),
    'CPF':input('informe o CPF: '),
    'RG' :input('Informe o RG: '),
    'Data de Nascimento' :input('Informe a Data de Nascimento: '),
    'Gênero' :input('Informe o Gênero: '),
    'E-mail' :input("Informe o E-mail: "),
    'Telefone' :input('Informe o Telefone: '),
    'Tipo Sanguíneo' :input('Informe o Tipo sanguíneo: '),
    'Profissão' :input('Informe a Profissão: '),
    'Empresa':input('Informe a Empresa: ')
}

os.system('cls')

print(f'{'-'*30} DADOS DA PESSOA {'-'*30}\n')

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')