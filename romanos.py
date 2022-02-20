listadetuplas_valores_a_romanos=[
    (1000,'M'),
    (500,'D'),
    (100,'C'),
    (50,'L'),
    (10,'X'),
    (5,'V'),
    (1,'I')   
]

def arabigo_a_romano(n):
    romano='' #romano es un str vació (str porque contendrá letras, no números)
    resto=None #tengo que definir el resto con algún valor inicial distinto de 0, vale el valor que sea, es sólo para que entre al while.
    while resto!=0: #entro con un número (n) inicial. Ejemplo n=36. Que luego cambiará con cada iteración.
        for valor1,valor2 in listadetuplas_valores_a_romanos: #recorro la lista de tuplas, par a par de valores
            if n>=valor1: #si el número (n) es mayor o igual que el valor1 de cada par, me salgo. Ejemplo: si n=36, saldrá con valor1=10
                break
        cociente=n//valor1 #Ejemplo: cociente=36//10=3 
        resto=n%valor1 #Ejemplo: resto=6
        n=resto #ahora mi nuevo n, será ese resto
        romano=romano+(cociente*valor2) #Ejemplo: romano=''+3*'X' >>> De aquí sacaría XXX. Python puede multiplicar str. #se podría poner romano+=cociente*valor2       
    #De aquí volvería a entrar al while. Y sacaría 6//5=1 >>> V y resto=1. Y de nuevo al while 1//1=1 >>> I y resto=0. El while se hace mientras el resto no sea =0.
    return romano

for i in range(1,101):
	print(arabigo_a_romano(i))