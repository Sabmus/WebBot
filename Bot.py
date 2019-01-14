import time
import os
import pyautogui
import datetime
import shutil
import schedule
import csv
from PIL import ImageGrab
from numpy import *
from selenium import webdriver
from pyunpack import Archive


pyautogui.FAILSAFE = False  # disables the fail-safe
# driver de INTERNET EXPLORER
ie_driver = "C:\\Users\\smunoz\\Documents\\Python\\WebBot\\IEDriverServer.exe"
chrome_driver = "C:\\Users\\smunoz\\Documents\\Python\\WebBot\\chromedriver.exe"

# datos SMU
user_smu = '17596472-K'
pass_smu = 'Rita2018'
url_smu = 'https://b2b.smu.cl//Supermercados/BBRe-commerce/access/login.do'
ruta_archivo_smu = 'M:\WebBot\SMU'
ruta_pix_smu = 'mapeo_pix_smu/'

# datos Cencosud
user_cenco = '166076633'
pass_cenco = 'Rita2033'
url_cenco = 'https://www.cenconlineb2b.com/'
ruta_archivo_cenco = 'M:\WebBot\Cenco'
ruta_pix_cenco = 'mapeo_pix_cenco/'

# datos Tottus
rut_empresa = '86547900k'
user_tottus = '166076633'
pass_tottus = 'Rita2033'
url_tottus = 'https://b2b.tottus.com/b2btoclpr/grafica/html/index.html'
ruta_archivo_tottus = 'M:\WebBot\Tottus'
ruta_pix_tottus = 'mapeo_pix_tottus/'

# datos Walmart
user_wmt = 'Soc439a'
pass_wmt = 'Vodkaskyy75'
url_wmt = 'https://rllogin.wal-mart.com/rl_security/rl_logon.aspx?ServerType=IIS1&CTAuthMode=BASIC&language=en&CT_ORIG_URL=%2F&ct_orig_uri=%2F'
url_wmt_dl = 'https://retaillink.wal-mart.com'
ruta_archivo_wallmart = 'M:\WebBot\Wallmart'

now = datetime.datetime.now()
day_number = now.day
day_cod = time.gmtime().tm_wday  # 0 = Lunes
print(now)
print(day_number)
print(day_cod)


def left_click(x, y):
    pyautogui.click(x, y)
    time.sleep(1)


# recibe box=(x1, y1, x2, y2)
def screen_grab(box):
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\img\\test' + str(now.date()) + str(box) + '.png', 'PNG')
    return im


