import unittest
from datetime import datetime
from src.models.turno import Turno
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.paciente = Paciente("Juan Pérez", "12345678", "15/03/1985")
        self.medico = Medico("Dr. García", "54321")
        self.fecha_hora = datetime(2025, 6, 16, 10, 30)  
        self.especialidad = "Cardiología"
        

        cardiologia = Especialidad("Cardiología", ["lunes", "miércoles", "viernes"])
        self.medico.agregar_especialidad(cardiologia)
        
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)
    
    def test_crear_turno_exitoso(self):
        """Test de creación exitosa de turno"""
        self.assertEqual(self.turno.obtener_medico(), self.medico)
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)
    
    def test_obtener_medico(self):
        """Test de obtención del médico del turno"""
        medico_obtenido = self.turno.obtener_medico()
        self.assertEqual(medico_obtenido.obtener_matricula(), "54321")
    
    def test_obtener_fecha_hora(self):
        """Test de obtención de fecha y hora del turno"""
        fecha_obtenida = self.turno.obtener_fecha_hora()
        self.assertEqual(fecha_obtenida, self.fecha_hora)
    
    def test_representacion_string(self):
        """Test de representación en string del turno"""
        resultado = str(self.turno)
        self.assertIn("Juan Pérez", resultado)
        self.assertIn("Dr. García", resultado)
        self.assertIn("Cardiología", resultado)

        self.assertTrue(len(resultado) > 0)
    
    def test_turno_diferente_especialidad(self):
        """Test con turno de diferente especialidad"""

        medico_pediatra = Medico("Dra. López", "99999")
        pediatria = Especialidad("Pediatría", ["martes", "jueves"])
        medico_pediatra.agregar_especialidad(pediatria)
        
        fecha_martes = datetime(2025, 6, 17, 14, 0)  
        turno_pediatria = Turno(self.paciente, medico_pediatra, fecha_martes, "Pediatría")
        
        self.assertEqual(turno_pediatria.obtener_medico(), medico_pediatra)
        self.assertEqual(turno_pediatria.obtener_fecha_hora(), fecha_martes)
    
    def test_turno_mismo_paciente_diferente_medico(self):
        """Test con mismo paciente pero diferente médico"""
        otro_medico = Medico("Dr. Martínez", "77777")
        neurologia = Especialidad("Neurología", ["sábado"])
        otro_medico.agregar_especialidad(neurologia)
        
        fecha_sabado = datetime(2025, 6, 21, 9, 0)  
        otro_turno = Turno(self.paciente, otro_medico, fecha_sabado, "Neurología")
        
        
        self.assertEqual(self.turno.obtener_medico().obtener_matricula(), "54321")
        self.assertEqual(otro_turno.obtener_medico().obtener_matricula(), "77777")

if __name__ == "__main__":
    unittest.main()