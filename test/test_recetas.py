import unittest
from datetime import datetime
from src.models.receta import Receta
from src.models.paciente import Paciente
from src.models.medico import Medico

class TestReceta(unittest.TestCase):
    def test_crear_receta(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        medicamentos = ["Paracetamol 500mg", "Ibuprofeno 400mg"]
        
        receta = Receta(paciente, medico, medicamentos)
        self.assertEqual(receta.paciente, paciente)
        self.assertEqual(receta.medico, medico)
        self.assertEqual(len(receta.medicamentos), 2)
        self.assertIn("Paracetamol 500mg", receta.medicamentos)
    
    def test_medicamentos_vacios(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        
        with self.assertRaises(ValueError):
            Receta(paciente, medico, [])
    
    def test_medicamentos_none(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        
        with self.assertRaises(ValueError):
            Receta(paciente, medico, None)
    
    def test_medicamento_vacio(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        medicamentos = ["Paracetamol 500mg", ""]
        
        with self.assertRaises(ValueError):
            Receta(paciente, medico, medicamentos)
    
    def test_str(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        medicamentos = ["Paracetamol 500mg"]
        
        receta = Receta(paciente, medico, medicamentos)
        resultado = str(receta)
        self.assertIn("Matias Zarzur", resultado)
        self.assertIn("Dr. Carlos López", resultado)
        self.assertIn("Paracetamol 500mg", resultado)

if __name__ == "__main__":
    unittest.main()