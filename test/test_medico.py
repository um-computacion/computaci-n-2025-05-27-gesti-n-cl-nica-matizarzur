import unittest
from src.models.medico import Medico
from src.models.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_crear_medico(self):
        medico = Medico("Dr. Matias Zarzur", "MAT001")
        self.assertEqual(medico.obtener_matricula(), "MAT001")
        self.assertIn("Dr. Matias Zarzur", str(medico))
        self.assertIn("MAT001", str(medico))
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Medico("", "MAT001")
    
    def test_matricula_vacia(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Matias Zarzur", "")
    
    def test_matricula_mal(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Matias Zarzur", "123")
    
    def test_agregar_especialidad(self):
        medico = Medico("Dr. Matias Zarzur", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        self.assertEqual(len(medico.especialidades), 1)
        self.assertEqual(medico.especialidades[0].nombre, "Cardiología")
    
    def test_especialidad_duplicada(self):
        medico = Medico("Dr. Matias Zarzur", "MAT001")
        especialidad = Especialidad("Cardiología", ["lunes", "miercoles"])
        medico.agregar_especialidad(especialidad)
        with self.assertRaises(ValueError):
            medico.agregar_especialidad(especialidad)
    
    def test_str(self):
        medico = Medico("Dr. Matias Zarzur", "MAT001")
        resultado = str(medico)
        self.assertIn("Dr. Matias Zarzur", resultado)
        self.assertIn("MAT001", resultado)

if __name__ == "__main__":
    unittest.main()