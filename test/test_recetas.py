import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.receta import Receta

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Camila Rodriguez", "11223344", "15/09/1992")
        self.medico = Medico("Dr. Matias Fernandez", "MAT88888")
        self.medicamentos = ["Amoxicilina 875mg", "Loratadina 10mg"]
    
    def test_crear_receta(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        resultado = str(receta)
        
        self.assertIn("Camila Rodriguez", resultado)
        self.assertIn("Dr. Matias Fernandez", resultado)
        self.assertIn("Amoxicilina 875mg", resultado)
        self.assertIn("Loratadina 10mg", resultado)
        
        self.assertIsInstance(receta._Receta__fecha, datetime)
    
    def test_error_sin_medicamentos(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])
    
    def test_error_medicamentos_none(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, None)
    
    def test_error_paciente_none(self):
        with self.assertRaises(ValueError):
            Receta(None, self.medico, self.medicamentos)
    
    def test_error_medico_none(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, None, self.medicamentos)
    
    def test_str_contenido_completo(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        resultado = str(receta)
        
        self.assertIn("Receta", resultado)
        self.assertIn("Camila Rodriguez", resultado)
        self.assertIn("Dr. Matias Fernandez", resultado)
        self.assertIn("Amoxicilina 875mg", resultado)
    
    def test_medicamento_unico(self):
        medicamentos_uno = ["Aspirina 100mg"]
        receta = Receta(self.paciente, self.medico, medicamentos_uno)
        resultado = str(receta)
        
        self.assertIn("Aspirina 100mg", resultado)
        self.assertIn("Camila Rodriguez", resultado)
    
    def test_fecha_automatica(self):
        antes = datetime.now()
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        despues = datetime.now()
        
        fecha_receta = receta._Receta__fecha
        self.assertGreaterEqual(fecha_receta, antes)
        self.assertLessEqual(fecha_receta, despues)

if __name__ == "__main__":
    unittest.main()