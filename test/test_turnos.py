import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Sofia Martinez", "87654321", "12/05/1988")
        self.medico = Medico("Dr. Nicolas Vega", "MAT22222")
        self.dermatologia = Especialidad("Dermatologia", ["lunes", "miercoles", "viernes"])
        self.medico.agregar_especialidad(self.dermatologia)
        self.fecha_hora = datetime(2025, 6, 18, 10, 15)
    
    def test_crear_turno(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Dermatologia")
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
        self.assertIn("Sofia Martinez", str(turno))
        self.assertIn("Dr. Nicolas Vega", str(turno))
        self.assertIn("Dermatologia", str(turno))
    
    def test_paciente_none(self):
        with self.assertRaises(ValueError):
            Turno(None, self.medico, self.fecha_hora, "Dermatologia")
    
    def test_medico_none(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, self.fecha_hora, "Dermatologia")
    
    def test_fecha_none(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, None, "Dermatologia")
    
    def test_especialidad_vacia(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "")
    
    def test_str_completo(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Dermatologia")
        resultado = str(turno)
        self.assertIn("Sofia Martinez", resultado)
        self.assertIn("Dr. Nicolas Vega", resultado)
        self.assertIn("Dermatologia", resultado)
        self.assertIn("2025", resultado)
    
    def test_fecha_pasada(self):
        fecha_pasada = datetime(2020, 1, 1, 9, 0)
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, fecha_pasada, "Dermatologia")
    
    def test_especialidad_none(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, None)

if __name__ == "__main__":
    unittest.main()