from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.turno import Turno
from src.models.receta import Receta
from src.models.historiaclinica import HistoriaClinica
from src.models.exceptions import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}
    
    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError("Ya existe un paciente con ese DNI")
        
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)
    
    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError("Ya existe un medico con esa matricula")
        
        self.__medicos[matricula] = medico
    
    def obtener_pacientes(self):
        return list(self.__pacientes.values())
    
    def obtener_medicos(self):
        return list(self.__medicos.values())
    
    def obtener_medico_por_matricula(self, matricula):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException("Medico no encontrado")
        return self.__medicos[matricula]
    
    def validar_existencia_paciente(self, dni):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException("Paciente no encontrado")
    
    def validar_existencia_medico(self, matricula):
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException("Medico no encontrado")
    
    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and 
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException("Ya existe un turno en esa fecha y hora")
    
    def obtener_dia_semana_en_espanol(self, fecha_hora):
        dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        return dias[fecha_hora.weekday()]
    
    def obtener_especialidad_disponible(self, medico, dia_semana):
        return medico.obtener_especialidad_para_dia(dia_semana)
    
    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia_semana):
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if (especialidad_disponible is None or 
            especialidad_disponible != especialidad_solicitada):
            raise MedicoNoDisponibleException("El medico no atiende esa especialidad en ese dia")
    
    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        if fecha_hora < datetime.now():
            raise ValueError("No se pueden agendar turnos en el pasado")
        
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        
        medico = self.__medicos[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        
        paciente = self.__pacientes[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)
    
    def obtener_turnos(self):
        return self.__turnos.copy()
    
    def emitir_receta(self, dni, matricula, medicamentos):
        if not medicamentos or len(medicamentos) == 0:
            raise RecetaInvalidaException("La receta debe tener al menos un medicamento")
        
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)
    
    def obtener_historia_clinica(self, dni):
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]