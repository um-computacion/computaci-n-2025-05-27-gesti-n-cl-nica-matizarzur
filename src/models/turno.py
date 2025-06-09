from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        if paciente is None:
            raise ValueError("El paciente no puede ser None")
        
        if medico is None:
            raise ValueError("El medico no puede ser None")
        
        if fecha_hora is None:
            raise ValueError("La fecha y hora no pueden ser None")
        
        if not especialidad or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacia")
        
        if especialidad is None:
            raise ValueError("La especialidad no puede ser None")
        
        if fecha_hora < datetime.now():
            raise ValueError("No se pueden agendar turnos en el pasado")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad.strip()
    
    def obtener_medico(self):
        return self.__medico
    
    def obtener_fecha_hora(self):
        return self.__fecha_hora
    
    def __str__(self):
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"Turno: {self.__paciente} con {self.__medico} - {self.__especialidad} - {fecha_str}"