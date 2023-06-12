
class AddProduct:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        for i in self.produtos:
            if i.id == produto.id:
                return "Produto já cadastrado"

        if produto.id and produto.nome and produto.descricao and produto.valor:
            # Cria uma instância do modelo Produto e adiciona-a à sessão
            produto_db = Produto(id=produto.id, nome=produto.nome, descricao=produto.descricao, valor=produto.valor)
            session.add(produto_db)
            session.commit()

            self.produtos.append(produto)
            return "Produto cadastrado"
        else:
            return "Informações insuficientes"

    def imprimir_lista(self):
        for produto in self.produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Valor: {produto.valor}")


class UpdateProduct:
    def __init__(self):
        self.produtos = []

    def atualizar_produto(self, produto):
        for i in self.produtos:
            if i.id == produto.id:
                if produto.id and produto.nome and produto.descricao and produto.valor:
                    i.nome = produto.nome
                    i.descricao = produto.descricao
                    i.valor = produto.valor
                    return "Produto atualizado"
                else:
                    return "Informações insuficientes"


class SelectProduct:
    def __init__(self):
        self.produtos = []

    def selecionar_produto(self, produto):
        if produto in self.produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Valor: {produto.valor}")
        else:
            return "Produto não foi encontrado"


class SelectAllProducts:
    def __init__(self):
        self.produtos = []

    def selecionar_todos_produtos(self):
        if len(self.produtos) == 0:
            return "Nenhum produto cadastrado"

        for produto in self.produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Valor: {produto.valor}")
        return "Produtos impressos"


class DeleteProduct:
    def __init__(self):
        self.produtos = []

    def deletar_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            return "Produto excluído"
        else:
            return "Produto não encontrado"
