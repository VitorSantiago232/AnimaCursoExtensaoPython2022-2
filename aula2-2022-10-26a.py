# comando imput (): quero permitir que
#o usuario digite algo...

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print ("Olá seu nome é {} e sua idade é {}".format(nome, idade))
#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print ("O dobro da idade informada é {}". format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é jovem ainda, jovem ainda...")

  #E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
  #Mostre (...e você também precisa/precisou prestar o serviço militar obrigatorio)
  genero = str(input('Informe o seu gênero (M) para masculino ou (F) para feminino: ')).upper()
if genero == 'M'and idade >= 18:
  print('Você já prestou ou irá prestar o serviço militar obrigatório.')
elif genero == 'M' and idade < 18:
  print('Ainda não chegou a sua hora de prestar o serviço militar obrigatório, pois você não completou 18 anos.')
else:
  print('No Brasil, o serviço militar não é obrigatório para mulheres.')

  
