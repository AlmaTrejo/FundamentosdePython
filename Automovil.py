class Automovil:
    def __init__(self,marca, color):
        #definir atributos de la clase 
        #son los que empiezan con self
        self.marca = marca
        self.color = color

    def avanzar (self):
        print(f"El coche avanza y es un:{self.marca}")

    def retroceder(self):
        print(f"El coche retrocede y es de color:{self.color}")
        #hasta aqui creamos una plantilla es decir la clase

if __name__ == "__main__":
    auto = Automovil("BMW","Azul")
    auto.avanzar()
    auto.retroceder()

    auto1 = Automovil("Honda","Gris")
    auto1.avanzar()
    auto1.retroceder()
