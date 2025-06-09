from datetime import datetime
from src.models.paciente import Paciente
from src.models.medico import Medico

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        if paciente is None:
            raise ValueError("El paciente no puede ser None")
        
        if medico is None:
            raise ValueError("El medico no puede ser None")
        
        if medicamentos is None:
            raise ValueError("Los medicamentos no pueden ser None")
        
        if not medicamentos or len(medicamentos) == 0:
            raise ValueError("Debe incluir al menos un medicamento")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()
    
    def __str__(self):
        medicamentos_str = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        return f"Receta para {self.__paciente} - Medico: {self.__medico} - Medicamentos: {medicamentos_str} - Fecha: {fecha_str}"