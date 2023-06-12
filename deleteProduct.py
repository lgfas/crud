class DeleteProduct():
    def __init__(self):
        self.produtos = []
    
    def deletar_produto(self,produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            return "Produto excluído"
        else:
          return "Produto não encontrado"