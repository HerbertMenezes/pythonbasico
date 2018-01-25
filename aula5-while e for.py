nomes = ['abc', 'def', 'ghi', 'jkl']

for x in nomes:
    print(x)

lista_de_numeros = range(5)

for i in lista_de_numeros:
    print(i)

lista_de_numeros = range(5, 10)
for i in lista_de_numeros:
    print(i)

lista_de_numeros = range(0, 100, 2)
for i in lista_de_numeros:
    print(i)

for i in range(4):
    print(nomes[i])

for i in range(len(nomes)):
    print(nomes[i])

i = 0
while i < 10:
    print('Ainda é menor que 10: ', i)
    i += 1
    if i == 5:
        break
