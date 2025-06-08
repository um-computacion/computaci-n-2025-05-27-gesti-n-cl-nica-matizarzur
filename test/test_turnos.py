import unittest
from datetime import datetime
from src.models.turno import Turno
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    def test_crear_turno(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        fecha_hora = datetime(2024, 12, 16, 10, 0)
        
        turno = Turno(paciente, medico, especialidad.nombre, fecha_hora)
        self.assertEqual(turno.paciente, paciente)
        self.assertEqual(turno.medico, medico)
        self.assertEqual(turno.especialidad, "Cardiología")
        self.assertEqual(turno.fecha_hora, fecha_hora)
    
    def test_medico_no_atiende_especialidad(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        fecha_hora = datetime(2024, 12, 16, 10, 0)
        
        with self.assertRaises(ValueError):
            Turno(paciente, medico, "Neurología", fecha_hora)
    
    def test_medico_no_atiende_ese_dia(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        fecha_hora = datetime(2024, 12, 17, 10, 0)  # Martes
        
        with self.assertRaises(ValueError):
            Turno(paciente, medico, "Cardiología", fecha_hora)
    
    def test_fecha_pasada(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        fecha_hora = datetime(2020, 12, 16, 10, 0)
        
        with self.assertRaises(ValueError):
            Turno(paciente, medico, "Cardiología", fecha_hora)
    
    def test_str(self):
        paciente = Paciente("Matias Zarzur", "12345678", "17/07/1977")
        medico = Medico("Dr. Carlos López", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        fecha_hora = datetime(2024, 12, 16, 10, 0)
        
        turno = Turno(paciente, medico, "Cardiología", fecha_hora)
        resultado = str(turno)
        self.assertIn("Matias Zarzur", resultado)
        self.assertIn("Dr. Carlos López", resultado)
        self.assertIn("Cardiología", resultado)

if __name__ == "__main__":
    unittest.main()