 #validaciones
import re

def validarEmail(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    email_match = re.match(email_pattern,email)
    return bool(email_match)
            
            
def validarDNI(dni):
    dni_pattern = r"\d{8}[A-Z]$"
    dni_match = re.match(dni_pattern,dni)
    return bool(dni_match)

def validarPassword(contrasena):
    password_pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    password_match = re.match(password_pattern,contrasena)
    return bool(password_match)

def ValidarDate(fecha):
    date_pattner = r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"
    date_match = re.match(date_pattner,fecha)
    return bool(date_match)