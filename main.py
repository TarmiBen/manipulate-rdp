import subprocess
import pyautogui
import time
import sys
from dotenv import load_dotenv
import os

from numpy.ma.core import true_divide


def firstAlert():
    alert_image1 = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\alert1.png"

    try:
        alert_location = pyautogui.locateOnScreen(alert_image1, confidence=0.6)  # Ajusta el nivel de confianza
        if alert_location:
            print("Se detectó la alerta en:", alert_location)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
        else:
            print("No se detectó la alerta1.")
    except pyautogui.ImageNotFoundException:
        print("No se encontró la imagen en la pantalla.")

def secondAlert():
    alert_image2 = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\alert2.png"
    try:
        alert_location = pyautogui.locateOnScreen(alert_image2, confidence=0.6)  # Ajusta el nivel de confianza
        if alert_location:
            print("Se detectó la alerta2 en:", alert_location)
            pyautogui.press('s')
            pyautogui.press('enter')
        else:
            print("No se detectó la alerta.")
    except pyautogui.ImageNotFoundException:
        print("No se encontró la imagen en la pantalla.")

def valideScreen(image, program, exit=False):
    try:
        alert_location = pyautogui.locateOnScreen(image, confidence=0.3)
        if not alert_location:
            if exit:
                sys.exit()
            else:
                return False
        else:
            print("Se encuentra abierto ", program)
            return True
    except pyautogui.ImageNotFoundException:
        if exit:
            sys.exit()
        else:
            return False


def insideProscai(user, password, maxAttempts=10):
    image_proscai = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\proscai.jpg"
    login_image = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\login.png"
    inside_proscai_image = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\insideProscai.png"
    time.sleep(3)
    print("Validando dentro de proscai")
    attempts = 0
    if valideScreen(image_proscai, "Proscai"):
        pyautogui.press('enter')
        time.sleep(2)
        while attempts < maxAttempts:
            attempts += 1
            if valideScreen(login_image, "Login"):
                pyautogui.write(user)
                pyautogui.press('tab')
                pyautogui.write(password)
                pyautogui.press('enter')
                time.sleep(3)

                if valideScreen(inside_proscai_image, "Dentro de proscai"):
                    print("Login exitoso, dentro de Proscai.")
                    pyautogui.press('f4')
                    return True
                else:
                    return False
            else:
                pyautogui.press('enter')
                time.sleep(1)
                print("Pantalla de login no detectada, reintentando...")

        print("Número máximo de intentos alcanzado, abortando.")
        return True

    else:
        print("Pantalla de Proscai no detectada, reintentando...")
        time.sleep(3)

def cancelDocument(document):
    time.sleep(1)
    pyautogui.hotkey('ctrl', '2')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(document)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', '8')
    time.sleep(2)
    if valideScreen(image_cancel, "Cancelación"):
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')
        pyautogui.press('enter')
        return True
    else:
        failed_documents.append(document)
        return False


load_dotenv()

rdp_file = r"C:\Users\TIENDA\Desktop\QRY.rdp"
user = os.getenv("USER")
password = os.getenv("PASSWORD")

documents = [
   "J000235089"
]
failed_documents = []


subprocess.Popen(["mstsc", "/f", rdp_file])

time.sleep(2)
firstAlert()
time.sleep(2)
secondAlert()
time.sleep(5)

# OPEN PROSCAI valide inside
image_desktoop = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\escritorio.png"
image_cancel = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\cancel.png"
file_path = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\manipulatorProscai\failed_documents.txt"


screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

pyautogui.moveTo(center_x, center_y, duration=0.5)
pyautogui.click()

time.sleep(1)
pyautogui.press('p')
pyautogui.press('enter')


time.sleep(1)
print("entrado a proscai")
if insideProscai(user, password):
    time.sleep(1)
    for document in documents:
        if cancelDocument(document):
            print('Documento cancelado', document)
        else:
            response = input('fallo la cancelacion, continuo? 1 ... Si / 0 ...no')
            if response == '0':
                sys.exit()


    print("Proceso finalizado.")
    try:
        with open(file_path, 'w') as file:
            for document in failed_documents:
                file.write(f"{document}\n")
        print(f"Documentos fallidos exportados a {file_path}")
    except Exception as e:
        print(f"Error al exportar los documentos: {e}")









