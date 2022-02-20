listadetuplas_valores_a_romanos=[
    (1000,'M'),
    (900,'CM'),
    (500,'D'),
    (400,'CD'),
    (100,'C'),
    (90,'XC'),
    (50,'L'),
    (40,'XL'),
    (10,'X'),
    (9,'IX'),
    (5,'V'),
    (4,'IV'),
    (1,'I')   
]

def arabigo_a_romano(n):
    romano='' 
    resto=None 
    while resto!=0: 
        for valor1,valor2 in listadetuplas_valores_a_romanos: 
            if n>=valor1: 
                break
        cociente=n//valor1 
        resto=n%valor1 
        n=resto 
        romano=romano+(cociente*valor2)
    return romano

for i in range(1,101):
		print(arabigo_a_romano(i))