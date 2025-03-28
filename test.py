import pyautogui
import time
import sys

def valideScreen(image, program, exit=False):
    try:
        alert_location = pyautogui.locateOnScreen(image, confidence=0.4)
    except Exception as e:
        print(f"Error al buscar la imagen: {e}")
        if exit:
            sys.exit(e)
        return False

    if not alert_location:
        if exit:
            sys.exit("Imagen no encontrada.")
        else:
            return False
    else:
        print("Se encuentra abierto", program)
        return True


def cancelDocument(document, attempts=0):
    if attempts <= 2:

        time.sleep(2)
        pyautogui.hotkey('ctrl', '2')
        time.sleep(2)
        if valideScreen(image_search, "Cancelación"):
            time.sleep(2)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(document)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('ctrl', '8')
            time.sleep(3)
            if valideScreen(image_cancel, "Cancelación"):
                pyautogui.press('tab')
                pyautogui.press('space')
                pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(2)
                return True
            else:
                pyautogui.press('escape')
                time.sleep(1)
                attempts += 1
                cancelDocument(document, attempts)

        else:
            print("no se encontro el search ")
            pyautogui.press('escape')
            time.sleep(1)
            attempts += 1
            cancelDocument(document, attempts)
    else:
        print("No se pudo cancelar el documento después de varios intentos.")
        return False




documents = ["J000232774", "J000233623", "J000233692", "J000234062", "J000234271", "J000234285", "J000234392", "J000234411", "J000234556", "J000234700", "J000234896", "J000235089", "J000235263", "J000235334", "J000235358", "J000235378", "J000235436", "J000235750", "J000235779", "J000235868", "J000235943", "J000235949", "J000236020", "J000236172", "J000236306", "J000236662", "J000236754", "J000236790", "J000237049", "J000237057", "J000237227", "J000237250", "J000237284", "J000237378", "J000148487", "J000148488"]

failed_documents = []
image_cancel = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\cancel.png"
image_search = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\search.jpg"
file_path = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\failed_documents.txt"

print('inicio de proceso...')
print('Cambiar a ventana Proscai, por favor, no tocar el mouse o teclado')
time.sleep(5)

for document in documents:
    time.sleep(1)
    if cancelDocument(document):
        print('Documento cancelado', document)
    else:
        failed_documents.append(document)
        print('Error al cancelar documento', document)
        print('Continuando con el siguiente...')
        pyautogui.press('enter')


print("Proceso finalizado.")
try:
    with open(file_path, 'w') as file:
        for document in failed_documents:
            file.write(f"{document}\n")
    print(f"Documentos fallidos exportados a {file_path}")
except Exception as e:
    print(f"Error al exportar los documentos: {e}")