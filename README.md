# CovidCertificateGen
Programa en Python para generar un certificado de vacunacion de COVID-19. Aplica para Ecuador.

## Requisitos
El carnet generado usa la fuente FiraSans, estilo Regular. Fira Sans es una fuente desarrollada por Mozilla. Puede ser descargada de [Github de Mozilla](https://github.com/mozilla/Fira) o [Google Fonts](https://fonts.google.com/specimen/Fira+Sans).

## Instalación

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```
python app.py <NumeroDeCedula> <FechaDeNacimiento>
```

Ejemplo:

```
python app.py 1760000000 1990-01-01
```

Este programa descarga los certificados del sitio oficial del Ministerio de Salud Publica del Ecuador: https://certificados-vacunas.msp.gob.ec/
