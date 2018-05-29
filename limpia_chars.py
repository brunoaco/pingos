def limpia_chars(contenido):

    contenido=contenido.replace(str(chr(1)),"|")
    contenido=contenido.replace(str(chr(2)),"+")
    contenido=contenido.replace(str(chr(3)),"-")
    contenido=contenido.replace(str(chr(4)),"+")
    contenido=contenido.replace(str(chr(5)),"+")
    contenido=contenido.replace(str(chr(6)),"|")
    contenido=contenido.replace(str(chr(7)),"-")
    contenido=contenido.replace(str(chr(8)),"|")
    return contenido