import sys
import requests
import qrcode
import os
from Persona import Persona
from Vacuna import Vacuna
from Card import Card


def limpeza():
    path = os.getcwd()
    files = os.listdir(path)
    
    for file in files:
        if file.endswith('.png'):
            os.remove(os.path.join(path, file))

def main(args):
    limpeza()
    p = Persona(args[1], args[2])
    # Consultar Datos
    print('Consultando datos...')
    url = 'https://certificados-vacunas.msp.gob.ec/tomapacientemsp'
    data = {"form[identificacion]": p.cedula, "form[fechanacimiento]": p.fechanacimiento}
    try:
        response = requests.post(url=url, data=data)
        response = response.json()['data']

        if bool(response['status']):

            p.nombre = response['datapersona'][0]['nombres']
            p.idencrypt = response['datapersona'][0]['idencrypt']
            for v in response['datavacuna']:
                vac = Vacuna(v['nomvacuna'], v['fechavacuna'], v['dosisaplicada'])
                p.agregarVacuna(vac)
            print('Datos obtenidos!')

            # print(p)

            # Generar codigo QR
            # El codigo QR es la URL para descargar el certificado en formato PDF, el cual usa el idencrypt como parametro
            qr_color = (36, 37, 45)
            print('Generando codigo QR...')
            p.url = f"https://certificados-vacunas.msp.gob.ec/viewpdfcertificadomsp/{p.idencrypt}"
            qr = qrcode.QRCode(
                version=9,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=70,
                border=4
            )
            qr.add_data(p.url)
            qr.make()
            img = qr.make_image(fill_color=qr_color).convert('RGB')
            img.save('qr.png')
            print('Codigo QR generado!')

            # Crear tarjeta
            print('Creando la tarjeta...')
            Card.crear_tarjeta(persona=p)
            print(f'Tarjeta creada: {p.cedula}.png')
        else:
            print(response['message'])
            sys.exit(1)
    except requests.exceptions.ConnectionError:
        print('Connection Error')


if __name__ == '__main__':
    main(sys.argv)
