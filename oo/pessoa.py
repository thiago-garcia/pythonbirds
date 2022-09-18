class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=26):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
    
    @staticmethod
    def metodo_estatico():
        return 18
    
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    thiago = Pessoa(nome='Thiago')
    luiz = Pessoa(thiago, nome='Luiz')
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(luiz.idade)
    for filho in luiz.filhos:
        print(filho.nome)
    luiz.sobrenome = 'Paula'
    del luiz.filhos
    luiz.olhos = 1
    del luiz.olhos
    print(luiz.__dict__)
    print(thiago.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(thiago.olhos)
    print(id(Pessoa.olhos), id(luiz.olhos), id(thiago.olhos))
    print(Pessoa.metodo_estatico(), luiz.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luiz.nome_e_atributos_de_classe())
    