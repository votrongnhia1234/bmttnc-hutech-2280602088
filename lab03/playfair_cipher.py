import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_CreateMatrix.clicked.connect(self.call_api_create_matrix)
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text" : self.ui.txtPlainText.toPlainText(),
            "key" : self.ui.txtKey.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtCipherText.setText(data['encrypted_text'])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption successful!")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_create_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {
            "key" : self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                matrix = data['playfair_matrix']
                matrix_str = '\n'.join([' '.join(row) for row in matrix])
                self.ui.txtMatrix.setText(matrix_str)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Matrix created successfully!")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text" : self.ui.txtCipherText.toPlainText(),
            "key" : self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtPlainText.setText(data['decrypted_text'])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption successful!")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)
if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    sys.exit(app.exec_())