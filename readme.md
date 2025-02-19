# Integrantes
- Camilo Eduardo Muñoz Albornoz
- Juan Camilo Mejia Henao

# Analizador Léxico para el Lenguaje GOX

Este proyecto es un analizador léxico que reconoce tokens para el lenguaje de programación inventado GOX. Los tokens son los elementos básicos que componen un lenguaje.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

### Archivos Principales

- `analizadorLexico.py`: Contiene la lógica principal del analizador léxico.
- `tokenModule.py`: Define la clase `Token` utilizada para representar los tokens.
- `tokenPatterns.py`: Define los patrones de expresiones regulares para los diferentes tipos de tokens.
- `testTokenizer.py`: Contiene pruebas unitarias para verificar el correcto funcionamiento del analizador léxico.
- `program.gox`: Archivo de ejemplo con código fuente en el lenguaje GOX.

### `analizadorLexico.py`: Explicación del código

El archivo `analizadorLexico.py` contiene la función `tokenize`, que es la encargada de analizar el código fuente en GOX y convertirlo en una lista de tokens.

#### **Funcionamiento de `tokenize`**

1. **Inicialización de variables**  
   - `tokenList`: Lista vacía donde se almacenarán los tokens encontrados.
   - `lineon`: Contador de la línea actual, usado para reportar errores y registrar la ubicación de los tokens.
   - `index`: Índice que recorre el código fuente.

2. **Recorrido del código fuente**  
   - Se usa un bucle `while` para procesar el código caracter por caracter hasta el final.

3. **Ignorar espacios en blanco y saltos de línea**  
   - Si se encuentra un espacio, tabulación o salto de línea, se ignora.
   - Si hay un salto de línea (`\n`), se incrementa el contador `lineon`.

4. **Manejo de comentarios**  
   - **Comentarios de bloque (`/* ... */`)**  
     - Se busca la posición de cierre `*/`.
     - Si no se encuentra, se muestra un error y se detiene el análisis.
     - Se cuentan los saltos de línea dentro del comentario y se actualiza `lineon`.
   - **Comentarios de línea (`// ...`)**  
     - Se busca el siguiente salto de línea `\n` y se ignora el texto intermedio.

5. **Identificación de tokens**  
   - Se usan expresiones regulares para detectar distintos tipos de tokens en orden de prioridad:
     1. **Identificadores y palabras clave**  
        - Se busca un nombre (`NAME_PAT`).
        - Si coincide con una palabra clave, se clasifica como tal; de lo contrario, es un identificador (`ID`).
     2. **Números flotantes** (`FLOAT_PAT`)
     3. **Números enteros** (`INT_PAT`)
     4. **Caracteres** (`CHAR_PAT`)
     5. **Símbolos de dos caracteres** (`TWO_CHAR`)
     6. **Símbolos de un solo carácter** (`ONE_CHAR`)

6. **Manejo de errores**  
   - Si un carácter no coincide con ninguna regla, se reporta un error indicando la línea y posición.

7. **Retorno de la lista de tokens**  
   - Al final, `tokenList` contiene todos los tokens detectados y se devuelve como resultado de la función.


## Problemas Encontrados y Soluciones

### Problema con Patrones de Expresiones Regulares para Números Científicos

Tuvimos problemas con el patrón de expresión regular para reconocer números en notación científica. La expresión regular original no reconocía correctamente algunos números en notación científica.

**Solución**: Ajustamos la expresión regular para números flotantes (`FLOAT_PAT`) en el archivo `tokenPatterns.py` para que reconozca correctamente los números en notación científica.

### Problema con Comentarios de Línea al Final del Texto

Otro problema que encontramos fue que los comentarios de línea (`//`) al final del texto causaban errores en el análisis léxico.

**Solución**: Ajustamos la lógica en la función `tokenize` en el archivo `analizadorLexico.py` para manejar correctamente los comentarios de línea al final del texto.

## Ejecución del Proyecto

Para ejecutar el analizador léxico, simplemente ejecute el archivo `analizadorLexico.py`:

```bash
python analizadorLexico.py
```

Para ejecutar las pruebas unitarias, ejecute el archivo `testTokenizer.py`:

```bash
python testTokenizer.py
```

## Resaltado de Sintaxis en Visual Studio Code

Para mejorar la experiencia de desarrollo, se creó una extensión de Visual Studio Code que permite el resaltado de sintaxis del lenguaje GOX.

### Creación de la Extensión

Se utilizó la librería `yo` para generar la estructura de la extensión:

```bash
npm install -g yo generator-code
```

Luego, se generó un nuevo proyecto con:

```bash
yo code
```

Esto creó la carpeta `gox-syntax`, que contiene los archivos clave para definir la sintaxis del lenguaje:

- `language-configuration.json`: Define reglas básicas del lenguaje, como caracteres de comentario y delimitadores.
- `syntaxes/gox.tmLanguage.json`: Especifica las reglas de resaltado de sintaxis mediante expresiones regulares.

### Instalación de la Extensión

Para instalar la extensión en Visual Studio Code, ejecute el siguiente comando:

```bash
code --install-extension gox-syntax-0.0.1.vsix
```

Una vez instalada, la sintaxis de GOX será resaltada automáticamente en los archivos con la extensión `.gox`.
