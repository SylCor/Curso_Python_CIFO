# Expresiones regulares - Regular Expressions
import re

# patrones para validar textos comunes como emails, passwords, dni...
email = "armand@gmail.com"

# explicación de patrón
# r: raw string: cadena sin interpretar, para evitar problemas con caracteres de escape
# ^: inicio cadena
# [a-zA-Z0-9_.+-]: uno o más caracteres alfanuméricos, punto, guión bajo, símbolo mas o guión
# @: arroba
# [a-zA-Z0-9-]: Lo mismo que lo anterior
# \.: punto
# [a-zA-Z0-9-.]: Lo mismo que lo anterior
# $: fin de cadena

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email_match = re.match(email_pattern,email)


# DNI
dni = "12345678A"
dni_pattern = r"\d{8}[A-Z]$"
#\d{8}: 8 dígitos
# [A-Z]: una letra mayúscula

