import unittest
from unittest.mock import Mock
from produto import Produto
from addProduct import AddProduct

class TestAddProduct(unittest.TestCase):
    def test_adicionar_produto(self):
        produto_mock = Mock(spec=Produto)
        produto_mock.id = 1
        produto_mock.nome = "Produto Teste"
        produto_mock.descricao = "Descrição do produto teste"
        produto_mock.valor = 10.99

        # cria objeto
        lista = AddProduct()

        # adicinar o Mock
        resultado = lista.adicionar_produto(produto_mock)

        # assert
        self.assertIn(produto_mock, lista.produtos)
        self.assertEqual(resultado, "Produto cadastrado")
        
        # mostrar na tela a lista
        lista.imprimir_lista()
    
    def test_adicionar_produto_informacoes_insuficientes (self):
        produto_mock = Mock(spec=Produto)
        produto_mock.id = 1
        produto_mock.nome = "" #Informacao insuficiente
        produto_mock.descricao = "Descrição do produto teste"
        produto_mock.valor = 10.99

        lista = AddProduct()

        resultado = lista.adicionar_produto(produto_mock)
        self.assertEqual(resultado, "Informações insuficientes") #Verifica se o produto nao foi adicionado por falta de informações

        lista.imprimir_lista()
    
    def test_adicionar_produto_ja_existente (self):
        produto_mock1 = Mock(spec=Produto)
        produto_mock1.id = 1
        produto_mock1.nome = "Produto Existente"
        produto_mock1.descricao = "Descrição do produto existente"
        produto_mock1.valor = 9.99

        produto_mock2 = Mock(spec=Produto)
        produto_mock2.id = 1  # Mesmo ID do produto_mock1
        produto_mock2.nome = "Novo Produto"
        produto_mock2.descricao = "Descrição do novo produto"
        produto_mock2.valor = 19.99

        lista = AddProduct()
        lista.adicionar_produto(produto_mock1)

        resultado = lista.adicionar_produto(produto_mock2)
        self.assertEqual(resultado, "Produto já cadastrado")  # Verifica se o produto não foi adicionado

        lista.imprimir_lista()

if __name__ == '__main__':
    unittest.main()
