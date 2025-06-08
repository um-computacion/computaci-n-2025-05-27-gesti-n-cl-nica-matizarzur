import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.medico = Medico("Dr. Juan Pérez", "12345")
        self.cardiologia = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])
        self.pediatria = Especialidad("Pediatría", ["martes", "jueves"])
    
    def test_crear_medico_exitoso(self):
        """Test de creación exitosa de médico"""
        self.assertEqual(self.medico.obtener_matricula(), "12345")
        self.assertIn("Dr. Juan Pérez", str(self.medico))
        self.assertIn("12345", str(self.medico))
    
    def test_agregar_especialidad(self):
        """Test de agregar especialidad a médico"""
        self.medico.agregar_especialidad(self.cardiologia)

        self.assertIn("Cardiología", str(self.medico))
    
    def test_obtener_especialidad_para_dia_disponible(self):
        """Test de obtener especialidad para día disponible"""
        self.medico.agregar_especialidad(self.cardiologia)
        especialidad = self.medico.obtener_especialidad_para_dia("lunes")
        self.assertEqual(especialidad, "Cardiología")
    
    def test_obtener_especialidad_para_dia_no_disponible(self):
        """Test de obtener especialidad para día no disponible"""
        self.medico.agregar_especialidad(self.cardiologia)
        especialidad = self.medico.obtener_especialidad_para_dia("martes")
        self.assertIsNone(especialidad)
    
    def test_agregar_multiple_especialidades(self):
        """Test de agregar múltiples especialidades"""
        self.medico.agregar_especialidad(self.cardiologia)
        self.medico.agregar_especialidad(self.pediatria)
        

        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertEqual(self.medico.obtener_especialidad_para_dia("martes"), "Pediatría")
    
    def test_obtener_matricula(self):
        """Test de obtención de matrícula"""
        medico2 = Medico("Dra. Ana García", "67890")
        self.assertEqual(medico2.obtener_matricula(), "67890")
    
    def test_representacion_string(self):
        """Test de representación en string del médico"""
        self.medico.agregar_especialidad(self.cardiologia)
        resultado = str(self.medico)
        self.assertIn("Dr. Juan Pérez", resultado)
        self.assertIn("12345", resultado)
        self.assertIn("Cardiología", resultado)
    
    def test_medico_sin_especialidades(self):
        """Test de médico sin especialidades"""
        medico_nuevo = Medico("Dr. Carlos López", "11111")
        self.assertIsNone(medico_nuevo.obtener_especialidad_para_dia("lunes"))
        # El string representation debería funcionar aunque no tenga especialidades
        self.assertIn("Dr. Carlos López", str(medico_nuevo))

if __name__ == "__main__":
    unittest.main()