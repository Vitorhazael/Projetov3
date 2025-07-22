nome = input('DIGITE SEU NOME: ')
idade = input('DIGITE SUA IDADE: ')

if nome and idade:# AQUI EM CIMA E O AND QUE VAI CONECTAR AMBOS.
  print(f'seu nome e {nome}')
  print(f'seu nome invertido e {nome[::-1]}')# O TRUQUE PARA INVERTER E PEGAR O PRIMEIRO E ULTIMO NUMERO ESTA AI, -1.
  
                   
  if ' ' in nome: #COM ESSE COMANDO ELE VAI CHECAR SE TEM ESPACOS DENTRO DO NOME. 
    print('seu nome contem espacos')
  else:
    print('seu nome nao contem espacos')

  print(f'seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome e {nome[0]}')#QUANDO FOR PEGAR A PRIMEIRA LETRA DO NOME.
  print(f'a ultima letra do seu nome e {nome[-1]}')# PARA CHEGAR QUAL A ULTIMA LETRA DO SEU NOME E SO USAR O -1.

else:
  
  print('Desculpe voce deixou campos vazios') 
  # ELE TE DA ALGUMAS COIAS COMO SUAS INFROMACOES DE NOME, NOME INVERTIDO, SE SEU NOME CONTEM ESPACOS,
  # QUANTIDADE DE LETRAS EM CARACTERES, A PRIMEIRA E ULTIMA LETRA DO SEU NOME,
  # E CASO NAO PREENCHA ELE APRESENTA OUTRA MENSAGEM.