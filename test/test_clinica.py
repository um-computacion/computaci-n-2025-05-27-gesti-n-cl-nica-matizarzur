import unittest
from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.clinica import Clinica
from src.models.exceptions import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)


class TestClinica(unittest.TestCase):
    
    def setUp(self):
        self.clinica = Clinica()

        self.paciente1 = Paciente("Ana Martínez", "12345678", "15/03/1990")
        self.paciente2 = Paciente("Carlos López", "87654321", "20/05/1985")
        
        self.medico1 = Medico("Dr. Juan Pérez", "MAT12345")
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.medico1.agregar_especialidad(self.pediatria)
        
        self.medico2 = Medico("Dra. María García", "MAT67890")
        self.cardiologia = Especialidad("Cardiología", ["martes", "jueves"])
        self.medico2.agregar_especialidad(self.cardiologia)
        
        # Fechas de prueba
        self.fecha_lunes = datetime(2025, 6, 16, 14, 30) 
        self.fecha_martes = datetime(2025, 6, 17, 10, 0)  
        self.fecha_miercoles = datetime(2025, 6, 18, 16, 0)  
    
    # Tests para agregar pacientes
    
    def test_agregar_paciente_exitoso(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "12345678")

        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIsNotNone(historia)
    
    def test_agregar_paciente_duplicado(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        paciente_duplicado = Paciente("Ana Duplicada", "12345678", "01/01/2000")
        with self.assertRaises(ValueError) as context:
            self.clinica.agregar_paciente(paciente_duplicado)
        
        self.assertIn("ya está registrado", str(context.exception))
    
    def test_agregar_multiples_pacientes(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_paciente(self.paciente2)
        
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 2)
    
    # Tests para agregar médicos
    
    def test_agregar_medico_exitoso(self):
        self.clinica.agregar_medico(self.medico1)
        
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "MAT12345")
    
    def test_agregar_medico_duplicado(self):
        self.clinica.agregar_medico(self.medico1)
        
        medico_duplicado = Medico("Dr. Juan Duplicado", "MAT12345")
        with self.assertRaises(ValueError) as context:
            self.clinica.agregar_medico(medico_duplicado)
        
        self.assertIn("ya está registrado", str(context.exception))
    
    def test_obtener_medico_por_matricula(self):
        self.clinica.agregar_medico(self.medico1)
        
        medico = self.clinica.obtener_medico_por_matricula("MAT12345")
        self.assertEqual(medico.obtener_matricula(), "MAT12345")
    
    def test_obtener_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.obtener_medico_por_matricula("MAT99999")
    
    # Tests para agendar turnos
    
    def test_agendar_turno_exitoso(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        self.clinica.agendar_turno("12345678", "MAT12345", "Pediatría", self.fecha_lunes)
        
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "MAT12345")

        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_turnos()), 1)
    
    def test_agendar_turno_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "MAT12345", "Pediatría", self.fecha_lunes)
    
    def test_agendar_turno_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT99999", "Pediatría", self.fecha_lunes)
    
    def test_agendar_turno_duplicado(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_paciente(self.paciente2)
        self.clinica.agregar_medico(self.medico1)

        self.clinica.agendar_turno("12345678", "MAT12345", "Pediatría", self.fecha_lunes)

        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("87654321", "MAT12345", "Pediatría", self.fecha_lunes)
    
    def test_agendar_turno_medico_no_trabaja_ese_dia(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)  
        
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT12345", "Pediatría", self.fecha_martes)
    
    def test_agendar_turno_especialidad_incorrecta(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MAT12345", "Cardiología", self.fecha_lunes)

    
    def test_emitir_receta_exitosa(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        medicamentos = ["Paracetamol 500mg", "Ibuprofeno 400mg"]
        self.clinica.emitir_receta("12345678", "MAT12345", medicamentos)
        
        historia = self.clinica.obtener_historia_clinica("12345678")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
    
    def test_emitir_receta_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "MAT12345", ["Aspirina"])
    
    def test_emitir_receta_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("12345678", "MAT99999", ["Aspirina"])
    
    def test_emitir_receta_sin_medicamentos(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "MAT12345", [])
    
    def test_emitir_receta_medicamentos_vacios(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)
        
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "MAT12345", ["", "  ", "Aspirina"])

    
    def test_obtener_historia_clinica_existente(self):
        self.clinica.agregar_paciente(self.paciente1)
        
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIsNotNone(historia)
        self.assertEqual(len(historia.obtener_turnos()), 0)
        self.assertEqual(len(historia.obtener_recetas()), 0)
    
    def test_obtener_historia_clinica_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica("99999999")
    
    def test_historia_clinica_se_actualiza_con_turnos_y_recetas(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)

        self.clinica.agendar_turno("12345678", "MAT12345", "Pediatría", self.fecha_lunes)

        self.clinica.emitir_receta("12345678", "MAT12345", ["Paracetamol"])

        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)
    
    
    def test_validar_existencia_paciente_existente(self):
        self.clinica.agregar_paciente(self.paciente1)

        self.clinica.validar_existencia_paciente("12345678")
    
    def test_validar_existencia_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.validar_existencia_paciente("99999999")
    
    def test_validar_existencia_medico_existente(self):
        self.clinica.agregar_medico(self.medico1)

        self.clinica.validar_existencia_medico("MAT12345")
    
    def test_validar_existencia_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.validar_existencia_medico("MAT99999")
    
    def test_validar_turno_no_duplicado_exitoso(self):
        self.clinica.agregar_paciente(self.paciente1)
        self.clinica.agregar_medico(self.medico1)

        self.clinica.agendar_turno("12345678", "MAT12345", "Pediatría", self.fecha_lunes)

        with self.assertRaises(TurnoOcupadoException):
            self.clinica.validar_turno_no_duplicado("MAT12345", self.fecha_lunes)
    
    # Tests para métodos utilitarios
    
    def test_obtener_dia_semana_en_espanol(self):
        dia = self.clinica.obtener_dia_semana_en_espanol(self.fecha_lunes)
        self.assertEqual(dia, "lunes")

        dia = self.clinica.obtener_dia_semana_en_espanol(self.fecha_martes)
        self.assertEqual(dia, "martes")
    
    def test_obtener_especialidad_disponible(self):
        especialidad = self.clinica.obtener_especialidad_disponible(self.medico1, "lunes")
        self.assertEqual(especialidad, "Pediatría")
    
    def test_obtener_especialidad_no_disponible(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.obtener_especialidad_disponible(self.medico1, "martes")
    
    def test_validar_especialidad_en_dia_correcta(self):
        self.clinica.validar_especialidad_en_dia(self.medico1, "Pediatría", "lunes")
    
    def test_validar_especialidad_en_dia_incorrecta(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.validar_especialidad_en_dia(self.medico1, "Cardiología", "lunes")
    
    def test_validar_especialidad_dia_no_disponible(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.validar_especialidad_en_dia(self.medico1, "Pediatría", "martes")


if __name__ == "__main__":
    unittest.main()