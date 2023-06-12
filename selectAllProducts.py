class SelectAllProducts():
    def __init__(self):
        self.produtos = []
    
    def selecionar_todos_produtos(self):
      if len(self.produtos) == 0:
        return "Nenhum produto cadastrado"

      for produto in self.produtos:
        print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Valor: {produto.valor}")
      return "Produto printado"
    
    
        