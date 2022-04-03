from class_producto import Producto

class Pedido:

    __productos = []
    __pedidos = []

    def __init__(self, productos: str, cantidades: int):
        self.__productos = productos
        self.__pedidos = cantidades

    def total_pedido(self):
        total = 0

        for (producto, pedido) in zip(self.__productos, self.__pedidos):
            total += producto.calcular_total(pedido)

        return total

    def mostrar_produtos(self):
        for (producto, pedido) in zip(self.__productos, self.__pedidos):
            print("Producto: " + producto.nombre + ", Cantidad: " + str(pedido))

    @staticmethod
    def mostrar_total_pedido():
        p1 = Producto(1, "producto 1", 10)
        p2 = Producto(2, "producto 2", 1)
        p3 = Producto(3, "producto 3", 100)

        productos = [p1, p2, p3]
        cantidades = [10, 100, 1]

        pedido = Pedido(productos, cantidades)

        print("Total pedido: " + str(pedido.total_pedido()))
        pedido.mostrar_produtos()