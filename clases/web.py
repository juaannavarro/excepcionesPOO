import re

class EntradaIncorrecta(BaseException):pass
class DireccionCorrecta(BaseException):pass
class CuentaBloqueada(BaseException):pass


class web:
    def __init__(self, correo):
        self.correo = correo

    def acceso(x):
        x = input("Introduce un correo para entrar: ")
        print(x)
        if x is None or x == "":
            print("Introduce un correo electrónico")
            raise EntradaIncorrecta
        
        elif re.search(".*@.*\..*", x) is None:
            print("El correo debe de escribirse así: xxx@xx.xx")
            raise DireccionCorrecta

        elif x == "xxx@xx.xx":
            print("Cuenta bloqueada por acceso fallido ")
            raise CuentaBloqueada
        else:
            print("Bienvenido, has entrado en la web")
            return
print(web.acceso("x"))