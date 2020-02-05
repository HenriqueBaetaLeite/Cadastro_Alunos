from datetime import date
from time import sleep

lista_Aluno = []
while True:
    print('''Menu de escolha:
          1 - Cadastro de novo aluno
          2 - Registar pagamento
          3 - Histórico do aluno
          4 - Sair do programa''')
    opção = int(input('Escolha sua opção: '))
    sleep(.5)

    if opção == 1:
        anoatual = date.today().year
        print('<<< Cadastrar novo aluno >>>')
        nome = str(input('Nome: '))
        nascimento = int(input('Ano de nascimento: '))
        altura = float(input('Altura (m): '))
        peso = float(input('Peso (Kg): '))
        idade = anoatual - nascimento
        imc = peso / altura ** 2
        fcmax = 220 - idade
        print('Aluno registrado com sucesso!')
        sleep(.5)
        print(f'{nome} tem {idade} anos de idade\nSeu IMC é {imc:.2f}\nSua Frequência cardíaca Máxima é de {fcmax} BPM')
        lista_Aluno.append([nome, idade, peso, imc, fcmax])

    elif opção == 2:
        print('<<< Registrar pagamento >>>')

    elif opção == 3:
        print('<<< Histórico do aluno >>>')
        print(str(input('Digite o nome do aluno: ')))
        for a in lista_Aluno:
            print(f'Atualmente o aluno {a[0]} tem {a[1]} anos, está com {a[2]} Kg, seu IMC é de {a[3]:.1f} e sua FC máxima é de {a[4]} BPM.')

    elif opção == 4:
        print('Finalizando...')
        sleep(1)
        break

    elif opção < 1 or opção > 4:
        print('Opção inválida, tente novamente...')
