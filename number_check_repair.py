import re
def number_format_chek_and_repair(contenido):
    match_arr = re.findall( r'\.[\d][\d][\d][\d]',contenido,flags=0)
    numerito=""
    principio=""
    fin=""
    if  match_arr:
        for m in match_arr:
            numerito=contenido[contenido.find(m)-1:contenido.find(m)+7]
            principio=numerito[0:5]
            fin=numerito[5:8]
            contenido=contenido.replace(numerito,principio+"|"+fin)
    return contenido
