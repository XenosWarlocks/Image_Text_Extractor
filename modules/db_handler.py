import psycopg2

class DBHandler:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()

    def save_results(self, results):
        for file_name, names in results.items():
            for name in names:
                self.cursor.execute(
                    "INSERT INTO extracted_data (file_name, name) VALUES (%s, %s)",
                    (file_name, name)
                )
        self.conn.commit()