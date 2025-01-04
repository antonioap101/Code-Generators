import unittest
from api.crud.src.generator.SQL.mysql.MySQLGenerator import MySQLGenerator
from api.crud.src.parsing.components.TableModel import TableModel
from api.crud.src.parsing.components.FieldModel import FieldModel
from api.crud.src.parsing.constants.types.type_mapper import TypeEnum


class TestMySQLGenerator(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        self.table = TableModel(
            name="users",
            fields=[
                FieldModel(name="id", type=TypeEnum.NUMBER, primaryKey=True, autoIncrement=True, nullable=False),
                FieldModel(name="name", type=TypeEnum.TEXT, nullable=False, unique=False),
                FieldModel(name="email", type=TypeEnum.TEXT, nullable=False, unique=True),
                FieldModel(name="age", type=TypeEnum.NUMBER, nullable=True)
            ]
        )
        self.generator = MySQLGenerator(self.table)

    def test_generate_create_table(self):
        """
        Prueba para validar la consulta CREATE TABLE.
        """
        expected_query = (
            "CREATE TABLE users (\n"
            "  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\n"
            "  name VARCHAR({length}) NOT NULL,\n"
            "  email VARCHAR({length}) NOT NULL UNIQUE,\n"
            "  age INT\n"
            ");"
        )
        self.assertEqual(self.generator.generate_create_table(), expected_query)

    def test_generate_insert(self):
        """
        Prueba para validar la consulta INSERT.
        """
        expected_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s);"
        self.assertEqual(self.generator.generate_insert(), expected_query)

    def test_generate_select(self):
        """
        Prueba para validar la consulta SELECT.
        """
        expected_query = "SELECT * FROM users WHERE id = %s;"
        self.assertEqual(self.generator.generate_select(), expected_query)

    def test_generate_update(self):
        """
        Prueba para validar la consulta UPDATE.
        """
        expected_query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s;"
        self.assertEqual(self.generator.generate_update(), expected_query)

    def test_generate_delete(self):
        """
        Prueba para validar la consulta DELETE.
        """
        expected_query = "DELETE FROM users WHERE id = %s;"
        self.assertEqual(self.generator.generate_delete(), expected_query)


if __name__ == "__main__":
    unittest.main()
