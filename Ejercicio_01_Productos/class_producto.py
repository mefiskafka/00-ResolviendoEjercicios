class Producto:

    __codigo = 0
    __nombre = 0
    __precio = 0

    def __init__(self, codigo: int, nombre: int, precio: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, valor: int):
        self.__codigo = valor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, valor: str):
        self.__nombre = valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor: int):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.precio * unidades

    def __str__(self) -> str:
        return (
            "Codigo: "
            + str(self.codigo)
            + ", Nombre: "
            + self.nombre
            + ", Precio: "
            + str(self.precio)
        )
