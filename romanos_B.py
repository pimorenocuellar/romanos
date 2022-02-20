dict_valores_a_romanos={
    1000:'M',
    900:'CM',
    500:'D',
    400:'CD',
    100:'C',
    90:'XC',
    50:'L',
    40:'XL',
    10:'X',
    9:'IX',
    5:'V',
    4:'IV',
    1:'I'
}

def arabigo_a_romano(n):
    romano=''
    resto=None
    while resto!=0:
        for key in sorted(dict_valores_a_romanos.keys(),reverse=True): #con sorted ordeno el diccionario. Con .keys lo hago según la clave. Con reverse=True, lo hago de mayor a menor. 
        #Si pusiera .values lo ordenaría por valor. Y sino pusiera el reserve o pusiera reverse=False, iría de menor a mayor.
            if n>=key:
                break
        cociente=n//key
        resto=n%key
        n=resto
        romano=romano+(cociente*dict_valores_a_romanos[key]) #Se accede al valor usando dict[key]=value
    return romano

for i in range(1,101):
	print(arabigo_a_romano(i))