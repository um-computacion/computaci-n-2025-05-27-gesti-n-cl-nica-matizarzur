import unittest
from src.models.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_crear_paciente(self):
        paciente = Paciente("Maria Elena Rodriguez", "45678912", "25/03/1985")
        self.assertEqual(paciente.obtener_dni(), "45678912")
        self.assertIn("Maria Elena Rodriguez", str(paciente))
        self.assertIn("45678912", str(paciente))
        self.assertIn("25/03/1985", str(paciente))
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Paciente("", "45678912", "25/03/1985")
    
    def test_dni_vacio(self):
        with self.assertRaises(ValueError):
            Paciente("Maria Elena Rodriguez", "", "25/03/1985")
    
    def test_fecha_vacia(self):
        with self.assertRaises(ValueError):
            Paciente("Maria Elena Rodriguez", "45678912", "")
    
    def test_dni_mal(self):
        with self.assertRaises(ValueError):
            Paciente("Maria Elena Rodriguez", "XYZ78912", "25/03/1985")
    
    def test_fecha_mala(self):
        with self.assertRaises(ValueError):
            Paciente("Maria Elena Rodriguez", "45678912", "1985/03/25")
    
    def test_fecha_inexistente(self):
        with self.assertRaises(ValueError):
            Paciente("Maria Elena Rodriguez", "45678912", "30/02/1985")
    
    def test_str(self):
        paciente = Paciente("Carlos Alberto Fernandez", "23456789", "12/11/1990")
        resultado = str(paciente)
        self.assertIn("Carlos Alberto Fernandez", resultado)
        self.assertIn("23456789", resultado)
        self.assertIn("12/11/1990", resultado)
    
    def test_dni_espacios(self):
        with self.assertRaises(ValueError):
            Paciente("Ana Maria Lopez", "456 789 12", "15/08/1992")
    
    def test_fecha_formato_malo(self):
        with self.assertRaises(ValueError):
            Paciente("Luis Miguel Torres", "34567891", "15-08-1992")


if __name__ == "__main__":
    unittest.main()