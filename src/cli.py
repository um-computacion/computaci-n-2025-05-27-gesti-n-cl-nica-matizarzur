from datetime import datetime
from src.models.clinica import Clinica
from src.models.paciente import Paciente
from src.models.medico import Medico
from src.models.especialidad import Especialidad
from src.models.exceptions import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class CLI:
    def __init__(self):
        self.clinica = Clinica()
    
    def limpiar_pantalla(self):
        print("\n" * 50)
    
    def pausa(self):
        input("\nPresione Enter para continuar...")
    
    def mostrar_menu(self):
        print("\n" + "="*50)
        print("          SISTEMA DE GESTION DE CLINICA MEDICA")
        print("="*50)
        print("1) Agregar paciente")
        print("2) Agregar medico")
        print("3) Agendar turno")
        print("4) Agregar especialidad a medico")
        print("5) Emitir receta medica")
        print("6) Ver historia clinica de paciente")
        print("7) Ver listado completo de turnos")
        print("8) Ver listado completo de pacientes")
        print("9) Ver listado completo de medicos")
        print("0) Salir del sistema")
        print("="*50)
    
    def ejecutar(self):
        print("Bienvenido al Sistema de Gestion de Clinica Medica")
        print("Iniciando sistema...")
        
        while True:
            self.mostrar_menu()
            try:
                opcion = input("Ingrese el numero de la opcion deseada: ").strip()
                
                if opcion == "0":
                    print("\nCerrando sistema...")
                    print("Gracias por utilizar el Sistema de Gestion de Clinica Medica")
                    break
                elif opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_todos_turnos()
                elif opcion == "8":
                    self.ver_todos_pacientes()
                elif opcion == "9":
                    self.ver_todos_medicos()
                else:
                    print("Error: Opcion invalida. Por favor ingrese un numero del 0 al 9.")
                    
                if opcion != "0":
                    self.pausa()
                    
            except KeyboardInterrupt:
                print("\n\nInterrupcion detectada. Cerrando sistema...")
                print("Gracias por utilizar el Sistema de Gestion de Clinica Medica")
                break
            except Exception as e:
                print(f"Error critico del sistema: {e}")
                print("Contacte al administrador del sistema.")
                self.pausa()
    
    def agregar_paciente(self):
        print("\n" + "-"*50)
        print("           REGISTRO DE NUEVO PACIENTE")
        print("-"*50)
        
        try:
            print("Por favor, complete los siguientes datos del paciente:")
            print()
            
            while True:
                nombre = input("Nombre completo del paciente: ").strip()
                if nombre:
                    break
                print("Error: El nombre no puede estar vacio. Intente nuevamente.")
            
            while True:
                dni = input("Numero de DNI (solo numeros): ").strip()
                if dni:
                    break
                print("Error: El DNI no puede estar vacio. Intente nuevamente.")
            
            while True:
                fecha_nacimiento = input("Fecha de nacimiento (formato dd/mm/aaaa): ").strip()
                if fecha_nacimiento:
                    break
                print("Error: La fecha no puede estar vacia. Intente nuevamente.")
            
            print("\nProcesando datos del paciente...")
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)
            
            print("EXITO: El paciente ha sido registrado correctamente en el sistema.")
            print(f"Paciente: {nombre}")
            print(f"DNI: {dni}")
            print(f"Fecha de nacimiento: {fecha_nacimiento}")
            print("Se ha creado automaticamente una historia clinica para este paciente.")
            
        except ValueError as e:
            print(f"ERROR DE VALIDACION: {e}")
            print("Verifique que los datos ingresados sean correctos.")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def agregar_medico(self):
        print("\n" + "-"*50)
        print("           REGISTRO DE NUEVO MEDICO")
        print("-"*50)
        
        try:
            print("Por favor, complete los siguientes datos del medico:")
            print()
            
            while True:
                nombre = input("Nombre completo del medico: ").strip()
                if nombre:
                    break
                print("Error: El nombre no puede estar vacio. Intente nuevamente.")
            
            while True:
                matricula = input("Numero de matricula profesional: ").strip()
                if matricula:
                    break
                print("Error: La matricula no puede estar vacia. Intente nuevamente.")
            
            print("\nProcesando datos del medico...")
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            
            print("EXITO: El medico ha sido registrado correctamente en el sistema.")
            print(f"Medico: {nombre}")
            print(f"Matricula: {matricula}")
            print("NOTA: Recuerde agregar las especialidades y dias de atencion del medico.")
            
        except ValueError as e:
            print(f"ERROR DE VALIDACION: {e}")
            print("Verifique que los datos ingresados sean correctos.")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def agendar_turno(self):
        print("\n" + "-"*50)
        print("              AGENDAR NUEVO TURNO")
        print("-"*50)
        
        try:
            print("Complete los siguientes datos para agendar el turno:")
            print()
            
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matricula del medico: ").strip()
            especialidad = input("Especialidad medica requerida: ").strip()
            
            print("\nInformacion de fecha y hora:")
            fecha_str = input("Fecha del turno (formato dd/mm/aaaa): ").strip()
            hora_str = input("Hora del turno (formato HH:MM): ").strip()
            
            print("\nValidando disponibilidad...")
            fecha_hora = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
            
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            
            print("EXITO: El turno ha sido agendado correctamente.")
            print("Detalles del turno:")
            print(f"Paciente DNI: {dni}")
            print(f"Medico matricula: {matricula}")
            print(f"Especialidad: {especialidad}")
            print(f"Fecha: {fecha_str}")
            print(f"Hora: {hora_str}")
            print("El turno ha sido agregado automaticamente a la historia clinica del paciente.")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, 
                MedicoNoDisponibleException, TurnoOcupadoException) as e:
            print(f"ERROR DE SISTEMA: {e}")
            print("Verifique que el paciente y medico existan, y que el medico atienda esa especialidad en el dia solicitado.")
        except ValueError as e:
            print(f"ERROR DE FORMATO: {e}")
            print("Verifique el formato de fecha y hora ingresados.")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def agregar_especialidad(self):
        print("\n" + "-"*50)
        print("         AGREGAR ESPECIALIDAD A MEDICO")
        print("-"*50)
        
        try:
            print("Complete los datos para agregar una nueva especialidad:")
            print()
            
            matricula = input("Matricula del medico: ").strip()
            
            print("Buscando medico en el sistema...")
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            print(f"Medico encontrado: {medico}")
            print()
            
            tipo_especialidad = input("Nombre de la especialidad medica: ").strip()
            
            print("\nDias de atencion disponibles:")
            print("Opciones: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
            print("Ingrese los dias separados por comas (ejemplo: lunes, miercoles, viernes)")
            dias_str = input("Dias de atencion: ").strip()
            
            dias = [dia.strip() for dia in dias_str.split(",")]
            
            print("\nValidando datos de la especialidad...")
            especialidad = Especialidad(tipo_especialidad, dias)
            
            medico.agregar_especialidad(especialidad)
            
            print("EXITO: La especialidad ha sido agregada correctamente al medico.")
            print("Detalles de la especialidad:")
            print(f"Especialidad: {tipo_especialidad}")
            print(f"Dias de atencion: {', '.join(dias)}")
            print("El medico ya puede atender pacientes en esta especialidad en los dias indicados.")
            
        except MedicoNoEncontradoException as e:
            print(f"ERROR: {e}")
            print("Verifique que la matricula del medico sea correcta.")
        except ValueError as e:
            print(f"ERROR DE VALIDACION: {e}")
            print("Verifique que los dias ingresados sean validos y no esten duplicados.")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def emitir_receta(self):
        print("\n" + "-"*50)
        print("              EMITIR RECETA MEDICA")
        print("-"*50)
        
        try:
            print("Complete los datos para emitir la receta medica:")
            print()
            
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matricula del medico: ").strip()
            
            print("\nMedicamentos recetados:")
            print("Ingrese los medicamentos con sus dosificaciones separados por comas")
            print("Ejemplo: Paracetamol 500mg, Ibuprofeno 400mg, Amoxicilina 875mg")
            medicamentos_str = input("Lista de medicamentos: ").strip()
            
            medicamentos = [med.strip() for med in medicamentos_str.split(",")]
            
            print("\nValidando datos y emitiendo receta...")
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            
            print("EXITO: La receta medica ha sido emitida correctamente.")
            print("Detalles de la receta:")
            print(f"Paciente DNI: {dni}")
            print(f"Medico matricula: {matricula}")
            print("Medicamentos recetados:")
            for i, medicamento in enumerate(medicamentos, 1):
                print(f"  {i}. {medicamento}")
            print("La receta ha sido agregada automaticamente a la historia clinica del paciente.")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, 
                RecetaInvalidaException) as e:
            print(f"ERROR DE SISTEMA: {e}")
            print("Verifique que el paciente y medico existan, y que haya al menos un medicamento.")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def ver_historia_clinica(self):
        print("\n" + "-"*50)
        print("            HISTORIA CLINICA DEL PACIENTE")
        print("-"*50)
        
        try:
            dni = input("Ingrese el DNI del paciente: ").strip()
            
            print("Buscando historia clinica...")
            historia = self.clinica.obtener_historia_clinica(dni)
            
            print("HISTORIA CLINICA ENCONTRADA:")
            print("="*50)
            print(str(historia))
            print("="*50)
            
        except PacienteNoEncontradoException as e:
            print(f"ERROR: {e}")
            print("Verifique que el DNI del paciente sea correcto.")
        except Exception as e:
            print(f"ERROR: {e}")
    
    def ver_todos_turnos(self):
        print("\n" + "-"*50)
        print("           LISTADO COMPLETO DE TURNOS")
        print("-"*50)
        
        turnos = self.clinica.obtener_turnos()
        
        if not turnos:
            print("INFORMACION: No hay turnos agendados en el sistema.")
            print("Puede agendar turnos usando la opcion 3 del menu principal.")
        else:
            print(f"Total de turnos agendados: {len(turnos)}")
            print("-"*50)
            for i, turno in enumerate(turnos, 1):
                print(f"{i:2d}. {turno}")
            print("-"*50)
    
    def ver_todos_pacientes(self):
        print("\n" + "-"*50)
        print("          LISTADO COMPLETO DE PACIENTES")
        print("-"*50)
        
        pacientes = self.clinica.obtener_pacientes()
        
        if not pacientes:
            print("INFORMACION: No hay pacientes registrados en el sistema.")
            print("Puede registrar pacientes usando la opcion 1 del menu principal.")
        else:
            print(f"Total de pacientes registrados: {len(pacientes)}")
            print("-"*50)
            for i, paciente in enumerate(pacientes, 1):
                print(f"{i:2d}. {paciente}")
            print("-"*50)
    
    def ver_todos_medicos(self):
        print("\n" + "-"*50)
        print("           LISTADO COMPLETO DE MEDICOS")
        print("-"*50)
        
        medicos = self.clinica.obtener_medicos()
        
        if not medicos:
            print("INFORMACION: No hay medicos registrados en el sistema.")
            print("Puede registrar medicos usando la opcion 2 del menu principal.")
        else:
            print(f"Total de medicos registrados: {len(medicos)}")
            print("-"*50)
            for i, medico in enumerate(medicos, 1):
                print(f"{i:2d}. {medico}")
            print("-"*50)


if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()