def buscadia(coordenadas, ruta, cadena='none', dia='none'):
    #if day_number <= 5:
    #    day = 1
    #else:
    if day_cod == 0:  # pregunta si es LUNES
        day = day_number - 4  # si es lunes buscar el Viernes
    else:
        day = day_number - 2  # sino, busca el día anterior
        print('dia buscado: ', day)

    if dia == 'hoy':
        day = day_number

    box = ''
    quitar_blanco1 = '(255, 255, 255), '
    quitar_blanco2 = ', (255, 255, 255)'
    quitar_azul1 = '(168, 198, 238), '
    quitar_azul2 = ', (168, 198, 238)'
    blanco = (255, 255, 255)
    blanco1 = (250, 250, 250)

    file = ruta + str(day) + '.txt'
    print(file)
    map = open(file, 'r')
    pix_buscado = map.read()
    print('-----------------------------')
    print('pixel buscado: \n')
    print(pix_buscado)
    print('-----------------------------')
    print('\n\n')

    if cadena == 'none':
        # Magia
        if day <= 15:
            for k, v in coordenadas.items():
                print(k)
                im = screen_grab(v)
                pix = [im.getpixel((x, y)) for x in range(0, v[2] - v[0]) for y in range(0, v[3] - v[1])]
                paso1 = str(pix).replace(quitar_blanco1, '')
                paso2 = paso1.replace(quitar_blanco2, '')
                paso3 = paso2.replace(quitar_azul1, '')
                pix = paso3.replace(quitar_azul2, '')
                print(pix)
                if pix == pix_buscado:
                    box = k
                    print('box' + box)
                    break
        elif day > 15:
            for k, v in sorted(coordenadas.items(), key=lambda vector: int(vector[0]), reverse=True):
                print(k)
                im = screen_grab(v)
                pix = [im.getpixel((x, y)) for x in range(0, v[2] - v[0]) for y in range(0, v[3] - v[1])]
                paso1 = str(pix).replace(quitar_blanco1, '')
                paso2 = paso1.replace(quitar_blanco2, '')
                paso3 = paso2.replace(quitar_azul1, '')
                pix = paso3.replace(quitar_azul2, '')
                print(pix)
                if pix == pix_buscado:
                    box = k
                    print('box' + box)
                    break
    if cadena == 'tottus':
        # Magia
        if day <= 15:
            for k, v in coordenadas.items():
                print(k)
                im = screen_grab(v)
                pix = [im.getpixel((x, y)) for x in range(0, v[2] - v[0]) for y in range(0, v[3] - v[1])]
                for pos in range(len(pix)):
                    if pix[pos] == blanco:
                        pix[pos] = blanco1
                    if pix[pos] != blanco1:
                        pix[pos] = (0, 0, 0)
                print(pix)
                if str(pix) == pix_buscado:
                    box = k
                    print('box' + box)
                    break
        elif day > 15:
            for k, v in sorted(coordenadas.items(), key=lambda vector: int(vector[0]), reverse=True):
                print(k)
                im = screen_grab(v)
                pix = [im.getpixel((x, y)) for x in range(0, v[2] - v[0]) for y in range(0, v[3] - v[1])]
                for pos in range(len(pix)):
                    if pix[pos] == blanco:
                        pix[pos] = blanco1
                    if pix[pos] != blanco1:
                        pix[pos] = (0, 0, 0)
                print(pix)
                if str(pix) == pix_buscado:
                    box = k
                    print('encontrado en: box' + box)
                    break

    x = coordenadas.get(box)[0] + 3  # primera coordenada
    y = coordenadas.get(box)[1] + 3  # segunda coordenada
    return x, y


def smu():
    coord_x1 = 195
    coord_y1 = 556
    coord_x2 = 212
    coord_y2 = 569
    cont = 1
    calendar_coord_smu = {}

    # abro IE
    browser = webdriver.Ie(ie_driver)
    browser.get(url_smu)

    time.sleep(20)
    left_click(1016, 449)
    time.sleep(0.25)
    pyautogui.typewrite(user_smu, interval=0.2)
    left_click(1016, 473)
    time.sleep(0.25)
    pyautogui.typewrite(pass_smu, interval=0.2)
    left_click(989, 503)

    # click para sacar primer pop-up
    time.sleep(20)
    left_click(1271, 447)
    time.sleep(5)
    # click en comercial
    left_click(455, 132)
    time.sleep(5)
    # click en informe de ventas
    left_click(523, 184)
    time.sleep(20)
    # click para sacar segundo pop-up
    left_click(1553, 132)
    time.sleep(5)

    if day_number > 5:
        # calendario inicio
        left_click(193, 507)
        time.sleep(0.1)

        for x in range(6):  # 6 líneas de cajas
            for y in range(7):  # 7 cajas por línea
                print(coord_x1, coord_y1, coord_x2, coord_y2)
                linea = {str(cont): (coord_x1, coord_y1, coord_x2, coord_y2)}
                calendar_coord_smu.update(linea)
                cont += 1
                if y % 2 == 0:
                    coord_x1 += 25
                    coord_x2 += 25
                else:
                    coord_x1 += 24
                    coord_x2 += 24
            coord_x1 = 195
            coord_x2 = 212
            coord_y1 += 23
            coord_y2 += 23

        x, y = buscadia(calendar_coord_smu, ruta_pix_smu)
        left_click(x, y)
        time.sleep(0.5)

    # generar informe
    left_click(423, 619)
    time.sleep(20)
    # descargar informe
    #left_click(1717, 279)
    #time.sleep(4)

    left_click(1751, 279)
    time.sleep(20)
    left_click(893, 725)
    time.sleep(20)

    # CSV
    #left_click(883, 576)
    #time.sleep(2)
    # Excel
    #left_click(883, 619)
    #time.sleep(2)
    # seleccionar
    #left_click(963, 658)
    #time.sleep(4)
    # boton guardar
    left_click(911, 655)
    time.sleep(20)

    # click en url del explorador de windows
    left_click(646, 47)
    time.sleep(0.25)
    pyautogui.typewrite(ruta_archivo_smu, interval=0.2)
    pyautogui.press('enter')
    # click en nombre del explorador de windows
    left_click(602, 438)
    time.sleep(0.25)
    pyautogui.typewrite('archivo_' + str(now.date()) + '.rar', interval=0.2)
    time.sleep(0.25)
    pyautogui.press('enter')

    # guardar en pc
    #left_click(513, 447)
    #time.sleep(2)
    # cerrar
    time.sleep(20)
    left_click(1012, 655)
    # cerrar sesión
    time.sleep(0.5)
    left_click(1904, 132)

    #extraigo el rar
    Archive(ruta_archivo_smu + '\\archivo_' + str(now.date()) + '.rar').extractall(ruta_archivo_smu)
    for file in os.listdir(ruta_archivo_smu):
        if file.endswith(".csv"):
            os.rename(os.path.join(ruta_archivo_smu, file), os.path.join(ruta_archivo_smu, 'datos.csv'))

    '''texto = nombre_archivo + '.txt'
    for file in os.listdir(ruta_archivo_smu):
        if file.endswith(".csv"):
            archivo = os.path.join(ruta_archivo_smu, file)
            with open(archivo, 'r') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=' ')
                with open(texto, 'w') as txtfile:
                    for row in csvreader:
                        txtfile.write(','.join(row) + '\n')
                        # print(','.join(row))
                    txtfile.close()
    '''


