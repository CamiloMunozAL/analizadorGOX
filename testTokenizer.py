"""
Pruebas unitarias para el analizador léxico

"""

# Importar el módulo unittest sirve para realizar pruebas unitarias
import unittest

# Importar la función tokenize del módulo analizadorLexico
from analizadorLexico import tokenize

# Clase TestTokenizer que hereda de unittest.TestCase

class TestTokenizer(unittest.TestCase):

  # Metodo test para probar el  de floats
  def test_float(self):
    # Código de prueba
    code = "3.4425 .123 1234. 13e-02 13E-03"
    # Se llama a la función tokenize con el código de prueba
    tokens = tokenize(code)#Lista de tokens
    #Pasar a tuplas
    tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]
    # Tokens esperados
    expected = [
      ("FLOAT", "3.4425", 1),
      ("FLOAT", ".123", 1),
      ("FLOAT", "1234.", 1),
      ("FLOAT", "13e-02", 1),
      ("FLOAT", "13E-03", 1)
    ]
    # Se comparan los tokens esperados con los tokens obtenidos
    self.assertEqual(tokensTuples, expected)

  # Metodo test para probar el funcionamiento de enteros
  def test_int(self):
    # Código de prueba
    code = "123 6 7 897786441 477"
    # Se llama a la función tokenize con el código de prueba
    tokens = tokenize(code)#Lista de tokens
    #Pasar a tuplas
    tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]
    # Tokens esperados
    expected = [
      ("INT", "123", 1),
      ("INT", "6", 1),
      ("INT", "7", 1),
      ("INT", "897786441", 1),
      ("INT", "477", 1)
    ]
    # Se comparan los tokens esperados con los tokens obtenidos
    self.assertEqual(tokensTuples, expected)

  # Metodo test para probar el reconocimiento de caracteres
  def test_char(self):
    # Código de prueba
    code = "'a' 'b' 'c' 'D'"
    # Se llama a la función tokenize con el código de prueba
    tokens = tokenize(code)#Lista de tokens
    #Pasar a tuplas
    tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]
    # Tokens esperados
    expected = [
      ("CHAR", "'a'", 1),
      ("CHAR", "'b'", 1),
      ("CHAR", "'c'", 1),
      ("CHAR", "'D'", 1)
    ]
    # Se comparan los tokens esperados con los tokens obtenidos
    self.assertEqual(tokensTuples, expected)

  def test_identifiers(self):
    # Código de prueba
    code =  "variable1 variable2 variable3"
    # Se llama a la función tokenize con el código de prueba
    tokens = tokenize(code)
    #Pasar a tuplas
    tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]

    # Tokens esperados
    expected = [
      ("ID", "variable1", 1),
      ("ID", "variable2", 1),
      ("ID", "variable3", 1)
    ]
    # Se comparan los tokens esperados con los tokens obtenidos
    self.assertEqual(tokensTuples, expected)

  def test_keywords(self):
    # Código de prueba
    code = "var const func if else while break continue return print import true false int float char bool"
    # Se llama a la función tokenize con el código de prueba
    tokens = tokenize(code)
    #Pasar a tuplas
    tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]

    # Tokens esperados
    expected = [
      ("VAR", "var", 1),
      ("CONST", "const", 1),
      ("FUNC", "func", 1),
      ("IF", "if", 1),
      ("ELSE", "else", 1),
      ("WHILE", "while", 1),
      ("BREAK", "break", 1),
      ("CONTINUE", "continue", 1),
      ("RETURN", "return", 1),
      ("PRINT", "print", 1),
      ("IMPORT", "import", 1),
      ("TRUE", "true", 1),
      ("FALSE", "false", 1),
      ("TYPE_INT", "int", 1),
      ("TYPE_FLOAT", "float", 1),
      ("TYPE_CHAR", "char", 1),
      ("TYPE_BOOL", "bool", 1)
    ]
    # Se comparan los tokens esperados con los tokens obtenidos
    self.assertEqual(tokensTuples, expected)


    def test_two_char(self):
      # Código de prueba
      code = "<= >= == != && ||"
      # Se llama a la función tokenize con el código de prueba
      tokens = tokenize(code)
      #Pasar a tuplas
      tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]

      # Tokens esperados
      expected = [
        ("LESS_EQUAL", "<=", 1),
        ("GREATER_EQUAL", ">=", 1),
        ("EQUAL_EQUAL", "==", 1),
        ("NOT_EQUAL", "!=", 1),
        ("AND", "&&", 1),
        ("OR", "||", 1)
      ]
      # Se comparan los tokens esperados con los tokens obtenidos
      self.assertEqual(tokensTuples, expected)

    def test_one_char(self):
      # Código de prueba
      code = "+ - * / = ; ( ) { } ,"
      # Se llama a la función tokenize con el código de prueba
      tokens = tokenize(code)
      #Pasar a tuplas
      tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]

      # Tokens esperados
      expected = [
        ("PLUS", "+", 1),
        ("MINUS", "-", 1),
        ("STAR", "*", 1),
        ("SLASH", "/", 1),
        ("EQUAL", "=", 1),
        ("SEMICOLON", ";", 1),
        ("LEFT_PAREN", "(", 1),
        ("RIGHT_PAREN", ")", 1),
        ("LEFT_BRACE", "{", 1),
        ("RIGHT_BRACE", "}", 1),
        ("COMMA", ",", 1)
      ]
      # Se comparan los tokens esperados con los tokens obtenidos
      self.assertEqual(tokensTuples, expected)

    def test_comments(self):
      # Código de prueba
      code = """
      // Comentario de una línea
      /* Comentario de varias líneas
      */
      """
      # Se llama a la función tokenize con el código de prueba
      tokens = tokenize(code)
      #Pasar a tuplas
      tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]

      # Tokens esperados
      expected = []
      # Se comparan los tokens esperados con los tokens obtenidos
      self.assertEqual(tokensTuples, expected)

    def test_errors(self):
      # Código de prueba
      code = "@@"
      # Se llama a la función tokenize con el código de prueba
      tokens = tokenize(code)
      #Pasar a tuplas
      tokensTuples = [(token.type, token.value, token.lineon) for token in tokens]

      # Tokens esperados
      expected = []
      # Se comparan los tokens esperados con los tokens obtenidos
      self.assertEqual(tokensTuples, expected)

if __name__ == '__main__':
    unittest.main()
