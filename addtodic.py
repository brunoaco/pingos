def agregar_al_dic(word,into):
##sort el diccionario por largo de words
    print("["+word+"] sera agregado al diccionario")
    f = open(into,'a')
##si diccionario vacio, agregar word sin salto de carro
    f.write("\n"+word)
    f.close()
