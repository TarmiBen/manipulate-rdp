import subprocess
import pyautogui
import time
import sys
from dotenv import load_dotenv
import os

def firstAlert():
    alert_image1 = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\alert1.png"
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
    alert_image2 = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\alert2.png"
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
        alert_location = pyautogui.locateOnScreen(image, confidence=0.6)
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
    image_proscai = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\proscai.png"
    login_image = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\login.png"
    inside_proscai_image = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\insideProscai.png"

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

    else:
        print("Pantalla de Proscai no detectada, reintentando...")
        time.sleep(3)

def cancelDocument(document):
    pyautogui.hotkey('ctrl', '2')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(document)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', '8')
    time.sleep(1)
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

rdp_file = r"C:\Users\SAN BENI\Desktop\QRY.rdp"
user = os.getenv("USER")
password = os.getenv("PASSWORD")

documents = [
    "J000179755", "J000203767", "J000212039", "J000212055", "J000212079",
    "J000212083", "J000212195", "J000212205", "J000212256", "J000212307", "J000212321",
    "J000212323", "J000212332", "J000212373", "J000212375", "J000212382", "J000212403",
    "J000212421", "J000212425", "J000212437", "J000212442", "J000212548", "J000212606",
    "J000212613", "J000212629", "J000212660", "J000212665", "J000212720", "J000212729",
    "J000212739", "J000212801", "J000212843", "J000212855", "J000212869", "J000212975",
    "J000212995", "J000213075", "J000213083", "J000213190", "J000213217", "J000213229",
    "J000213267", "J000213269", "J000213296", "J000213299", "J000213347", "J000213362",
    "J000213363", "J000213391", "J000213393", "J000213475", "J000213521", "J000213570",
    "J000213580", "J000213591", "J000213659", "J000213665", "J000213680", "J000213687",
    "J000213707", "J000213714", "J000213725", "J000213763", "J000213805", "J000213841",
    "J000213877", "J000213907", "J000214001", "J000214019", "J000214021", "J000214054",
    "J000214065", "J000214067", "J000214079", "J000214150", "J000214198", "J000214206",
    "J000214259", "J000214277", "J000214379", "J000214382", "J000214390", "J000214421",
    "J000214443", "J000214458", "J000214488", "J000214519", "J000214536", "J000215623",
    "J000216979", "J000218687", "J000218833", "J000222336", "J000224198", "J000246620",
    "J000247049", "J000247551", "J000247719", "J000247802", "J000247943", "J000248004",
    "J000256971", "J000262034", "J000263434", "J000266218", "J000266857", "J000268746",
    "J000270020", "J000271387", "J000272089", "J000272674", "J000272676", "J000272679",
    "J000272680", "J000272681", "J000272683", "J000272684", "J000272729", "J000272750",
    "J000273281", "J000273413", "J000274430", "J000274498", "J000274578", "J000274880",
    "J000275034", "J000275268", "J000275328", "J000275357", "J000275359", "J000275402",
    "J000275403", "J000275444", "J000276084", "J000276170", "J000276710", "J000277013",
    "J000277245", "J000277246", "J000277563", "J000277567", "J000277748", "J000277918",
    "J000277957", "J000277962", "J000277993", "J000278026", "J000278191", "J000278201",
    "J000278204", "J000278319", "J000278344", "J000278497", "J000278538", "J000278582",
    "J000278584", "J000278698"
]
failed_documents = []


subprocess.Popen(["mstsc", "/f", rdp_file])
time.sleep(2)
firstAlert()
time.sleep(2)
secondAlert()
time.sleep(5)

# OPEN PROSCAI valide inside
image_desktoop = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\escritorio.png"
image_cancel = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\images\alerts\cancel.png"
file_path = r"C:\Users\SAN BENI\PycharmProjects\manipulatorProscai\failed_documents.txt"
valideScreen(image_desktoop, "Escritorio")
time.sleep(2)

if insideProscai(user, password):
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









