##################################################################################################################################
#   1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
##################################################################################################################################

print("==="*30)
numero = int(input("Digite um número: "))
sequenciaFibonacci = [0 ,1]
totalElementos = 2
tamanhoLista = len(sequenciaFibonacci)

while ( tamanhoLista < numero ):
    
    penultimoNumero = sequenciaFibonacci[-2]
    ultimoNumero = sequenciaFibonacci[-1]
    
    proximoNumero =  penultimoNumero + ultimoNumero
    sequenciaFibonacci.append(proximoNumero)

    tamanhoLista += 1

if numero in sequenciaFibonacci:
    print(f"o número {numero} faz parte da sequência de Fibonacci.")
else:
    print(f"o número {numero} não faz parte da sequência de Fibonacci.")

print("==="*30)
# print(sequenciaFibonacci)
