import sys
import requests
from pathlib import Path
import pdfplumber
from Persona import Persona
from Vacuna import Vacuna
from Card import Card


def main(args):
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

            # Obtener certificado
            print('Obteniendo certificado...')
            url = f"https://certificados-vacunas.msp.gob.ec/viewpdfcertificadomsp/{p.idencrypt}"
            certificado = requests.get(url)
            filename = Path(f'{p.cedula}.pdf')
            filename.write_bytes(certificado.content)
            print('Certificado descargado!')

            # Obtener QR del certificado
            print('Obteniendo el codigo QR...')
            pdf = pdfplumber.open(f'{p.cedula}.pdf')
            pagina = pdf.pages[0]
            height = pagina.height
            img = pagina.images[0]  # El codigo QR es la primera imagen del documento
            # print(img)
            bbox = (img['x0'] - 1, height - img['y1'], img['x1'] + 1, height - img['y0'] + 1)
            # print(bbox)
            cropped = pagina.crop(bbox)
            img = cropped.to_image(resolution=145)
            img.save('qr.png')
            print('Codigo QR obtenido!')

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
