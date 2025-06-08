import unittest
from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):
    
    def test_crear_paciente_exitoso(self):
        """Test de creación exitosa de paciente"""
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Matias Zarzur", str(paciente))
        self.assertIn("12345678", str(paciente))
        self.assertIn("17/07/1977", str(paciente))
    
    def test_obtener_dni(self):
        """Test de obtención del DNI"""
        paciente = Paciente("Juan Pérez", "87654321", "15/03/1985")
        self.assertEqual(paciente.obtener_dni(), "87654321")
    
    def test_representacion_string(self):
        """Test de representación en string del paciente"""
        paciente = Paciente("Ana García", "11223344", "20/12/1990")
        resultado = str(paciente)
        self.assertIn("Ana García", resultado)
        self.assertIn("11223344", resultado)
        self.assertIn("20/12/1990", resultado)
    
    def test_diferentes_pacientes(self):
        """Test con diferentes datos de pacientes"""
        paciente1 = Paciente("Carlos López", "99887766", "05/08/1980")
        paciente2 = Paciente("María Rodríguez", "55443322", "12/11/1995")
        
        self.assertEqual(paciente1.obtener_dni(), "99887766")
        self.assertEqual(paciente2.obtener_dni(), "55443322")
        self.assertNotEqual(str(paciente1), str(paciente2))

if __name__ == "__main__":
    unittest.main()
