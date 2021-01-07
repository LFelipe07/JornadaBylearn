def numero_quadrado(numero):
  quadrado = numero * numero
  return  quadrado

def imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada
  return meu_imc

meu_imc = imc (92, 1.81)
print (f'o meu imc é {meu_imc:.2f}')
