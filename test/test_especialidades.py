import unittest
from src.models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_crear_especialidad(self):
        especialidad = Especialidad("Dermatologia", ["lunes", "miercoles", "viernes"])
        self.assertEqual(especialidad.obtener_especialidad(), "Dermatologia")
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("MIERCOLES"))
        self.assertFalse(especialidad.verificar_dia("martes"))
    
    def test_dias_invalidos(self):
        with self.assertRaises(ValueError):
            Especialidad("Traumatologia", ["lunez", "martes"])
    
    def test_dia_vacio(self):
        with self.assertRaises(ValueError):
            Especialidad("Ginecologia", [])
    
    def test_especialidad_vacia(self):
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes", "martes"])
    
    def test_dia_case_insensitive(self):
        especialidad = Especialidad("Urologia", ["martes", "jueves"])
        self.assertTrue(especialidad.verificar_dia("martes"))
        self.assertTrue(especialidad.verificar_dia("MARTES"))
        self.assertTrue(especialidad.verificar_dia("Martes"))
        self.assertTrue(especialidad.verificar_dia("mArTeS"))
    
    def test_especialidad_acentos(self):
        especialidad = Especialidad("Oncologia", ["lunes", "miercoles", "viernes"])
        self.assertEqual(especialidad.obtener_especialidad(), "Oncologia")
        self.assertTrue(especialidad.verificar_dia("miercoles"))
        self.assertIn("Oncologia", str(especialidad))
    
    def test_normalizacion_dias_entrada(self):
        especialidad1 = Especialidad("Psiquiatria", ["miercoles", "sabado"])
        especialidad2 = Especialidad("Radiologia", ["miercoles", "sabado"])
        
        self.assertTrue(especialidad1.verificar_dia("miercoles"))
        self.assertTrue(especialidad2.verificar_dia("miercoles"))
        self.assertTrue(especialidad1.verificar_dia("miercoles"))
        self.assertTrue(especialidad2.verificar_dia("miercoles"))
    
    def test_str(self):
        especialidad = Especialidad("Endocrinologia", ["lunes", "miercoles"])
        resultado = str(especialidad)
        self.assertIn("Endocrinologia", resultado)
        self.assertIn("lunes", resultado)
        self.assertIn("miercoles", resultado)
    
    def test_dias_duplicados(self):
        with self.assertRaises(ValueError):
            Especialidad("Gastroenterologia", ["lunes", "lunes", "martes"])
    
    def test_dia_inexistente(self):
        with self.assertRaises(ValueError):
            Especialidad("Reumatologia", ["lunes", "noexiste"])

if __name__ == "__main__":
    unittest.main()