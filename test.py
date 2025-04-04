import pyautogui
import time
import sys

def valideScreen(image, program, exit=False, concidence = 0.3):
    try:
        alert_location = pyautogui.locateOnScreen(image, confidence=concidence)
    except Exception as e:
        print(f"Error al buscar la imagen: {e}", program)
        if exit:
            sys.exit(e)
        return False

    if not alert_location:
        if exit:
            sys.exit("Imagen no encontrada.",program)
        else:
            return False
    else:
        print("Se encuentra abierto", program)
        return True


def cancelDocument(document, attempts=0, store=None ):
    if attempts <= 2:

        time.sleep(1)
        pyautogui.hotkey('ctrl', '2')
        time.sleep(2)
        if valideScreen(image_search, "Search"):
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(document)

            if(store):
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.write(store)

            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            return alertCancel(attempts)
        else:
            print("no se encontro el search ")

            time.sleep(1)
            attempts += 1
            cancelDocument(document, attempts)
    else:
        print("No se pudo cancelar el documento después de varios intentos.")
        return False


def alertCancel(attempts = 0):
    if attempts <= 2:
        pyautogui.hotkey('ctrl', '8')
        time.sleep(1)
        # ya cancelado
        if valideScreen(image_pos, "POS", 0, 0.4 ):
            # press tecla N
            time.sleep(1)
            pyautogui.press('enter')
            return True

        if valideScreen(image_cancel, "Cancelación"):
            pyautogui.press('tab')
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            if valideScreen(image_regenerate, "Regenerar",0, 0.4):
                # press tecla N
                time.sleep(1)
                pyautogui.press('n')
                time.sleep(1)

            time.sleep(2)
            return True
        else:

            time.sleep(1)
            attempts += 1
            alertCancel( attempts)
    else:
        print("No se pudo cancelar el documento después de varios intentos.")
        return False



documents = ["J000047217", "J000047237", "J000047239", "J000047247", "J000047249", "J000047250", "J000047251", "J000047253", "J000047254", "J000047256", "J000094739", "J000095153", "J000096133", "J000096621", "J000096629", "J000096778", "J000096861", "J000096950", "J000097199", "J000097200", "J000097202", "J000097327", "J000097333", "J000097339", "J000097480", "J000097504", "J000097717", "J000098421", "J000098454", "J000098487", "J000099195", "J000100483", "J000101001", "J000101860", "J000102041", "J000102137", "J000102171", "J000102496", "J000102886", "J000103073", "J000103517", "J000103560", "J000103564", "J000103569", "J000103787", "J000103969", "J000103971", "J000103973", "J000103974", "J000103975", "J000103976", "J000103977", "J000103978", "J000103979", "J000103980", "J000103981", "J000103983", "J000103984", "J000104377", "J000104379", "J000104380", "J000104382", "J000104383", "J000104748", "J000104839", "J000104844", "J000104845", "J000104941", "J000104943", "J000104945", "J000104976", "J000105309", "J000105592", "J000106062", "J000106114", "J000106135", "J000106138", "J000106141", "J000106143", "J000106352", "J000106354", "J000106357", "J000106467", "J000106477", "J000106785", "J000106885", "J000106890", "J000106892", "J000106894", "J000106897", "J000106898", "J000107050", "J000107051", "J000107052", "J000107054", "J000107149", "J000107173", "J000107387", "J000107503", "J000107744", "J000108025", "J000108067", "J000108078", "J000108089", "J000108104", "J000108167", "J000108186", "J000108201", "J000108209", "J000108235", "J000108246", "J000108283", "J000108321", "J000108325", "J000108366", "J000108383", "J000108397", "J000108405", "J000108410", "J000108422", "J000108431", "J000108432", "J000108464", "J000108500", "J000108516", "J000108549", "J000108724", "J000108727", "J000108729", "J000108733", "J000108734", "J000108735", "J000108738", "J000108741", "J000108753", "J000108798", "J000108799", "J000108866", "J000108868", "J000108869", "J000108871", "J000108872", "J000108888", "J000109037", "J000109084", "J000109085", "J000109086", "J000109087", "J000109286", "J000109332", "J000109377", "J000109378", "J000109390", "J000109460", "J000109498", "J000109558", "J000109639", "J000109640", "J000109641", "J000109654", "J000109693", "J000109716", "J000109718", "J000109827", "J000109829", "J000109832", "J000109834", "J0190579", "J0190580", "J0190581", "J0190582", "J0190583", "J0190584", "J0190585", "J061000181"];
stores = ["911", "023", "059", "018", "001", "025", "911", "023", "025", "911", "032", "032", "028", "032", "028", "032", "028", "028", "032", "032", "032", "032", "032", "032", "032", "034", "028", "028", "032", "032", "028", "032", "032", "027", "032", "032", "032", "032", "032", "028", "027", "028", "028", "028", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "028", "028", "028", "032", "032", "032", "028", "028", "027", "032", "028", "032", "032", "032", "032", "028", "028", "028", "028", "027", "028", "032", "032", "032", "032", "032", "032", "028", "028", "028", "028", "028", "027", "028", "028", "027", "028", "028", "028", "032", "032", "027", "100", "032", "032", "032", "032", "032", "027", "028", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "032", "028", "028", "028", "028", "028", "028", "028", "028", "032", "032", "032", "028", "028", "028", "028", "028", "025", "027", "032", "032", "032", "032", "032", "028", "032", "032", "032", "032", "032", "032", "028", "032", "028", "032", "032", "032", "032", "028", "032", "032", "032", "026", "026", "026", "026", "026", "026", "026", "026"]

failed_documents = []
image_cancel = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\cancel.png"
image_search = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\search.jpg"
image_pos = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\pos.jpg"
image_regenerate = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\images\alerts\regenerar.jpg"
file_path = r"C:\Users\TIENDA\Desktop\AMS\manipulate-rdp\failed_documents.txt"


print('inicio de proceso...')
print('Cambiar a ventana Proscai, por favor, no tocar el mouse o teclado')
time.sleep(5)

for indice, document in enumerate(documents):
    time.sleep(1)
    if cancelDocument(document, 0, stores[indice]):
        print('Documento cancelado', document)
    else:
        failed_documents.append(document)
        print('Error al cancelar documento', document)
        print('Continuando con el siguiente...')
        pyautogui.press('enter')
    time.sleep(5)


print("Proceso finalizado.")
try:
    with open(file_path, 'w') as file:
        for document in failed_documents:
            file.write(f"{document}\n")
    print(f"Documentos fallidos exportados a {file_path}")
except Exception as e:
    print(f"Error al exportar los documentos: {e}")