from .especialidad import Especialidad

class Medico:
    def __init__(self, nombre, matricula):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        
        if not matricula or not matricula.strip():
            raise ValueError("La matricula no puede estar vacia")
        
        if not matricula.startswith("MAT"):
            raise ValueError("La matricula debe tener formato valido")
        
        self.__nombre = nombre.strip()
        self.__matricula = matricula.strip()
        self.__especialidades = []
    
    def agregar_especialidad(self, especialidad):
        for esp in self.__especialidades:
            if esp.obtener_especialidad() == especialidad.obtener_especialidad():
                raise ValueError("La especialidad ya existe para este medico")
        
        self.__especialidades.append(especialidad)
    
    def obtener_matricula(self):
        return self.__matricula
    
    def obtener_especialidad_para_dia(self, dia):
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None
    
    def __str__(self):
        especialidades_str = ", ".join([esp.obtener_especialidad() for esp in self.__especialidades])
        if especialidades_str:
            return f"Dr. {self.__nombre} - Matricula: {self.__matricula} - Especialidades: {especialidades_str}"
        else:
            return f"Dr. {self.__nombre} - Matricula: {self.__matricula}"