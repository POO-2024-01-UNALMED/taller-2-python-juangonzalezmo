class Asiento:
    def __init__(self, color, precio, registro):

        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):

        if color=="rojo" or color=="verde"or color=="amarillo"or color=="negro" or color=="blanco":

            self.color= color

class Auto:

    cantidadCreados= 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados ):
        
        self.modelo= modelo
        self.precio= precio
        self.asientos= asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados= cantidadCreados

    def cantidadAsientos(self):
        x=0
        for i in self.asientos:

            if type(i)==Asiento:
                x+=1
        return x

    def verificarIntegridad(self):

        veracidad= False
        for y in self.asientos:
            if type(y)==Asiento:
                if self.registro==y.registro and self.registro==self.motor.registro:
                    veracidad= True
                else:
                    veracidad = False
                    break
        if veracidad== True:

            return "Auto original"
        
        else:

            return "Las piezas no son originales"

class Motor:
    
    def __init__(self, numeroCilindros, tipo, registro):

        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro= registro

    def cambiarRegistro(self,registro):
        
        self.registro= registro

    def asignarTipo(self, tipo):

        if tipo=="electrico" or tipo=="gasolina":

            self.tipo = tipo

