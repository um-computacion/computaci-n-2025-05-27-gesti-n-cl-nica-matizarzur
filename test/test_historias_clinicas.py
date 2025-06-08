import unittest
from datetime import datetime
from src.models.historiaclinica import HistoriaClinica
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.turno import Turno
from src.models.receta import Receta
from src.models.especialidad import Especialidad

class TestHistoriaClinica(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.paciente = Paciente("Ana Martínez", "55667788", "25/12/1988")
        self.historia = HistoriaClinica(self.paciente)
        

        self.medico = Medico("Dr. López", "98765")
        cardiologia = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])
        self.medico.agregar_especialidad(cardiologia)
        

        self.fecha_turno = datetime(2025, 6, 18, 15, 30)  # Miércoles 18 de junio, 15:30
        self.turno = Turno(self.paciente, self.medico, self.fecha_turno, "Cardiología")
        self.medicamentos = ["Enalapril 10mg", "Atenolol 50mg"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)
    
    def test_crear_historia_clinica_exitosa(self):
        """Test de creación exitosa de historia clínica"""

        turnos = self.historia.obtener_turnos()
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(turnos), 0)
        self.assertEqual(len(recetas), 0)
    
    def test_agregar_turno(self):
        """Test de agregar turno a la historia clínica"""
        self.historia.agregar_turno(self.turno)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], self.turno)
    
    def test_agregar_receta(self):
        """Test de agregar receta a la historia clínica"""
        self.historia.agregar_receta(self.receta)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], self.receta)
    
    def test_obtener_turnos_copia(self):
        """Test que obtener_turnos devuelve una copia de la lista"""
        self.historia.agregar_turno(self.turno)
        turnos1 = self.historia.obtener_turnos()
        turnos2 = self.historia.obtener_turnos()
        

        self.assertIsNot(turnos1, turnos2)

        self.assertEqual(turnos1, turnos2)
    
    def test_obtener_recetas_copia(self):
        """Test que obtener_recetas devuelve una copia de la lista"""
        self.historia.agregar_receta(self.receta)
        recetas1 = self.historia.obtener_recetas()
        recetas2 = self.historia.obtener_recetas()
        

        self.assertIsNot(recetas1, recetas2)

        self.assertEqual(recetas1, recetas2)
    
    def test_agregar_multiples_turnos(self):
        """Test de agregar múltiples turnos"""
        # Crear segundo médico y turno
        medico2 = Medico("Dra. García", "11111")
        pediatria = Especialidad("Pediatría", ["martes", "jueves"])
        medico2.agregar_especialidad(pediatria)
        
        fecha_turno2 = datetime(2025, 6, 19, 10, 0)  # Jueves 19 de junio, 10:00
        turno2 = Turno(self.paciente, medico2, fecha_turno2, "Pediatría")
        
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_turno(turno2)
        
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 2)
        self.assertIn(self.turno, turnos)
        self.assertIn(turno2, turnos)
    
    def test_agregar_multiples_recetas(self):
        """Test de agregar múltiples recetas"""

        medicamentos2 = ["Ibuprofeno 400mg"]
        receta2 = Receta(self.paciente, self.medico, medicamentos2)
        
        self.historia.agregar_receta(self.receta)
        self.historia.agregar_receta(receta2)
        
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 2)
        self.assertIn(self.receta, recetas)
        self.assertIn(receta2, recetas)
    
    def test_representacion_string(self):
        """Test de representación en string de la historia clínica"""
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        
        resultado = str(self.historia)
        self.assertIn("Ana Martínez", resultado)

        self.assertTrue(len(resultado) > 0)
    
    def test_historia_clinica_vacia(self):
        """Test de historia clínica sin turnos ni recetas"""
        resultado = str(self.historia)
        self.assertIn("Ana Martínez", resultado)

        self.assertTrue(len(resultado) > 0)

if __name__ == "__main__":
    unittest.main()