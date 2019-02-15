class Producto():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
class Medicamento(Producto):
    def __init__(self,nombre, cantidad, precio, composicion, porcentaje):
        super().__init__(nombre, cantidad, precio)
        self.composicion = composicion
        self.porcentaje = porcentaje
class Laboratorio():
    def __init__(self, laboratorio, Producto, Producto2):
        self.laboratorio = laboratorio
        self.producto = Producto
        self.producto2 = Producto2

pañales = Producto("pañales",2, 4)

ibuprofeno = Medicamento("ibuprofeno", 6, 3, "Acido", 0.3)

bayer = Laboratorio("Bayer", ibuprofeno, pañales)

print(bayer.producto.nombre)
print(bayer.producto2.nombre)
print("El laboratorio", bayer.laboratorio, "tiene", bayer.producto.nombre ,", ", bayer.producto2.nombre)
print("la composición de", bayer.producto.nombre,"es", bayer.producto.composicion)
