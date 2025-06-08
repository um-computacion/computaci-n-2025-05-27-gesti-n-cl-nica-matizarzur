import unittest
from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_crear_paciente(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Matias Zarzur", str(paciente))
        self.assertIn("12345678", str(paciente))
        self.assertIn("17/07/1977", str(paciente))
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "17/07/1977")
    
    def test_dni_vacio(self):
        with self.assertRaises(ValueError):
            Paciente("Matias Zarzur", "", "17/07/1977")
    
    def test_fecha_vacia(self):
        with self.assertRaises(ValueError):
            Paciente("Matias Zarzur", "12345678", "")
    
    def test_dni_mal(self):
        with self.assertRaises(ValueError):
            Paciente("Matias Zarzur", "ABC45678", "17/07/1977")
    
    def test_fecha_mala(self):
        with self.assertRaises(ValueError):
            Paciente("Matias Zarzur", "12345678", "1977/07/17")
    
    def test_fecha_inexistente(self):
        with self.assertRaises(ValueError):
            Paciente("Matias Zarzur", "12345678", "32/07/1977")
    
    def test_str(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        resultado = str(paciente)
        self.assertIn("Matias Zarzur", resultado)
        self.assertIn("12345678", resultado)
        self.assertIn("17/07/1977", resultado)
            
if __name__ == "__main__":
    unittest.main()