import unittest
from modules.db_handler import DBHandler
import psycopg2

class TestDBHandler(unittest.TestCase):
    def setUp(self):
        # Test database config
        db_config = {
            "database": "test_db",
            "user": "user",
            "password": "password",
            "host": "localhost",
            "port": 5432
        }
        self.db_handler = DBHandler(db_config)
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS extracted_data (file_name TEXT, name TEXT);")
        self.conn.commit()

    def tearDown(self):
        self.cursor.execute("DROP TABLE IF EXISTS extracted_data;")
        self.conn.commit()
        self.conn.close()
    
    def test_save_results(self):
        results = {
            "file1.png": ["John Doe", "Alice Smith"],
            "file2.pdf": ["Bob Johnson"]
        }
        self.db_handler.save_results(results)
        self.cursor.execute("SELECT * FROM extracted_data;")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 3)