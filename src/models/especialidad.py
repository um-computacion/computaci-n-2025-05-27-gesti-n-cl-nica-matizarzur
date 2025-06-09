class Especialidad:
    def __init__(self, tipo, dias):
        if not tipo or not tipo.strip():
            raise ValueError("La especialidad no puede estar vacia")
        
        if not dias or len(dias) == 0:
            raise ValueError("Debe tener al menos un dia de atencion")
        
        dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        dias_normalizados = []
        
        for dia in dias:
            dia_lower = dia.lower().strip()
            if dia_lower not in dias_validos:
                raise ValueError(f"Dia invalido: {dia}")
            if dia_lower in dias_normalizados:
                raise ValueError("No se permiten dias duplicados")
            dias_normalizados.append(dia_lower)
        
        self.__tipo = tipo.strip()
        self.__dias = dias_normalizados
    
    def obtener_especialidad(self):
        return self.__tipo
    
    def verificar_dia(self, dia):
        return dia.lower().strip() in self.__dias
    
    def __str__(self):
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Dias: {dias_str})"