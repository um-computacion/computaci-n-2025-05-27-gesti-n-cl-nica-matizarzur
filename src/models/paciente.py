from datetime import datetime

class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        if not dni or not dni.strip():
            raise ValueError("El DNI no puede estar vacio")
        if not fecha_nacimiento or not fecha_nacimiento.strip():
            raise ValueError("La fecha de nacimiento no puede estar vacia")
        
        if not dni.isdigit():
            raise ValueError("El DNI debe contener exclusivamente numeros")
        
        if not self._validar_fecha(fecha_nacimiento):
            raise ValueError("La fecha debe estar en formato dd/mm/aaaa y ser valida")
        
        self.__nombre = nombre.strip()
        self.__dni = dni.strip()
        self.__fecha_nacimiento = fecha_nacimiento.strip()
    
    def _validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha.strip(), "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def obtener_dni(self):
        return self.__dni
    
    def __str__(self):
        return f"Paciente: {self.__nombre}, DNI: {self.__dni}, Fecha de nacimiento: {self.__fecha_nacimiento}"
    