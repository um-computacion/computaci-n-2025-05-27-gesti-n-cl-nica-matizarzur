import unittest
from datetime import datetime
from src.models.clinica import Clinica
from src.models.exceptions import PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException, RecetaInvalidaException

class TestClinica(unittest.TestCase):
    def test_crear_clinica(self):
        clinica = Clinica()
        self.assertEqual(len(clinica.pacientes), 0)
        self.assertEqual(len(clinica.medicos), 0)
        self.assertEqual(len(clinica.turnos), 0)
    
    def test_registrar_paciente(self):
        clinica = Clinica()
        clinica.registrar_paciente("12345678", "Matias Zarzur", "17/07/1977", "123-456-7890")
        self.assertEqual(len(clinica.pacientes), 1)
        
        paciente = clinica.buscar_paciente_por_dni("12345678")
        self.assertEqual(paciente.nombre, "Matias Zarzur")
    
    def test_registrar_medico(self):
        clinica = Clinica()
        clinica.registrar_medico("MAT001", "Dr. Carlos López", "Medicina General")
        self.assertEqual(len(clinica.medicos), 1)
        
        medico = clinica.buscar_medico_por_matricula("MAT001")
        self.assertEqual(medico.nombre, "Dr. Carlos López")
    
    def test_paciente_duplicado(self):
        clinica = Clinica()
        clinica.registrar_paciente("12345678", "Matias Zarzur", "17/07/1977", "123-456-7890")
        
        with self.assertRaises(ValueError):
            clinica.registrar_paciente("12345678", "Otro Nombre", "01/01/1990", "987-654-3210")
    
    def test_medico_duplicado(self):
        clinica = Clinica()
        clinica.registrar_medico("MAT001", "Dr. Carlos López", "Medicina General")
        
        with self.assertRaises(ValueError):
            clinica.registrar_medico("MAT001", "Dr. Ana García", "Cardiología")
    
    def test_agendar_turno_exitoso(self):
        clinica = Clinica()
        clinica.registrar_paciente("12345678", "Matias Zarzur", "17/07/1977", "123-456-7890")
        clinica.registrar_medico("MAT001", "Dr. Carlos López", "Medicina General")
        clinica.agregar_especialidad_medico("MAT001", "Cardiología", ["lunes", "miercoles"])
        
        fecha_hora = datetime(2024, 12, 16, 10, 0)
        turno = clinica.agendar_turno("12345678", "MAT001", "Cardiología", fecha_hora)
        
        self.assertIsNotNone(turno)
        self.assertEqual(len(clinica.turnos), 1)
    
    def test_emitir_receta_exitosa(self):
        clinica = Clinica()
        clinica.registrar_paciente("12345678", "Matias Zarzur", "17/07/1977", "123-456-7890")
        clinica.registrar_medico("MAT001", "Dr. Carlos López", "Medicina General")
        
        medicamentos = ["Paracetamol 500mg"]
        receta = clinica.emitir_receta("12345678", "MAT001", medicamentos)
        
        self.assertIsNotNone(receta)
        paciente = clinica.buscar_paciente_por_dni("12345678")
        self.assertEqual(len(paciente.historia_clinica.recetas), 1)

if __name__ == "__main__":
    unittest.main()