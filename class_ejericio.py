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
        return  max_chips


class Relleno():
    def __init__(self, flavor):
        self.flavor = flavor
    def flavor_description(self):
        pass

class FilledCookie(Cookie, Relleno):
    #GalletaRellena(Galleta, Relleno) que use ambos y sobrescriba mostrar_info().
    def fill_cookie_description(self):
        print(f"La galleta {self.type} está rellena de {self.flavor}")


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
        match ops:
            case "1":
                max_cokie = int(input("Cuántas galletas agregará?"))
                for cookie_x in range(max_cokie):
                    temp_type = input("Coloque el tipo de galleta: ")
                    temp_price = int(input("Coloque el precio de la galleta: "))
                    temp_peso = int(input("Coloque el peso de la galleta: "))
                    temp_galleta = Cookie(temp_type, temp_price, temp_peso)
                    cookie_jar.append(temp_galleta)
            case "2":
                max_cokie = int(input("Cuántas galletas con chispas agregará? "))
                for cookie_x in range(max_cokie):
                    temp_type = input("Coloque el tipo de galleta: ")
                    temp_price = int(input("Coloque el precio de la galleta: "))
                    temp_peso = int(input("Coloque el peso de la galleta: "))
                    temp_chips = int(input("Cuántas chispas tiene la galleta? "))
                    temp_galleta = Cookie_w_Chips(temp_type, temp_price, temp_peso, temp_chips)
                    cookie_jar.append(temp_galleta)
            case "3":
                max_cokie = int(input("Cuántas galletas rellenas agregará? "))
                for cookie_x in range(max_cokie):
                    temp_type = input("Coloque el tipo de galleta: ")
                    temp_price = int(input("Coloque el precio de la galleta: "))
                    temp_peso = int(input("Coloque el peso de la galleta: "))
                    temp_flavor = input("Coloque el sabor del relleno: ")
                    temp_galleta = FilledCookie(temp_type, temp_price, temp_peso, temp_flavor)
                    cookie_jar.append(temp_galleta)
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                key = False
    except ValueError:
        print("XDDD")
    except Exception as e:
        print("XDDD")
