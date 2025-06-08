import unittest
from datetime import datetime
from src.models.receta import Receta
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestReceta(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.paciente = Paciente("María González", "87654321", "10/05/1990")
        self.medico = Medico("Dr. Rodríguez", "12345")
        self.medicamentos = ["Ibuprofeno 400mg", "Paracetamol 500mg"]
        

        cardiologia = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(cardiologia)
        
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)
    
    def test_crear_receta_exitosa(self):
        """Test de creación exitosa de receta"""

        resultado = str(self.receta)
        self.assertIn("María González", resultado)
        self.assertIn("Dr. Rodríguez", resultado)
        self.assertIn("Ibuprofeno 400mg", resultado)
        self.assertIn("Paracetamol 500mg", resultado)
    
    def test_representacion_string(self):
        """Test de representación en string de la receta"""
        resultado = str(self.receta)

        self.assertIn("María González", resultado)

        self.assertIn("Dr. Rodríguez", resultado)

        self.assertIn("Ibuprofeno 400mg", resultado)
        self.assertIn("Paracetamol 500mg", resultado)

        self.assertTrue(len(resultado) > 0)
    
    def test_receta_un_medicamento(self):
        """Test con receta de un solo medicamento"""
        medicamento_unico = ["Aspirina 100mg"]
        receta_simple = Receta(self.paciente, self.medico, medicamento_unico)
        resultado = str(receta_simple)
        self.assertIn("Aspirina 100mg", resultado)
        self.assertIn("María González", resultado)
    
    def test_receta_multiples_medicamentos(self):
        """Test con receta de múltiples medicamentos"""
        medicamentos_multiples = [
            "Atenolol 50mg",
            "Enalapril 10mg",
            "Simvastatina 20mg",
            "Aspirina 100mg"
        ]
        receta_compleja = Receta(self.paciente, self.medico, medicamentos_multiples)
        resultado = str(receta_compleja)
        

        for medicamento in medicamentos_multiples:
            self.assertIn(medicamento, resultado)
    
    def test_receta_diferentes_pacientes(self):
        """Test con diferentes pacientes"""
        otro_paciente = Paciente("Carlos López", "11223344", "20/08/1985")
        medicamentos_otros = ["Omeprazol 20mg"]
        
        receta_otro = Receta(otro_paciente, self.medico, medicamentos_otros)
        resultado = str(receta_otro)
        
        self.assertIn("Carlos López", resultado)
        self.assertIn("Dr. Rodríguez", resultado)
        self.assertIn("Omeprazol 20mg", resultado)
    
    def test_receta_diferentes_medicos(self):
        """Test con diferentes médicos"""
        otro_medico = Medico("Dra. Fernández", "67890")
        pediatria = Especialidad("Pediatría", ["martes", "jueves"])
        otro_medico.agregar_especialidad(pediatria)
        
        medicamentos_pediatria = ["Jarabe para la tos", "Vitamina D"]
        receta_pediatria = Receta(self.paciente, otro_medico, medicamentos_pediatria)
        resultado = str(receta_pediatria)
        
        self.assertIn("María González", resultado)
        self.assertIn("Dra. Fernández", resultado)
        self.assertIn("Jarabe para la tos", resultado)
        self.assertIn("Vitamina D", resultado)

if __name__ == "__main__":
    unittest.main()