<<<<<<< HEAD
import os
import re
import sys
from query_y_o_no import query_yes_no
from addtodic import agregar_al_dic
from limpia_chars import limpia_chars
#import number_check_repair as ncr

#file_name = "C:\\Users\\\Deyanira\\Downloads\\comprasoctubre2017-alt.txt"
file_name = "C:\\Users\\\Deyanira\\Downloads\\ventasmarzo2018-alt.txt"
file_name = "C:\\Users\\RVK-02\\Downloads\\ventasseptiembre2021-alt.txt"
#file_name = "C:\\Users\\acobar\\Google Drive\\LOS PINGOS-PROANIMAL-JAVIER JEREZ\\IVA 08 2018\\LOS PINGOS\\VENTAS 08 2018.txt"
#file_name = "C:\\Users\\acobar\\Google Drive\\LOS PINGOS-PROANIMAL-JAVIER JEREZ\\IVA 09 2018\\LOS PINGOS (OJO revisar para IVA)\\VENTAS 09 2018.txt"

diccionario_file = "diccionario.txt"

diccionario = []
diccionario_extendido = []
contenido = ""


def carga_diccionario():
    global diccionario_file
    global diccionario
    global diccionario_extendido

    diccionario_extendido = []
    diccionario = []

    if (os.path.isfile(diccionario_file)):
        ##iterar en el diccionario
        file_object = open(diccionario_file, "r")
        diccionario = [x.strip('\n') for x in file_object.readlines()]
        diccionario.sort(key=len, reverse=True)
        file_object.close()

        for j in diccionario:
            new_palabra = ""
            palabra = j

            for k in palabra:
                if (k != " "):
                    new_palabra += (k + " ")

            diccionario_extendido += [new_palabra.strip()]
    else:
        print("diccionario.txt no existe!!!!!")
    # TODO: OPCION CREAR DICCIONARIO

    return


carga_diccionario()


def data_grinding():
    global match_arr
    global largo
    global contenido
    modificado = bool(False)

    if match_arr:
        print("\nAcontinuacion los candidatos a ser agregados al diccionario(" + str(largo) + " items):")
        temp_string = ""
        modificado = bool(False)

        for x in range(0, largo):
            print("[" + match_arr[x] + "]")
            alternativas=[]
            for b in list(re.finditer(match_arr[x], contenido)):
                pos_letra_ini = b.start()
                while ord(contenido[pos_letra_ini]) != 10:
                    pos_letra_ini -= 1

                pos_letra_fin = b.end()
                while ord(contenido[pos_letra_fin]) != 10:
                    pos_letra_fin += 1

                my_sub=""
                my_sub = contenido[pos_letra_ini + 1:pos_letra_fin]
                ms=""
                for ms in my_sub.split("|"):
                    if (match_arr[x] in ms):
                        try:
                            alternativas.index(ms)
                        except:
                            pos_antes = ms.index(match_arr[x])
                            while pos_antes > 0 and " " in ms[pos_antes-2:pos_antes]:
                                pos_antes-=1
                            pos_despues = ms.index(match_arr[x])
                            while pos_despues < len(ms)+1 and " " in ms[pos_despues:pos_despues+2]:
                                pos_despues+=1
                            try:
                                alternativas.index(ms[pos_antes:pos_despues])
                            except:
                                alternativas.append(ms[pos_antes:pos_despues])
                my_sub = my_sub.replace(match_arr[x],"[" + match_arr[x] + "]")
                print("\t\t" + my_sub)
            print("")
            for cell in range(0,len(alternativas)):
                alternativas[cell]=alternativas[cell].replace(" ","")
                print("("+str(cell)+"):"+alternativas[cell]+".-")


            ##preguntar si incluir palabra en diccionario
            ignore = bool(True)
            ignore = query_yes_no("ignorar esta \"palabra\"?", "yes")

            if (ignore == False):
                word=""
                if(query_yes_no("usar alternativa?", "yes")):
                    try:
                        val=int(input("Seleccione alternativa:"))
                        word=str(alternativas[val % len(alternativas)]  )
                    except ValueError:
                        print("no es un numero")
                else:
                    print("Escriba la palabra (sensible a mayusculas y minusculas): ")
                    word = input()
                agregar_al_dic(word, diccionario_file)
                carga_diccionario()
                return bool(True)

                modificado = bool(True)

    # todo: regex para \++\-+  y luego \+ para ser reemplazados por \| para dejar las tablas finales compatibles en formato

    return modificado


def carga_contenido():
    global contenido
    global diccionario
    global diccionario_extendido
    global file_name

    if (os.path.isfile(file_name)):
