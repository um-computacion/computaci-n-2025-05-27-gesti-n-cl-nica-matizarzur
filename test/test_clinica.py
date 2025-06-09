import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.clinica import Clinica
from src.models.exceptions import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        
        self.paciente1 = Paciente("Lucia Vargas", "33445566", "08/11/1989")
        self.paciente2 = Paciente("Rodrigo Moreno", "77889900", "12/07/1993")
        
        self.medico1 = Medico("Dr. Sebastian Castro", "MAT11223")
        self.dermatologia = Especialidad("Dermatologia", ["lunes", "miercoles", "viernes"])
        self.medico1.agregar_especialidad(self.dermatologia)
        
        self.fecha_lunes = datetime(2025, 6, 16, 14, 30)
    
    def test_agregar_paciente(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "33445566")
    
    def test_paciente_duplicado(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        paciente_duplicado = Paciente("Lucia Duplicada", "33445566", "01/01/2000")
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(paciente_duplicado)
    
    def test_agregar_medico(self):
        self.clinica.agregar_medico(self.medico1)
        
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "MAT11223")
    
    def test_medico_duplicado(self):
        self.clinica.agregar_medico(self.medico1)
        
        medico_duplicado = Medico("Dr. Sebastian Duplicado", "MAT11223")
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(medico_duplicado)
    
    def test_agregar_especialidad(self):
        self.clinica.agregar_medico(self.medico1)
        urologia = Especialidad("Urologia", ["martes", "jueves"])
        
        medico = self.clinica.obtener_medico_por_matricula("MAT11223")
        medico.agregar_especialidad(urologia)
        
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Urologia")
    
    def test_error_agregar_especialidad(self):
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.obtener_medico_por_matricula("MAT99999")
    
    def test_agendar_turno_exitoso(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        self.clinica.agendar_turno("33445566", "MAT11223", "Dermatologia", self.fecha_lunes)
        
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "MAT11223")
    
    def test_turno_duplicado(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_paciente(self.paciente2)
        self.clinica.agregar_medico(self.medico1)
        
        self.clinica.agendar_turno("33445566", "MAT11223", "Dermatologia", self.fecha_lunes)
        
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("77889900", "MAT11223", "Dermatologia", self.fecha_lunes)
    
    def test_error_turno_fecha_pasada(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        fecha_pasada = datetime(2024, 1, 1, 10, 0)
        
        with self.assertRaises(ValueError) as context:
            self.clinica.agendar_turno("33445566", "MAT11223", "Dermatologia", fecha_pasada)
        
        self.assertIn("pasado", str(context.exception).lower())

    def test_error_turno_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "MAT11223", "Dermatologia", self.fecha_lunes)
    
    def test_error_turno_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.agendar_turno("33445566", "MAT99999", "Dermatologia", self.fecha_lunes)
    
    def test_error_medico_no_trabaja_ese_dia(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        fecha_martes = datetime(2025, 6, 17, 14, 30)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("33445566", "MAT11223", "Dermatologia", fecha_martes)
    
    def test_emitir_receta(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        self.clinica.emitir_receta("33445566", "MAT11223", ["Clotrimazol 1%"])
        
        historia = self.clinica.obtener_historia_clinica("33445566")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
    
    def test_error_receta_sin_medicamentos(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("33445566", "MAT11223", [])
    
    def test_historia_clinica_guarda_correctamente(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        self.clinica.agendar_turno("33445566", "MAT11223", "Dermatologia", self.fecha_lunes)
        self.clinica.emitir_receta("33445566", "MAT11223", ["Hidrocortisona 0.5%"])
        
        historia = self.clinica.obtener_historia_clinica("33445566")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)
    
    def test_error_receta_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "MAT11223", ["Medicamento"])
    
    def test_error_receta_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        with self.assertRaises(MedicoNoEncontradoException):
            self.clinica.emitir_receta("33445566", "MAT99999", ["Medicamento"])

if __name__ == "__main__":
    unittest.main()