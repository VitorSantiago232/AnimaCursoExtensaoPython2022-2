#Pede o nome do aulo e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "{nome}, Você é o bichão, mesmo..."
nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota"))

if (nota == 10):
  print(f"{nome}, é o bichão mesmo...")
elif (nota >= 6 and < 10):
  print(f"{nome}, bom trabalho")
else: # é sempre automaticamente o que as duas condições não tratamento
  print("Burro, não tirou dez..."

