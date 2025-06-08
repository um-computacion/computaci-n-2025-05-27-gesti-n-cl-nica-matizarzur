import unittest
from datetime import datetime
from src.models.historiaclinica import HistoriaClinica
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno
from src.models.receta import Receta

class TestHistoriaClinica(unittest.TestCase):
    def test_crear_historia_clinica(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        historia = HistoriaClinica(paciente)
        self.assertEqual(historia.paciente, paciente)
        self.assertEqual(len(historia.turnos), 0)
        self.assertEqual(len(historia.recetas), 0)
    
    def test_agregar_turno(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        fecha_hora = datetime(2024, 12, 16, 10, 0)
        
        turno = Turno(paciente, medico, "Cardiología", fecha_hora)
        historia = HistoriaClinica(paciente)
        historia.agregar_turno(turno)
        
        self.assertEqual(len(historia.turnos), 1)
        self.assertEqual(historia.turnos[0], turno)
    
    def test_agregar_receta(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        medicamentos = ["Paracetamol 500mg"]
        
        receta = Receta(paciente, medico, medicamentos)
        historia = HistoriaClinica(paciente)
        historia.agregar_receta(receta)
        
        self.assertEqual(len(historia.recetas), 1)
        self.assertEqual(historia.recetas[0], receta)
    
    def test_obtener_turnos_por_especialidad(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        especialidad1 = Especialidad("Cardiología", ["lunes", "miercoles"])
        especialidad2 = Especialidad("Neurología", ["martes", "jueves"])
        medico.agregar_especialidad(especialidad1)
        medico.agregar_especialidad(especialidad2)
        
        fecha_hora = datetime(2024, 12, 16, 10, 0)
        turno1 = Turno(paciente, medico, "Cardiología", fecha_hora)
        turno2 = Turno(paciente, medico, "Neurología", datetime(2024, 12, 17, 10, 0))
        
        historia = HistoriaClinica(paciente)
        historia.agregar_turno(turno1)
        historia.agregar_turno(turno2)
        
        turnos_cardio = historia.obtener_turnos_por_especialidad("Cardiología")
        self.assertEqual(len(turnos_cardio), 1)
        self.assertEqual(turnos_cardio[0], turno1)
    
    def test_str(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        historia = HistoriaClinica(paciente)
        resultado = str(historia)
        self.assertIn("Matias Zarzur", resultado)

if __name__ == "__main__":
    unittest.main()