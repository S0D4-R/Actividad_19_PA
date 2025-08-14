class Cookie:
    def __init__(self, type, price, weight):
        self.type = type
        self.price = price
        self.weight = weight
    def display_info(self):
        print(f"La galleta es de tipo {self.type}|Peso: {self.weight}|Precio: {self.price}", end="|")

#Galleta Chispas
class Cookie_w_Chips(Cookie):
    def chip_creation(self):
        #entero ≥ 0
        max_chips = int(input("Cuántas chispas quiere agregar?"))
        print(f"Chispas: {max_chips}")


class Relleno():
    def __init__(self, flavor):
        self.flavor = flavor
    def flavor_description(self):
        pass

class FilledCookie(Cookie, Relleno):
    #GalletaRellena(Galleta, Relleno) que use ambos y sobrescriba mostrar_info().
    pass


cookie_jar = []
key = True
while key:
    try:
        ops = input("-------------Menu------------\n\n"
                    "\n1. Registrar galleta básica"
                    "\n2. Registrar galleta con chispas"
                    "\n3. Registrar galleta rellena"
                    "\n4. Listar galletas"
                    "\n5. Buscar por nombre"
                    "\n6. Eliminar por nombre"
                    "\n7. Salir"
                    "\nOpcion: ")
    except ValueError:
        print("XDDD")
    except Exception as e:
        print("XDDD")
