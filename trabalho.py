#exerc3
from functools import reduce

exerc3= reduce(lambda x, y: x + y, [1,2,3,4,5])
print(exerc3)

#exerc4
exerc4=list(filter(lambda x: len(x) > 4, ["ana","lucas", "fernanda", "joao"] ))
print(exerc4)

#exerc5
quadrado = list(map(lambda x: x**2, [1,5,3,2,4]))
print(sorted(quadrado))

#exerc6
lista_inteiro = [1,2,3,4,5] 
dic= {
   "impar": [],
    "par": []
}

list(filter(lambda x: dic["par"].append(x) if x % 2==0 else dic["impar"].append(x), lista_inteiro
))
print(dic)

#exerc7
lista_int = [-1,0,1,2,-3,4,5,0] 
dicionario= {
   "positivo": list(filter(lambda x: x > 0, lista_int)),
    "negativo": list(filter(lambda x: x < 0, lista_int)),
    "zeros": list(filter(lambda x: x == 0, lista_int))
}
print(dicionario)

#exerc8
from functools import reduce
list = ["casa", "python", "lambda"]
contag = reduce(lambda x, y: x + y, map(len, list), 0)
print(contag)

#exerc9
lista_tupla = [(2, 8), (4, 5, 6), (1, 2)]
media= list(filter(lambda x: x >= 5,(map(lambda x: sum(x) / len(x),lista_tupla ))))
print(media)

#exerc10

dicionarios = {
    'Ana'
}