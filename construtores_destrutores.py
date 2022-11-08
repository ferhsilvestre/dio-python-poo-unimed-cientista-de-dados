class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Incializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância da classe..")

    def falar(self):
        print("Auauau")

def criar_cachorro():
    c1 = Cachorro("Zeus", "Branco e preto", False)        
    print(c1.nome)

c = Cachorro("Chappie", "Amarelo")
c.falar()

print("Olá mundo!")

del c

print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")

# criar_cachorro()
