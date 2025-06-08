import unittest
from src.models.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])
    
    def test_crear_especialidad_exitosa(self):
        """Test de creación exitosa de especialidad"""
        self.assertEqual(self.especialidad.obtener_especialidad(), "Cardiología")
    
    def test_verificar_dia_disponible(self):
        """Test de verificación de día disponible"""
        self.assertTrue(self.especialidad.verificar_dia("lunes"))
        self.assertTrue(self.especialidad.verificar_dia("miércoles"))
        self.assertTrue(self.especialidad.verificar_dia("viernes"))
        self.assertFalse(self.especialidad.verificar_dia("martes"))
        self.assertFalse(self.especialidad.verificar_dia("jueves"))
    
    def test_verificar_dia_case_insensitive(self):
        """Test de verificación de día sin importar mayúsculas/minúsculas"""
        self.assertTrue(self.especialidad.verificar_dia("LUNES"))
        self.assertTrue(self.especialidad.verificar_dia("Miércoles"))
        self.assertTrue(self.especialidad.verificar_dia("VIERNES"))
        self.assertFalse(self.especialidad.verificar_dia("MARTES"))
    
    def test_representacion_string(self):
        """Test de representación en string de la especialidad"""
        resultado = str(self.especialidad)
        self.assertIn("Cardiología", resultado)
        self.assertIn("lunes", resultado)
        self.assertIn("miércoles", resultado)
        self.assertIn("viernes", resultado)
    
    def test_especialidad_diferentes_dias(self):
        """Test con especialidad con diferentes días"""
        pediatria = Especialidad("Pediatría", ["martes", "jueves"])
        self.assertEqual(pediatria.obtener_especialidad(), "Pediatría")
        self.assertTrue(pediatria.verificar_dia("martes"))
        self.assertTrue(pediatria.verificar_dia("jueves"))
        self.assertFalse(pediatria.verificar_dia("lunes"))
    
    def test_especialidad_un_solo_dia(self):
        """Test con especialidad que atiende un solo día"""
        neurologia = Especialidad("Neurología", ["sábado"])
        self.assertTrue(neurologia.verificar_dia("sábado"))
        self.assertFalse(neurologia.verificar_dia("domingo"))

if __name__ == "__main__":
    unittest.main()