from unittest import TestCase

from oo.carro import Direcao, Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.acelerar() 
        motor.frear()
        self.assertEqual(0, motor.velocidade)
    
    def teste_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)
    
    def teste_virar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_direita()
        self.assertEqual('Norte', direcao.valor)
    
    def teste_virar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_a_esquerda()
        self.assertEqual('Norte', direcao.valor)