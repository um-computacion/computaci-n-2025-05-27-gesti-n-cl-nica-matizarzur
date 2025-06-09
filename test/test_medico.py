import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.pediatria = Especialidad("Pediatria", ["lunes", "miercoles", "viernes"])
        self.cardiologia = Especialidad("Cardiologia", ["martes", "jueves"])
    
    def test_crear_medico(self):
        medico = Medico("Dr. Ignacio Martinez", "MAT78945")
        self.assertEqual(medico.obtener_matricula(), "MAT78945")
        self.assertIn("Dr. Ignacio Martinez", str(medico))
        self.assertIn("MAT78945", str(medico))
    
    def test_agregar_especialidad(self):
        medico = Medico("Dr. Ana Castro", "MAT12367")
        medico.agregar_especialidad(self.pediatria)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatria")
        self.assertIn("Pediatria", str(medico))
    
    def test_duplicados_especialidad(self):
        medico = Medico("Dr. Matias Silva", "MAT98765")
        medico.agregar_especialidad(self.pediatria)
        with self.assertRaises(ValueError):
            medico.agregar_especialidad(self.pediatria)
    
    def test_especialidad_para_dia_disponible(self):
        medico = Medico("Dr. Laura Gomez", "MAT45678")
        medico.agregar_especialidad(self.pediatria)
        medico.agregar_especialidad(self.cardiologia)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatria")
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiologia")
        self.assertIsNone(medico.obtener_especialidad_para_dia("sabado"))
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Medico("", "MAT33333")
    
    def test_matricula_vacia(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Nicolas Torres", "")
    
    def test_str_con_especialidades(self):
        medico = Medico("Dr. Patricia Diaz", "MAT55555")
        medico.agregar_especialidad(self.pediatria)
        resultado = str(medico)
        self.assertIn("Dr. Patricia Diaz", resultado)
        self.assertIn("MAT55555", resultado)
        self.assertIn("Pediatria", resultado)
    
    def test_multiples_especialidades_diferentes_dias(self):
        medico = Medico("Dr. Fernando Morales", "MAT99999")
        medico.agregar_especialidad(self.pediatria)
        medico.agregar_especialidad(self.cardiologia)
        
        self.assertEqual(medico.obtener_especialidad_para_dia("miercoles"), "Pediatria")
        self.assertEqual(medico.obtener_especialidad_para_dia("jueves"), "Cardiologia")
        self.assertIsNone(medico.obtener_especialidad_para_dia("domingo"))
    
    def test_matricula_formato_invalido(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Sandra Lopez", "123456")

if __name__ == "__main__":
    unittest.main()