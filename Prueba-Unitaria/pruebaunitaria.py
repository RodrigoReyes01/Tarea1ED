from Funcion import Nota_estudiante
import unittest

class practica (unittest.TestCase):

    def Test_conseguir_nota(self):
        self.assertEqual(Nota_estudiante(75), "O")
        self.assertEqual(Nota_estudiante("Rodrigo Reyes"), False)
        self.assertEqual(Nota_estudiante(420), False)
        self.assertEqual(Nota_estudiante(-12), False)
