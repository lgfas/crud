class AddProduct:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        for i in self.produtos:
            if i.id == produto.id:
                return "Produto já cadastrado"

        if produto.id and produto.nome and produto.descricao and produto.valor:
            self.produtos.append(produto)
            return "Produto cadastrado"
        else:
            return "Informações insuficientes"

    def imprimir_lista(self):
        for produto in self.produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Valor: {produto.valor}")