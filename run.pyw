import sys
import os
from crypt_ui import *
from PyQt5.QtWidgets import *
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QMessageBox


class Ventana_principal(QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()  # Obtener la ubicación actual del archivo del programa
        self.ui.btn_genera_clave.clicked.connect(self.generate_clave)
        self.ui.btn_encriptar.clicked.connect(self.encrypt)
        self.ui.btn_desencriptar.clicked.connect(self.de_encrypt)
        self.ui.btn_buscar_archivo.clicked.connect(self.slot_btn_chooseFile)

    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "Seleccione Archivo",
                                                                self.cwd,  # Ruta de inicio
                                                                "All Files (*);;Text Files (*.txt)")   # Establecer el filtrado de la extensión de archivo, usar intervalo de punto y coma doble

        self.nom_archivo = fileName_choose  # asigna el monbre del archivo

        if fileName_choose == "":
            print("\nCancelar selección")

        #print("\ nEl archivo que seleccionó es:")
        #print(self.nom_archivo)
        #print("Tipo de filtro de archivo:", filetype)

    def generate_clave(self):
        self.clave = Fernet.generate_key()
        #print(self.clave)
        with open('clavegenerada/clave.key', 'wb') as archivo_clave:
            archivo_clave.write(self.clave)
            #print("clave generada exitosamente")

    def charge_clave(self):
        #print("clave cargada exitosamente")
        return open('clavegenerada/clave.key', 'r').read()

    def encrypt(self):
        try:
            f = Fernet(self.charge_clave())
            with open(self.nom_archivo, 'rb') as file:
                self.info_archivo = file.read()
            self.data_encrypted = f.encrypt(self.info_archivo)
            with open(self.nom_archivo, 'wb') as file:
                file.write(self.data_encrypted)
                def sms_encipted(self):
                    msgBox = QMessageBox(QMessageBox.NoIcon, 'Archivo','¡Encriptado Correctamente!')
                    msgBox.exec()
            sms_encipted(self)
        except Exception as e:
            print(e)

    def de_encrypt(self):
        try:
            f = Fernet(self.charge_clave())
            with open(self.nom_archivo, 'rb') as file:
                self.data_encrypted = file.read()
            self.data_decrypted = f.decrypt(self.data_encrypted)
            with open(self.nom_archivo, 'wb') as file:
                file.write(self.data_decrypted)
                def sms_de_encripted(self):
                    msgBox = QMessageBox(QMessageBox.NoIcon, 'Archivo','¡Desencriptado!')
                    msgBox.exec()
            sms_de_encripted(self)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    aplicacion_condesadora = QApplication(sys.argv)
    app = Ventana_principal()
    app.show()
    sys.exit(aplicacion_condesadora.exec_())
