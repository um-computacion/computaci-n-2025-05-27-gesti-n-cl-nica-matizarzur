import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno
from src.models.receta import Receta
from src.models.historiaclinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Diego Sanchez", "55667788", "22/03/1987")
        self.medico = Medico("Dr. Valeria Torres", "MAT77777")
        self.traumatologia = Especialidad("Traumatologia", ["martes", "jueves"])
        self.medico.agregar_especialidad(self.traumatologia)
        
        self.fecha_hora = datetime(2025, 6, 19, 15, 30)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, "Traumatologia")
        self.receta = Receta(self.paciente, self.medico, ["Diclofenac 50mg"])
        
        self.historia = HistoriaClinica(self.paciente)
    
    def test_crear_historia_clinica(self):
        self.assertEqual(len(self.historia.obtener_turnos()), 0)
        self.assertEqual(len(self.historia.obtener_recetas()), 0)
        self.assertIn("Diego Sanchez", str(self.historia))
    
    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno)
        
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], self.turno)
    
    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta)
        
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], self.receta)
    
    def test_obtener_copias_no_referencias(self):
        self.historia.agregar_turno(self.turno)
        
        turnos_obtenidos = self.historia.obtener_turnos()
        turnos_obtenidos.clear()
        
        self.assertEqual(len(self.historia.obtener_turnos()), 1)
    
    def test_agregar_turno_none(self):
        with self.assertRaises(ValueError):
            self.historia.agregar_turno(None)
    
    def test_agregar_receta_none(self):
        with self.assertRaises(ValueError):
            self.historia.agregar_receta(None)
    
    def test_str_representation_completa(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        resultado = str(self.historia)
        
        self.assertIn("Diego Sanchez", resultado)
        self.assertIn("Turnos", resultado)
        self.assertIn("Recetas", resultado)
        self.assertIn("Dr. Valeria Torres", resultado)
    
    def test_paciente_none(self):
        with self.assertRaises(ValueError):
            HistoriaClinica(None)
    
    def test_multiples_turnos_recetas(self):
        segundo_turno = Turno(self.paciente, self.medico, datetime(2025, 7, 1, 9, 0), "Traumatologia")
        segunda_receta = Receta(self.paciente, self.medico, ["Ibuprofeno 600mg"])
        
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_turno(segundo_turno)
        self.historia.agregar_receta(self.receta)
        self.historia.agregar_receta(segunda_receta)
        
        self.assertEqual(len(self.historia.obtener_turnos()), 2)
        self.assertEqual(len(self.historia.obtener_recetas()), 2)

if __name__ == "__main__":
    unittest.main()