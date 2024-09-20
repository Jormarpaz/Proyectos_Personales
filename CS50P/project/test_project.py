import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from io import StringIO
import requests
import project  # Importa tu módulo con las funciones reales

class TestCryptoProject(unittest.TestCase):

    # 1. Prueba de conexión a la base de datos
    def test_conexion_db(self):
        conexion = project.conectar_db()
        self.assertIsInstance(conexion, sqlite3.Connection, "La conexión no es una instancia de sqlite3.Connection")
        conexion.close()

    # 2. Prueba de la función obtener_precio_binance con una respuesta simulada
    @patch('requests.get')  # Simula las llamadas a requests.get
    def test_obtener_precio_binance(self, mock_get):
        # Simular la respuesta de la API
        mock_response = MagicMock()
        mock_response.json.return_value = {'price': '45000.00'}
        mock_get.return_value = mock_response

        # Ejecutar la función y comprobar el resultado
        precio = project.obtener_precio_y_binance('BTCUSDT')
        self.assertEqual(precio, 45000.00, "El precio de Bitcoin debería ser 45000.00")

    # 3. Prueba de la función eliminar_cripto con una base de datos simulada
    @patch('sqlite3.connect')  # Simula la conexión a la base de datos
    def test_eliminar_cripto(self, mock_connect):
        # Crear una simulación de la conexión y el cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        # Simular que la criptomoneda existe en la base de datos
        mock_cursor.fetchone.return_value = [1]

        # Llamar a la función eliminar_cripto
        project.eliminar_cripto('bitcoin')

        # Asegurarse de que se ejecuta el DELETE
        mock_cursor.execute.assert_called_with('DELETE FROM compras WHERE nombre = ?', ('bitcoin',))
        mock_conn.commit.assert_called_once()  # Verificar que se hizo commit
        mock_conn.close.assert_called_once()  # Verificar que se cerró la conexión


if __name__ == '__main__':
    unittest.main()