##        print("file exists")
        file_object = open(file_name, "r")
        contenido = file_object.read()
        contenido = limpia_chars(contenido)

        for x in range(0, 10):
            for y in range(0, 10):
                contenido = contenido.replace(str(x) + " " + str(y), str(x) + str(y))
                contenido = contenido.replace(str(x) + " " + str(y), str(x) + str(y))

                contenido = contenido.replace(str(x) + " , " + str(y), str(x) + "." + str(y))
                contenido = contenido.replace(str(x) + " . " + str(y), str(x) + "." + str(y))
                contenido = contenido.replace(str(x) + " - " + str(y), str(x) + "-" + str(y))
                contenido = contenido.replace(str(x) + "," + str(y), str(x) + "." + str(y))
            contenido = contenido.replace(str(x) + " - K", str(x) + "-K")

        

        for i in range(0, len(diccionario)):
            
##--falta debuguear algunos temas de orden en que se hacen los reemplazos
#            if contenido.find(diccionario_extendido[i])>=0:
#                print(diccionario[i])
#                print(contenido.find(diccionario_extendido[i]))
#                print(diccionario_extendido[i] + "-extendido")
#                print(contenido)
#                print(contenido.replace(" "+diccionario_extendido[i]+" ", diccionario[i] + " "))
#                input()
            
                
            contenido = contenido.replace(" "+diccionario_extendido[i]+" ", " "+diccionario[i] + " ")

        file_object.close()
        
        #--NO CONSIGO RECORDAR PARA QUE ERALA SIGUIENTE LINEA--
        #contenido = ncr.number_format_chek_and_repair(contenido)
        
    else:
        print("el archivo [" + file_name + "] no existe")

    return

carga_contenido()


match_arr = re.findall(r' [\w] [\w] ', contenido, flags=0)
match_arr = sorted(list(set(match_arr)))
largo = len(match_arr)
while (data_grinding()):
    carga_contenido()
    for i in range(0, len(diccionario)):
        contenido = contenido.replace(" "+diccionario_extendido[i]+" ", " "+diccionario[i] + " ")
    match_arr = re.findall(r' [\w] [\w] ', contenido, flags=0)
    match_arr = sorted(list(set(match_arr)))
    largo = len(match_arr)

            
contenido = contenido.replace("  ", " ")
contenido = contenido.replace("| ", "|")
contenido = contenido.replace(" |", "|")

file = open("salida.txt", "w")
file.write(contenido)
file.close()

print("\-\-FIN\-\-")
=======
import os
import re
import sys
from query_y_o_no import query_yes_no
from addtodic import agregar_al_dic
from limpia_chars import limpia_chars
#import number_check_repair as ncr

#file_name = "C:\\Users\\\Deyanira\\Downloads\\comprasoctubre2017-alt.txt"
file_name = "C:\\Users\\\Deyanira\\Downloads\\ventasmarzo2018-alt.txt"
file_name = "C:\\Users\\RVK-02\\Downloads\\ventasseptiembre2021-alt.txt"
#file_name = "C:\\Users\\acobar\\Google Drive\\LOS PINGOS-PROANIMAL-JAVIER JEREZ\\IVA 08 2018\\LOS PINGOS\\VENTAS 08 2018.txt"
#file_name = "C:\\Users\\acobar\\Google Drive\\LOS PINGOS-PROANIMAL-JAVIER JEREZ\\IVA 09 2018\\LOS PINGOS (OJO revisar para IVA)\\VENTAS 09 2018.txt"

diccionario_file = "diccionario.txt"

diccionario = []
diccionario_extendido = []
contenido = ""


def carga_diccionario():
    global diccionario_file
    global diccionario
    global diccionario_extendido

    diccionario_extendido = []
    diccionario = []

    if (os.path.isfile(diccionario_file)):
        ##iterar en el diccionario
        file_object = open(diccionario_file, "r")
        diccionario = [x.strip('\n') for x in file_object.readlines()]
        diccionario.sort(key=len, reverse=True)
        file_object.close()

        for j in diccionario:
            new_palabra = ""
            palabra = j

            for k in palabra:
                if (k != " "):
                    new_palabra += (k + " ")

            diccionario_extendido += [new_palabra.strip()]
    else:
        print("diccionario.txt no existe!!!!!")
    # TODO: OPCION CREAR DICCIONARIO

    return


carga_diccionario()


