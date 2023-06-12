class UpdateProduct():
    def __init__(self):
        self.produtos = []
    
    def atualizar_produto(self,produto):
        for i in self.produtos:
            if i.id == produto.id:
              if produto.id and produto.nome and produto.descricao and produto.valor:
                i.nome = produto.nome
                i.descricao = produto.descricao
                i.valor = produto.valor
                return "Produto atualizado"
              else:
                 return "Informações insuficientes"