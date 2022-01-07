# CovidCertificateGen
Programa en Python para generar un certificado de vacunacion de COVID-19. Aplica para Ecuador.

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
