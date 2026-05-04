import unittest
from classes import Produto, Cliente, Sistema, Venda

class testSistemaVendas(unittest.TestCase):
    
    def test_estoque_final(self):
        sistema = Sistema()
        p1 = Cliente(1010, "Joao")
        prod1 = Produto("Coca-cola", 10, 5.0)
        
        venda = Venda(p1, prod1, 2)
        venda.processar_venda(sistema)
    
    
        self.assertEqual(prod1.qtd, 8)
    

if __name__ == '__main__':
     unittest.main()

   