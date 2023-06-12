import unittest
from unittest.mock import Mock
from produto import Produto
from selectProduct import SelectProduct

class TestSelectProduct(unittest.TestCase):
  def test_selecionar_produto (self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    #adiciona produto_mock no objeto lista
    lista = SelectProduct()
    lista.produtos.append(produto_mock)

    resultado = lista.selecionar_produto(produto_mock)
    self.assertEqual(produto_mock.id, 1)
    self.assertEqual(produto_mock.nome, "Produto Teste")
    self.assertEqual(produto_mock.descricao, "Descrição do produto teste")
    self.assertEqual(produto_mock.valor, 10.99)

  def test_selecionar_produto_inexistente (self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    #adiciona produto_mock no objeto lista
    lista = SelectProduct()
    lista.produtos.append(produto_mock)

    produto_mock1 = Mock(spec=Produto)
    produto_mock1.id = 1
    produto_mock1.nome = "Novo Produto"
    produto_mock1.descricao = "Descrição do novo produto"
    produto_mock1.valor = 19.99

    resultado = lista.selecionar_produto(produto_mock1)
    self.assertEqual(resultado, "Produto não foi encontrado")
    


if __name__ == '__main__':
  unittest.main()
