import re

class EntradaIncorrecta(BaseException): pass
class EmailMalFormateado(BaseException): pass
class CiberAtaque(BaseException): pass

def validacion_email(cadena):
    if cadena is None or cadena == "":
        raise EntradaIncorrecta
    if re.search(".*@.*\..*", cadena) is None:
        raise EmailMalFormateado
    if cadena != "vincent@eni.fr":
        raise CiberAtaque

ataque = False
while not ataque:
    try:
        cadena = input('--> ')
        validacion_email(cadena)
        break
    except EntradaIncorrecta:
        print("'{}' es una entrada incorrecta. Introduzca una dirección de correo electrónico".format(cadena))
    except EmailMalFormateado:
        print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
    except CiberAtaque:
        print("Cuenta bloqueada debido a un ataque")
        ataque = True
if not ataque:
    print("Bienvenido Vincente")