def cenco():
    coord_x1 = 242
    coord_y1 = 532
    coord_x2 = 259
    coord_y2 = 545
    cont = 1
    calendar_coord_cenco = {}

    browser = webdriver.Ie(ie_driver)
    browser.get(url_cenco)
    #opciones = browser.find_element_by_name('pais').send_keys('chile')

    time.sleep(5)
    # seleccione país
    left_click(1048, 406)
    time.sleep(0.25)
    # seleccione CHILE
    left_click(892, 436)
    time.sleep(0.25)
    # seleccione UN
    left_click(1048, 467)
    time.sleep(0.25)
    # seleccione Supermercados
    left_click(953, 528)
    time.sleep(0.25)
    # Ingresar
    left_click(961, 511)
    time.sleep(3)

    # Login User
    left_click(1037, 423)
    time.sleep(0.25)
    pyautogui.typewrite(user_cenco, interval=0.2)
    #pyautogui.press('enter')
    time.sleep(0.25)
    # Login Paswword
    left_click(1037, 463)
    time.sleep(0.25)
    pyautogui.typewrite(pass_cenco, interval=0.2)
    pyautogui.press('enter')
    time.sleep(12)

    # quita pop-pu
    #left_click(1069, 283)
    time.sleep(0.25)
    # Click en Comercial
    left_click(424, 123)
    time.sleep(0.25)
    # Click en ventas
    left_click(445, 153)
    time.sleep(10)

    if day_number > 5:
        # Click en Calendario
        left_click(240, 482)
        time.sleep(0.25)

        # coordenadas de cajas
        for x in range(6):  # 6 líneas de cajas
            for y in range(7):  # 7 cajas por línea
                print(coord_x1, coord_y1, coord_x2, coord_y2)
                linea = {str(cont): (coord_x1, coord_y1, coord_x2, coord_y2)}
                calendar_coord_cenco.update(linea)
                cont += 1
                if y % 2 == 0:
                    coord_x1 += 25
                    coord_x2 += 25
                else:
                    coord_x1 += 24
                    coord_x2 += 24
            coord_x1 = 242
            coord_x2 = 259
            coord_y1 += 23
            coord_y2 += 23

        x, y = buscadia(calendar_coord_cenco, ruta_pix_cenco)
        left_click(x, y)
        time.sleep(0.5)

    # generar informe
    left_click(426, 582)
    time.sleep(15)
    # descargar informe
    #left_click(1819, 294)
    #time.sleep(3)

    left_click(1887, 251)
    time.sleep(4)
    left_click(893, 689)
    time.sleep(60)

    # CSV
    # left_click(883, 576)
    # time.sleep(2)
    # Excel
    # left_click(883, 619)
    # time.sleep(2)
    # seleccionar
    #left_click(962, 658)
    #time.sleep(5)
    # boton guardar
    left_click(911, 654)
    time.sleep(5)

    # click en url del explorador de windows
    left_click(646, 47)
    time.sleep(0.25)
    pyautogui.typewrite(ruta_archivo_cenco, interval=0.2)
    pyautogui.press('enter')
    # click en nombre del explorador de windows
    left_click(602, 438)
    pyautogui.typewrite('archivo_' + str(now.date()) + '.rar', interval=0.2)
    time.sleep(0.1)
    pyautogui.press('enter')

    # guardar en pc
    # left_click(513, 447)
    # time.sleep(2)
    # cerrar
    time.sleep(0.5)
    left_click(1012, 654)
    # cerrar sesión
    time.sleep(0.5)
    left_click(1888, 124)

    Archive(ruta_archivo_cenco + '\\archivo_' + str(now.date()) + '.rar').extractall(ruta_archivo_cenco)
    for file in os.listdir(ruta_archivo_cenco):
        if file.endswith(".csv"):
            os.rename(os.path.join(ruta_archivo_cenco, file), os.path.join(ruta_archivo_cenco, 'datos.csv'))


