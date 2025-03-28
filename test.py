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


def cancelDocument(document):
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
            failed_documents.append(document)
            return False
    else:
        print("no se encontro el search ")
        time.sleep(1)
        cancelDocument(document)




documents = ["J000231025", "J000231376", "J000231403", "J000232774", "J000233097", "J000233623", "J000233692", "J000233792", "J000233865", "J000234062", "J000234241", "J000234271", "J000234285", "J000234392", "J000234411", "J000234556", "J000234601", "J000234651", "J000234700", "J000234769", "J000234819", "J000234896", "J000235065", "J000235089", "J000235263", "J000235334", "J000235358", "J000235378", "J000235436", "J000235448", "J000235466", "J000235518", "J000235617", "J000235650", "J000235665", "J000235680", "J000235750", "J000235755", "J000235779", "J000235804", "J000235805", "J000235846", "J000235868", "J000235923", "J000235943", "J000235949", "J000235971", "J000236020", "J000236103", "J000236135", "J000236172", "J000236306", "J000236406", "J000236449", "J000236498", "J000236539", "J000236657", "J000236662", "J000236740", "J000236743", "J000236754", "J000236790", "J000236838", "J000236854", "J000236949", "J000237049", "J000237053", "J000237057", "J000237136", "J000237163", "J000237209", "J000237227", "J000237250", "J000237257", "J000237284", "J000237321", "J000237378", "J000148487", "J000148488"];

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