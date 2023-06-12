import unittest
from unittest.mock import Mock
from produto import Produto
from deleteProduct import DeleteProduct

class TestDeleteProduct(unittest.TestCase):
  def test_deletar_produto(self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    #adiciona produto_mock no objeto lista
    lista = DeleteProduct()
    lista.produtos.append(produto_mock)

    resultado = lista.deletar_produto(produto_mock)
    self.assertEqual(resultado, "Produto excluído")
  
  def test_deletar_produto_inexistente (self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    # cria uma lista vazia
    lista = DeleteProduct()

    resultado = lista.deletar_produto(produto_mock)
    self.assertEqual(resultado, "Produto não encontrado")


if __name__ == '__main__':
  unittest.main()
