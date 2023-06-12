import unittest
from unittest.mock import Mock
from produto import Produto
from selectAllProducts import SelectAllProducts

class TestSelectProduct(unittest.TestCase):
  def test_selecionar_todos_produtos (self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    produto_mock1 = Mock(spec=Produto)
    produto_mock1.id = 2
    produto_mock1.nome = "Novo Produto"
    produto_mock1.descricao = "Descrição do novo produto"
    produto_mock1.valor = 19.99

    #adiciona produto_mock e produto_mock1 no objeto lista
    lista = SelectAllProducts()
    lista.produtos.append(produto_mock)
    lista.produtos.append(produto_mock1)

    resultado = lista.selecionar_todos_produtos()
    self.assertEqual(resultado, "Produto printado")
  
  def test_selecionar_todos_produtos_inexistentes (self):
    #Cria uma lista vazia
    lista = SelectAllProducts()
    
    resultado = lista.selecionar_todos_produtos()
    self.assertEqual(resultado, "Nenhum produto cadastrado")
    


if __name__ == '__main__':
  unittest.main()
