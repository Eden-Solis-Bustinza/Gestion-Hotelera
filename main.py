import sys
import os
import ctypes
from PyQt5 import QtWidgets, QtCore
from src.controllers.login_controller import LoginController
from seed_database import seed_database

def main():
    # 0. Solución de Windows pura para laptops (Asus, etc.) con escalado 125/150%
    # Si le decimos a Windows que nuestra app NO es DPI Aware (Valor 0),
    # Windows se encarga de estirar toda la ventana como si fuese una imagen.
    # El layout no se romperá nunca más, conservando la proporción perfecta.
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(0)
    except Exception:
        pass
    
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"

    # 1. Se inicializa el motor gráfico principal
    app = QtWidgets.QApplication(sys.argv)

    # 2. Verificar e inicializar datos de catálogos en BD
    if not seed_database():
        print("[WARN] El seeding no se completó al 100%. Revise la consola.")

    # 3. El Controlador de Login toma el mando
    login = LoginController()
    login.show()

    # 4. Ciclo de ejecución del sistema
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()