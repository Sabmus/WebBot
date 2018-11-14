import time
import os
import pyautogui
import datetime
from PIL import ImageGrab
from numpy import *
from selenium import webdriver

# driver de INTERNET EXPLORER
driver = "C:\\Users\\smunoz\\Documents\\Python\\WebBot\\IEDriverServer.exe"

# datos SMU
user_smu = '17596472-K'
pass_smu = 'Rita2018'
url_smu = 'https://b2b.smu.cl//Supermercados/BBRe-commerce/access/login.do'

# datos Cencosud
user_cenco = '166076633'
pass_cenco = 'Rita2033'
url_cenco = 'https://www.cenconlineb2b.com/'

# datos Tottus
user_tottus = 'Rut VSR'
pass_tottus = 'Rita 2020'
url_tottus = 'https://b2b.tottus.com/b2btoclpr/grafica/html/index.html'

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


def smu():
    coord_x1 = 195
    coord_y1 = 556
    coord_x2 = 212
    coord_y2 = 569
    cont = 1
    calendar_coord_smu = {}

    # coordenadas de cajas
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

    # abro IE
    browser = webdriver.Ie(driver)
    browser.get(url_smu)

    time.sleep(7)
    left_click(735, 386)
    time.sleep(0.1)
    pyautogui.typewrite(user_smu, interval=0.05)
    left_click(735, 412)
    time.sleep(0.1)
    pyautogui.typewrite(pass_smu, interval=0.05)
    left_click(711, 440)

    # click para sacar primer pop-up
    time.sleep(25)
    left_click(1076, 132)
    time.sleep(0.25)
    # click en comercial
    left_click(455, 132)
    time.sleep(0.25)
    # click en informe de ventas
    left_click(523, 184)
    time.sleep(10)
    # click para sacar segundo pop-up
    left_click(1076, 132)
    time.sleep(0.25)
    # calendario inicio
    left_click(193, 507)
    time.sleep(0.25)

    if day_cod == 0:  # pregunta si es LUNES
        day = day_number - 4  # si es lunes buscar el Viernes
    else:
        day = day_number - 2  # sino, busca el día anterior
        print('dia buscado: ', day)

    box = ''
    quitar_blanco1 = '(255, 255, 255), '
    quitar_blanco2 = ', (255, 255, 255)'
    quitar_azul1 = '(168, 198, 238), '
    quitar_azul2 = ', (168, 198, 238)'

    map = open('mapeo_pix/' + str(day) + '.txt', 'r')
    pix_buscado = map.read()
    print('pixel buscado: \n')
    print(pix_buscado)
    print('\n\n')

    # Magia
    if day <= 15:
        for k, v in calendar_coord_smu.items():
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
        for k, v in sorted(calendar_coord_smu.items(), key=lambda vector: int(vector[0]), reverse=True):
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

    x = calendar_coord_smu.get(box)[0] + 3  # primera coordenada
    y = calendar_coord_smu.get(box)[1] + 3  # segunda coordenada
    left_click(x, y)
    time.sleep(0.5)

    # generar informe
    left_click(423, 619)
    time.sleep(12)

    # descargar informe
    left_click(1163, 279)
    time.sleep(0.5)

    # CSV
    #left_click(606, 420)
    #time.sleep(2)

    # Excel
    #left_click(606, 463)
    #time.sleep(2)

    # seleccionar
    left_click(683, 502)
    time.sleep(3)

    # boton guardar
    left_click(633, 500)
    time.sleep(5)

    # click en url del explorador de windows
    left_click(371, 47)
    time.sleep(0.25)

    pyautogui.typewrite('C:\WebBot\SMU', interval=0.01)
    pyautogui.press('enter')

    # click en nombre del explorador de windows
    #left_click(614, 342)
    #time.sleep(0.5)

    #pyautogui.typewrite('archivo_' + str(int(time.time())), interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')

    # guardar en pc
    #left_click(513, 447)
    #time.sleep(2)

    # cerrar
    time.sleep(0.25)
    left_click(731, 500)

    # cerrar sesión
    left_click(1350, 132)


def main():
    smu()


if __name__ == '__main__':
    main()
