import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd()))
from store import Store
from instrument import *


class InstrumentTests(unittest.TestCase):
    def test_creating_classes(self):
        """Testando se os instrumentos estão sendo criados corretamente
        """
        guitarra = Guitarra('x', 'y', 2000, 12)
        baixo = Baixo('a', 'b', 3000, 4)
        violao = Violao('c', 'd', 1500, 6)
        self.assertIsInstance(guitarra, Guitarra)
        self.assertIsInstance(baixo, Baixo)
        self.assertIsInstance(violao, Violao)
