"""
Este programa es un analizador léxico que reconoce tokens para el lenguaje de programación inventado GOX. 
Los tokens son los elementos básicos que componen un lenguaje.

"""
import tokenModule as tm
import tokenPatterns as tp

def tokenize(code):
  #Lista vacia para almacenar los tokens
  tokenList = []
  #Contador de la linea actual
  lineon = 1
  #Contador
  index = 0
  
  #Bucle para recorrer el codigo fuente
  while index < len(code):    
    #1. Ignorar espacios en blanco, tabulaciones y saltos de linea
    if code[index] in [' ', '\t', '\n']:
      if code[index] == '\n':
        lineon += 1
      index += 1
      continue

    #2. Comprobar si el token es un comentario
    if code[index:index+2] == '/*':
      posChar=code.find('*/',index+2)#Buscar la posicion del cierre del comentario
      #Si no se encuentra el cierre del comentario se muestra un error y se termina el programa
      if posChar==-1:
        print(f'Error: Comentario no cerrado en la linea {lineon}')
        break
      index=posChar+2 #Se actualiza la posicion del codigo fuente al final del comentario
      continue

    #3. Ignorar comentarios de linea
    if code[index:index+2] == '//':
        posChar = code.find('\n', index+2)
        if posChar == -1:  # Si no hay salto de línea, terminamos el análisis
            break
        index = posChar + 1
        lineon += 1
        continue

    #4. Identificar nombres (identificadores)
    result=tp.NAME_PAT.match(code,index)
    if result:
      #Se obtiene el valor del token
      value=result.group()
      #Buscar si el token es una palabra reservada
      if value in tp.TOKEN_PATTERNS["KEYWORDS"]:
        #Se obtiene el tipo del token
        type=tp.TOKEN_PATTERNS["KEYWORDS"][value]
        #Se crea un objeto token
        token=tm.Token(type,value,lineon)
        #Se agrega el token a la lista de tokens
        tokenList.append(token)
        #Se actualiza la posicion del codigo fuente
        index += len(value)
        continue #Se continua con el siguiente token
      else: #Si el token no es una palabra reservada
        #Se crea un objeto token
        token=tm.Token("ID",value,lineon)
        #Se agrega el token a la lista de tokens
        tokenList.append(token)
        #Se actualiza la posicion del codigo fuente
        index += len(value)
        continue

    #5. Identificar numeros flotantes
    result=tp.FLOAT_PAT.match(code,index)
    if result:
      #Se obtiene el valor del token
      value=result.group()
      #Se crea un objeto token
      token=tm.Token("FLOAT",value,lineon)
      #Se agrega el token a la lista de tokens
      tokenList.append(token)
      #Se actualiza la posicion del codigo fuente
      index += len(value)
      continue #Se continua con el siguiente token

    #6. Identificar numeros enteros
    result=tp.INT_PAT.match(code,index)
    if result:
      #Se obtiene el valor del token
      value=result.group()
      #Se crea un objeto token
      token=tm.Token("INT",value,lineon)
      #Se agrega el token a la lista de tokens
      tokenList.append(token)
      #Se actualiza la posicion del codigo fuente
      index += len(value)
      continue #Se continua con el siguiente token

    #7. Identificar caracteres
    result=tp.CHAR_PAT.match(code,index)
    if result:
      #Se obtiene el valor del token
      value=result.group()
      #Se crea un objeto token
      token=tm.Token("CHAR",value,lineon)
      #Se agrega el token a la lista de tokens
      tokenList.append(token)
      #Se actualiza la posicion del codigo fuente
      index += len(value)
      continue #Se continua con el siguiente token

    #8. Identificar operadores o simbolos de dos caracteres
    if code[index:index+2] in tp.TOKEN_PATTERNS["TWO_CHAR"]:
      #Obtencion valor del token
      value=code[index:index+2]
      #Obtencion tipo del token
      type=tp.TOKEN_PATTERNS["TWO_CHAR"][value]
      #Creacion del objeto token
      token=tm.Token(type,value,lineon)
      #Agregar el token a la lista de tokens
      tokenList.append(token)
      #Actualizar la posicion del codigo fuente
      index += 2
      continue

    #9. Identificar operadores o simbolos de un caracter
    if code[index] in tp.TOKEN_PATTERNS["ONE_CHAR"]:
      #Obtencion valor del token
      value=code[index]
      #Obtencion tipo del token
      type=tp.TOKEN_PATTERNS["ONE_CHAR"][value]
      #Creacion del objeto token
      token=tm.Token(type,value,lineon)
      #Agregar el token a la lista de tokens
      tokenList.append(token)
      #Actualizar la posicion del codigo fuente
      index += 1
      continue

    #10. Si no se reconoce el token se muestra un error
    print(f'Error: Token no reconocido en la línea {lineon} -> "{code[index]}" (posición {index})')
    return []
  return tokenList
        
        
        

# Leer código desde el archivo program.gox
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
    

if __name__ == "__main__":
    try:
        code = read_file("program.gox")  # Leer el código del archivo
        tokens = tokenize(code)  # Ejecutar el analizador léxico
        for token in tokens:
            print(token)  # Imprimir cada token encontrado
    except FileNotFoundError:
        print("Error: El archivo 'program.gox' no fue encontrado.")
    