def data_grinding():
    global match_arr
    global largo
    global contenido
    modificado = bool(False)

    if match_arr:
        print("\nAcontinuacion los candidatos a ser agregados al diccionario(" + str(largo) + " items):")
        temp_string = ""
        modificado = bool(False)

        for x in range(0, largo):
            print("[" + match_arr[x] + "]")
            alternativas=[]
            for b in list(re.finditer(match_arr[x], contenido)):
                pos_letra_ini = b.start()
                while ord(contenido[pos_letra_ini]) != 10:
                    pos_letra_ini -= 1

                pos_letra_fin = b.end()
                while ord(contenido[pos_letra_fin]) != 10:
                    pos_letra_fin += 1

                my_sub=""
                my_sub = contenido[pos_letra_ini + 1:pos_letra_fin]
                ms=""
                for ms in my_sub.split("|"):
                    if (match_arr[x] in ms):
                        try:
                            alternativas.index(ms)
                        except:
                            pos_antes = ms.index(match_arr[x])
                            while pos_antes > 0 and " " in ms[pos_antes-2:pos_antes]:
                                pos_antes-=1
                            pos_despues = ms.index(match_arr[x])
                            while pos_despues < len(ms)+1 and " " in ms[pos_despues:pos_despues+2]:
                                pos_despues+=1
                            try:
                                alternativas.index(ms[pos_antes:pos_despues])
                            except:
                                alternativas.append(ms[pos_antes:pos_despues])
                my_sub = my_sub.replace(match_arr[x],"[" + match_arr[x] + "]")
                print("\t\t" + my_sub)
            print("")
            for cell in range(0,len(alternativas)):
                alternativas[cell]=alternativas[cell].replace(" ","")
                print("("+str(cell)+"):"+alternativas[cell]+".-")


            ##preguntar si incluir palabra en diccionario
            ignore = bool(True)
            ignore = query_yes_no("ignorar esta \"palabra\"?", "yes")

            if (ignore == False):
                word=""
                if(query_yes_no("usar alternativa?", "yes")):
                    try:
                        val=int(input("Seleccione alternativa:"))
                        word=str(alternativas[val % len(alternativas)]  )
                    except ValueError:
                        print("no es un numero")
                else:
                    print("Escriba la palabra (sensible a mayusculas y minusculas): ")
                    word = input()
                agregar_al_dic(word, diccionario_file)
                carga_diccionario()
                return bool(True)

                modificado = bool(True)

    # todo: regex para \++\-+  y luego \+ para ser reemplazados por \| para dejar las tablas finales compatibles en formato

    return modificado


def carga_contenido():
    global contenido
    global diccionario
    global diccionario_extendido
    global file_name

    if (os.path.isfile(file_name)):
##        print("file exists")
        file_object = open(file_name, "r")
        contenido = file_object.read()
        contenido = limpia_chars(contenido)

        for x in range(0, 10):
            for y in range(0, 10):
                contenido = contenido.replace(str(x) + " " + str(y), str(x) + str(y))
                contenido = contenido.replace(str(x) + " " + str(y), str(x) + str(y))

                contenido = contenido.replace(str(x) + " , " + str(y), str(x) + "." + str(y))
                contenido = contenido.replace(str(x) + " . " + str(y), str(x) + "." + str(y))
                contenido = contenido.replace(str(x) + " - " + str(y), str(x) + "-" + str(y))
                contenido = contenido.replace(str(x) + "," + str(y), str(x) + "." + str(y))
            contenido = contenido.replace(str(x) + " - K", str(x) + "-K")

        

        for i in range(0, len(diccionario)):
            
##--falta debuguear algunos temas de orden en que se hacen los reemplazos
#            if contenido.find(diccionario_extendido[i])>=0:
#                print(diccionario[i])
#                print(contenido.find(diccionario_extendido[i]))
#                print(diccionario_extendido[i] + "-extendido")
#                print(contenido)
#                print(contenido.replace(" "+diccionario_extendido[i]+" ", diccionario[i] + " "))
#                input()
            
                
            contenido = contenido.replace(" "+diccionario_extendido[i]+" ", " "+diccionario[i] + " ")

        file_object.close()
        
        #--NO CONSIGO RECORDAR PARA QUE ERALA SIGUIENTE LINEA--
        #contenido = ncr.number_format_chek_and_repair(contenido)
        
    else:
        print("el archivo [" + file_name + "] no existe")

    return

carga_contenido()


match_arr = re.findall(r' [\w] [\w] ', contenido, flags=0)
match_arr = sorted(list(set(match_arr)))
largo = len(match_arr)
while (data_grinding()):
    carga_contenido()
    for i in range(0, len(diccionario)):
        contenido = contenido.replace(" "+diccionario_extendido[i]+" ", " "+diccionario[i] + " ")
    match_arr = re.findall(r' [\w] [\w] ', contenido, flags=0)
    match_arr = sorted(list(set(match_arr)))
    largo = len(match_arr)

            
contenido = contenido.replace("  ", " ")
contenido = contenido.replace("| ", "|")
contenido = contenido.replace(" |", "|")

file = open("salida.txt", "w")
file.write(contenido)
file.close()

print("\-\-FIN\-\-")
>>>>>>> b98379131e1838797677008c2d49bd371840a958
