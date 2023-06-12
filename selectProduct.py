class SelectProduct():
    def __init__(self):
        self.produtos = []
    
    def selecionar_produto(self,produto):
        if produto in self.produtos:
          print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Valor: {produto.valor}")
        else:
            return "Produto não foi encontrado"
        