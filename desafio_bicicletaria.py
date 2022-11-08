class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    def buzinar(self):
        print("Plim Plim....")
    
    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummmmm....")

    def get_cor(self):
        return self.cor

    # def __str__(self):
    #     return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "monark", 2000, 189)
b2.buzinar()  # Bicicleta.buzinar(b2)
print(b2.get_cor())
print(b2)