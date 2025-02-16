# Integrantes
- Camilo Eduardo Muñoz Albornoz
- 

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

## Problemas Encontrados y Soluciones

### Problema con Patrones de Expresiones Regulares para Números Científicos

Tuvimos problemas con el patrón de expresión regular para reconocer números en notación científica. La expresión regular original no reconocía correctamente algunos números en notación científica.

**Solución**: Ajustamos la expresión regular para números flotantes (`FLOAT_PAT`) en el archivo `tokenPatterns.py` para que reconozca correctamente los números en notación científica.

### Problema con Comentarios de Línea al Final del Texto

Otro problema que encontramos fue que los comentarios de línea (`//`) al final del texto causaban errores en el análisis léxico.

**Solución**: Ajustamos la lógica en la función `tokenize` en el archivo `analizadorLexico.py` para manejar correctamente los comentarios de línea al final del texto.

## Integrantes del Grupo

## Ejecución del Proyecto

Para ejecutar el analizador léxico, simplemente ejecute el archivo `analizadorLexico.py`:

python analizadorLexico.py

Para ejecutar las pruebas unitarias, ejecute el archivo `testTokenizer.py`:

python testTokenizer.py