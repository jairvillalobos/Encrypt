import sys
from crypt_ui import * 
from PyQt5.QtWidgets import *
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QMessageBox


class Ventana_principal(QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_genera_clave.clicked.connect(self.generate_clave)
        self.ui.btn_encriptar.clicked.connect(self.encrypt)
        self.ui.btn_desencriptar.clicked.connect(self.de_encrypt)
        self.nom_archivo = "web-site.jpg"

    def generate_clave(self):
        self.clave = Fernet.generate_key()
        print(self.clave)
        with open('clave-generada/clave.key', 'wb') as archivo_clave:
            archivo_clave.write(self.clave)
            print("clave generada exitosamente")

    def charge_clave(self):
        #print("clave cargada exitosamente")
        return open('clave-generada/clave.key', 'r').read()

    def encrypt(self):
        try:
            f = Fernet(self.charge_clave())
            with open (self.nom_archivo, 'rb') as file:
                self.info_archivo = file.read()
            self.data_encrypted = f.encrypt(self.info_archivo)
            with open (self.nom_archivo , 'wb') as file:
                file.write(self.data_encrypted)
        except Exception as e:
            print(e)

    def de_encrypt(self):
        try:
            f = Fernet(self.charge_clave())
            with open (self.nom_archivo, 'rb') as file:
                self.data_encrypted = file.read()
            self.data_decrypted = f.decrypt(self.data_encrypted)
            with open (self.nom_archivo , 'wb') as file:
                file.write(self.data_decrypted)
        except Exception as e:
            print(e)

    
    
if __name__ == "__main__":
        aplicacion_condesadora = QApplication(sys.argv)
        app = Ventana_principal()
        app.show()
        sys.exit(aplicacion_condesadora.exec_())