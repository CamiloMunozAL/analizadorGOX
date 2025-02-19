#Modulo para los patrones de los tokens y las expresiones regulares

import re

# Definicion de los tokens
TOKEN_PATTERNS = {
    "TWO_CHAR": {
        "<=": "LESS_EQUAL",
        ">=": "GREATER_EQUAL",
        "==": "EQUAL_EQUAL",
        "!=": "NOT_EQUAL",
        "&&": "AND",
        "||": "OR"
    },
    "ONE_CHAR": {
        "+": "PLUS",
        "-": "MINUS",
        "*": "STAR",
        "/": "SLASH",
        "=": "EQUAL",
        ";": "SEMICOLON",
        "(": "LEFT_PAREN",
        ")": "RIGHT_PAREN",
        "{": "LEFT_BRACE",
        "}": "RIGHT_BRACE",
        ",": "COMMA",
        "<": "LESS",
        ">": "GREATER",
        "!": "NOT",
        "&": "AMPERSAND",
        "|": "PIPE",
        "%": "MOD",
        "\"": "QUOTE",
        "'": "APOSTROPHE",
        ":": "COLLON"
    },
    "KEYWORDS": {
        "var": "VAR",
        "const": "CONST",
        "func": "FUNC",
        "if": "IF",
        "else": "ELSE",
        "while": "WHILE",
        "break": "BREAK",
        "continue": "CONTINUE",
        "return": "RETURN",
        "print": "PRINT",
        "import": "IMPORT",
        "true": "TRUE",
        "false": "FALSE",
        "int": "TYPE_INT",
        "float": "TYPE_FLOAT",
        "char": "TYPE_CHAR",
        "bool": "TYPE_BOOL",
    }
}

# Construccion de la expresion regular combinada

#NAME_PAT reconoce nombres de variables
NAME_PAT = re.compile(r"[a-zA-Z_]\w*")
#FLOAT_PAT reconoce numeros flotantes
FLOAT_PAT = re.compile(r"\d*\.\d+|\d+\.\d*|(\d+([eE][-+]?\d+))")
#INT_PAT reconoce numeros enteros
INT_PAT = re.compile(r"\d+")
#CHAR_PAT reconoce caracteres
CHAR_PAT = re.compile(r"'(\\.|[^'])'")

