import sys
import os
import ctypes
from PyQt5 import QtWidgets, QtCore
from src.controllers.login_controller import LoginController
from seed_database import seed_database

def main():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(0)
    except Exception:
        pass
    
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"

    app = QtWidgets.QApplication(sys.argv)

    if not seed_database():
        print("[WARN] El seeding no se completó al 100%. Revise la consola.")

    login = LoginController()
    login.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()