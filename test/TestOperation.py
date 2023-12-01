import unittest
from models.Operation import Operation

class TestOperation(unittest.TestCase):
    def setUp(self):
        # Configurar una instancia de la clase Deposito con un saldo inicial de 1000 para cada prueba
        self.mi_deposito = Operation(saldo_inicial=50000000000)

    def test_depositar(self):
        self.mi_deposito.pay(500)
        self.assertEqual(self.mi_deposito.obtener_saldo(), 1500)

    def test_retirar(self):
        self.mi_deposito.pay(200)
        self.assertEqual(self.mi_deposito.obtener_saldo(), 800)

    def test_pagar_cantidad_invalida(self):
        mensaje_esperado = "Error: La cantidad a depositar debe ser mayor que cero."
        with self.assertRaisesRegex(ValueError, mensaje_esperado):
            self.mi_deposito.pay(0)

    def test_obtener_saldo(self):
        saldo_actual = self.mi_deposito.history()
        self.assertEqual(saldo_actual, 1000)

if __name__ == "__main__":
    unittest.main()
