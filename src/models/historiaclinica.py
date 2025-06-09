from src.models.paciente import Paciente
from src.models.turno import Turno
from src.models.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente):
        if paciente is None:
            raise ValueError("El paciente no puede ser None")
        
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []
    
    def agregar_turno(self, turno):
        if turno is None:
            raise ValueError("El turno no puede ser None")
        
        self.__turnos.append(turno)
    
    def agregar_receta(self, receta):
        if receta is None:
            raise ValueError("La receta no puede ser None")
        
        self.__recetas.append(receta)
    
    def obtener_turnos(self):
        return self.__turnos.copy()
    
    def obtener_recetas(self):
        return self.__recetas.copy()
    
    def __str__(self):
        resultado = f"Historia Clinica de {self.__paciente}\n"
        resultado += f"Turnos: {len(self.__turnos)}\n"
        
        for i, turno in enumerate(self.__turnos, 1):
            resultado += f"  {i}. {turno}\n"
        
        resultado += f"Recetas: {len(self.__recetas)}\n"
        
        for i, receta in enumerate(self.__recetas, 1):
            resultado += f"  {i}. {receta}\n"
        
        return resultado.strip()