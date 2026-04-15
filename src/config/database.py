import pyodbc
import os

class ConnectionProxy:
    """
    Un 'escudo' que envuelve la conexión real a la base de datos.
    Atrapa las llamadas de model a conn.close() y las ignora, 
    permitiéndonos re-utilizar la misma conexión en toda la app 
    sin que ningún modelo la corte accidentalmente.
    """
    def __init__(self, real_conn):
        self.__dict__['_conn'] = real_conn
        
    def close(self):
        # Ignoramos la desconexión para no perder el milisegundo de reconexión
        pass
        
    def __getattr__(self, name):
        return getattr(self._conn, name)
        
    def __setattr__(self, name, value):
        if name == '_conn':
            super().__setattr__(name, value)
        else:
            setattr(self._conn, name, value)

class Database:
    def __init__(self):
        self.server = os.getenv('DB_SERVER', r'EDEN_SOLIS\SQLEXPRESS04') 
        self.database = os.getenv('DB_NAME', 'HotelDB')
        self.username = os.getenv('DB_USER', None)
        self.password = os.getenv('DB_PASS', None)
        self.driver = '{ODBC Driver 17 for SQL Server}'
        
        # Guardaremos la conexión maestra aquí
        self._persistent_conn = None

    def get_connection(self):
        try:
            # 1. ¿Tenemos una conexión activa ya cacheada?
            if self._persistent_conn:
                try:
                    # Validar si sigue viva con un ping ínfimo a la DB
                    cursor = self._persistent_conn.cursor()
                    cursor.execute("SELECT 1")
                    # Devolvemos el escudo falso para que nadie la mate con .close()
                    return ConnectionProxy(self._persistent_conn)
                except Exception:
                    # Se desconectó/timeout, forzamos reanudarla
                    self._persistent_conn = None
            
            # 2. No había conexión viva, creamos el TCP y validación costosa (0.5 a 1.5s)
            if self.username and self.password:
                conn_str = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
            else:
                conn_str = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;'
            
            self._persistent_conn = pyodbc.connect(conn_str)
            
            # 3. Devolvemos la conexión a través de la caja fuerte iterativa
            return ConnectionProxy(self._persistent_conn)
            
        except Exception as e:
            print(f"[!] FALLA DE CONEXIÓN A BASE DE DATOS: {e}")
            return None

    def test_connection(self):
        print(f"Iniciando prueba de conexión a {self.server}...")
        conn = self.get_connection()
        if conn:
            print("Conexión exitosa y anclada al Proxy Pool.")
            return True
        print("La conexión falló.")
        return False

# Solo instanciamos db central.
db = Database()