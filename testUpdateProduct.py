import unittest
from unittest.mock import Mock
from produto import Produto
from updateProduct import UpdateProduct

class TestUpdateProduct(unittest.TestCase):
  def test_atualizar_produto (self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    #adiciona produto_mock no objeto lista
    lista = UpdateProduct()
    lista.produtos.append(produto_mock)

    produto_mock1 = Mock(spec=Produto)
    produto_mock1.id = 1
    produto_mock1.nome = "Novo Produto"
    produto_mock1.descricao = "Descrição do novo produto"
    produto_mock1.valor = 19.99

    resultado = lista.atualizar_produto(produto_mock1)
    self.assertEqual(resultado, "Produto atualizado")
    self.assertEqual(produto_mock1.nome, "Novo Produto")
    self.assertEqual(produto_mock1.descricao, "Descrição do novo produto")
    self.assertEqual(produto_mock1.valor, 19.99)

  def test_atualizar_produto_informacoes_insuficientes (self):
    produto_mock = Mock(spec=Produto)
    produto_mock.id = 1
    produto_mock.nome = "Produto Teste"
    produto_mock.descricao = "Descrição do produto teste"
    produto_mock.valor = 10.99

    #adiciona produto_mock no objeto lista
    lista = UpdateProduct()
    lista.produtos.append(produto_mock)

    produto_mock1 = Mock(spec=Produto)
    produto_mock1.id = 1
    produto_mock1.nome = "" #Informações faltando
    produto_mock1.descricao = "Descrição do novo produto"
    produto_mock1.valor = 19.99

    resultado = lista.atualizar_produto(produto_mock1)
    self.assertEqual(resultado, "Informações insuficientes")



if __name__ == '__main__':
  unittest.main()