def tottus():
    '''
    coord_ini_x1 = 476
    coord_ini_y1 = 348
    coord_ini_x2 = 493
    coord_ini_y2 = 358
    cont_ini = 1
    calendar_coord_tottus_inicio = {}

    coord_fin_x1 = 1059
    coord_fin_y1 = 348
    coord_fin_x2 = 1076
    coord_fin_y2 = 358
    cont_fin = 1
    calendar_coord_tottus_fin = {}
    '''

    browser = webdriver.Ie(ie_driver)
    browser.get(url_tottus)

    time.sleep(5)
    # dropdown
    left_click(1210, 255)
    time.sleep(0.25)
    left_click(1210, 242)
    time.sleep(0.25)
    left_click(1024, 602)
    time.sleep(0.25)
    left_click(1210, 255)
    time.sleep(0.25)
    left_click(1210, 269)
    time.sleep(0.25)

    # Rut Empresa
    pyautogui.doubleClick(1236, 275)
    time.sleep(0.25)
    pyautogui.typewrite(rut_empresa, interval=0.2)
    # Uusario Tottus
    pyautogui.doubleClick(1236, 308)
    time.sleep(0.25)
    pyautogui.typewrite(user_tottus, interval=0.2)
    # Password Tottus
    pyautogui.doubleClick(1236, 340)
    time.sleep(0.25)
    pyautogui.typewrite(pass_tottus, interval=0.2)
    # Ingresar
    left_click(1204, 385)
    time.sleep(5)

    # Ventas
    pyautogui.moveTo(201, 149, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(209, 149, duration=0.5)
    pyautogui.moveTo(209, 293, duration=0.5)
    left_click(209, 293)
    pyautogui.mouseUp()
    time.sleep(10)

    if day_cod == 0:  # pregunta si es LUNES
        fecha = datetime.datetime.today() - datetime.timedelta(days=4)  # si es lunes buscar el Viernes
    else:
        fecha = datetime.datetime.today() - datetime.timedelta(days=2)  # sino, busca el día anterior

    hoy = datetime.datetime.today() - datetime.timedelta(days=1)
    time.sleep(1)
    # Click en Calendario_inicio
    left_click(605, 288)
    time.sleep(0.5)
    pyautogui.typewrite(str(hoy.strftime("%d/%m/%Y")), interval=0.2)
    #pyautogui.typewrite(str(fecha.strftime("%d/%m/%Y")), interval=0.2)

    left_click(1427, 289)
    time.sleep(0.5)
    #hoy = datetime.datetime.today()
    pyautogui.typewrite(str(hoy.strftime("%d/%m/%Y")), interval=0.2)

    # check box
    left_click(561, 309)
    time.sleep(0.25)
    # generar informe
    left_click(964, 338)
    time.sleep(10)
    # descargar informe
    left_click(1265, 1018)
    time.sleep(10)
    #mueve el archivo
    shutil.move('C:/Users/smunoz/Downloads/datos.csv', os.path.join(ruta_archivo_tottus, 'datos.csv'))
    # cerrar
    time.sleep(0.25)
    left_click(1397, 111)


def wallmart():
    browser = webdriver.Chrome(chrome_driver)
    browser.get(url_wmt)

    # mi usuario y doy next
    username = browser.find_element_by_id('txtUser')
    username.send_keys(user_wmt)
    password = browser.find_element_by_id('txtPass')
    password.send_keys(pass_wmt)
    nextButton = browser.find_element_by_id('Login')
    nextButton.click()

    containers = browser.find_elements_by_xpath('//i[@class="icon-download-alt mediumBlueIcon downloadIcon"]')
    print('print containers:\n\n ')
    print(containers)
    print('\n\n')
    url = ''
    for item in containers:
        print(item.get_attribute('id'))
        if 'Sell Out Walmart VSR (Bot Planeamiento-No Borrar)' in item.get_attribute('id'):
            url = url_wmt_dl + item.get_attribute('id')
            print('url: ' + url)
            break

    browser.get(url)
    time.sleep(30)
    pyautogui.hotkey('ctrl', 's')

    # click en url del explorador de windows
    left_click(646, 47)
    time.sleep(0.25)
    pyautogui.typewrite(ruta_archivo_wallmart, interval=0.2)
    pyautogui.press('enter')
    time.sleep(0.25)
    # click en nombre del explorador de windows
    left_click(602, 438)
    # pyautogui.typewrite('archivo_' + str(now.date()) + '.txt', interval=0.2)
    pyautogui.typewrite('datos.txt', interval=0.2)
    time.sleep(0.1)
    pyautogui.press('enter')


def elimina_archivos():
    try:
        os.remove(path=ruta_archivo_wallmart + '\datos.txt')
    except Exception as e:
        print(e)
        pass

    try:
        os.remove(path=ruta_archivo_smu + '\datos.csv')
    except Exception as e:
        print(e)
        pass

    try:
        os.remove(path=ruta_archivo_smu + '\\archivo_' + str(now.date()) + '.rar')
    except Exception as e:
        print(e)
        pass

    try:
        os.remove(path=ruta_archivo_cenco + '\datos.csv')
    except Exception as e:
        print(e)
        pass

    try:
        os.remove(path=ruta_archivo_cenco + '\\archivo_' + str(now.date()) + '.rar')
    except Exception as e:
        print(e)
        pass

    try:
        os.remove(path=ruta_archivo_tottus + '\datos.csv')
    except Exception as e:
        print(e)
        pass


def job():
    print('corriendo Wallmart:')
    try:
        #wallmart()
        print('OK')
    except Exception as e:
        time.sleep(2)
        print('Falló')
        print(e)
        pass

    print('corriendo SMU:')
    try:
        #smu()
        print('OK')
    except Exception as e:
        time.sleep(2)
        print('Falló')
        print(e)
        pass

    print('corriendo Cenco:')
    try:
        #cenco()
        print('OK')
    except Exception as e:
        time.sleep(2)
        print('Falló')
        print(e)
        pass

    print('corriendo Tottus:')
    try:
        #tottus()
        print('OK')
    except Exception as e:
        time.sleep(2)
        print('Falló')
        print(e)
        pass


def job2():
    print('Eliminando archivos:')
    try:
        elimina_archivos()
        print('OK')
    except Exception as e:
        time.sleep(2)
        print('Falló')
        print(e)
        pass


def main():
    '''
    # pasar a TXT
    import csv
    csv_file = raw_input('Enter the name of your input file: ')
    txt_file = raw_input('Enter the name of your output file: ')
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
    
    # scheduler
    https://github.com/dbader/schedule/blob/master/test_schedule.py
    import schedule
    import time

    schedule.every(1).minutes.do(job)
    schedule.every().hour.do(job)

    def job(t):
        print "I'm working...", t
        return
    '''

    schedule.every().day.at("06:00").do(job)
    schedule.every().day.at("07:00").do(job2)

    while True:
        schedule.run_pending()
        print(datetime.datetime.now())
        time.sleep(2)  # wait x = 1 sec


if __name__ == '__main__':
    main()
