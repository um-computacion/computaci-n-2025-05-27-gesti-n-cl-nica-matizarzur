import unittest
from src.models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_crear_especialidad(self):
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles", "viernes"])
        self.assertEqual(especialidad.nombre, "Cardiología")
        self.assertEqual(len(especialidad.dias_atencion), 3)
        self.assertIn("lunes", especialidad.dias_atencion)
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes", "miercoles"])
    
    def test_dias_vacios(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", [])
    
    def test_dia_invalido(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", ["lunez", "miercoles"])
    
    def test_dia_duplicado(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", ["lunes", "lunes", "miercoles"])
    
    def test_atiende_dia(self):
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        self.assertTrue(especialidad.atiende_dia("lunes"))
        self.assertFalse(especialidad.atiende_dia("martes"))
    
    def test_str(self):
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        resultado = str(especialidad)
        self.assertIn("Cardiología", resultado)
        self.assertIn("lunes", resultado)
        self.assertIn("miercoles", resultado)

if __name__ == "__main__":
    unittest.main()