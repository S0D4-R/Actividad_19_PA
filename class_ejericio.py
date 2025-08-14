class Cookie:
    def __init__(self, type, price, weight):
        self.type = type
        self.price = price
        self.weight = weight
    def display_info(self):
        print(f"La galleta es de tipo {self.type}|Peso: {self.weight}|Precio: {self.price}")

#Galleta Chispas
class Cookie_w_Chips(Cookie):
    pass
class Relleno():
    def __init__(self, flavor):
        self.flavor = flavor

class FilledCookie(Cookie, Relleno):
    pass

key = True
while key:
    try:
        ops = input("Menú con opciones:
Registrar galleta básica
Registrar galleta con chispas
Registrar galleta rellena
Listar galletas
Buscar por nombre
Eliminar por nombre
Salir")
    except Exception as e:
        print("XDDD")