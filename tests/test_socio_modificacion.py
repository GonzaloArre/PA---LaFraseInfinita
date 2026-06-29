import json
import os
import tempfile
import unittest

import LaFraseInfinita.Biblio.People.Socio as socio_module


class SocioModificacionTests(unittest.TestCase):
    def setUp(self):
        self.original_db_path = socio_module.DB_PATH
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.temp_file.close()
        socio_module.DB_PATH = self.temp_file.name

    def tearDown(self):
        socio_module.DB_PATH = self.original_db_path
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_modificar_persiste_en_archivo(self):
        socio = socio_module.Socio("Ana", "López", "01/01/2000", "111", "ana@test.com", "123", "Calle 1")
        socio_module.Socio.agregar_socio(socio)

        socio.modificar(nombre="Ana María", dni="456")

        with open(self.temp_file.name, "r", encoding="utf-8") as archivo:
            socios = json.load(archivo)

        self.assertEqual(len(socios), 1)
        self.assertEqual(socios[0]["nombre"], "Ana María")
        self.assertEqual(socios[0]["dni"], "456")


if __name__ == "__main__":
    unittest.main()
