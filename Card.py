from textwrap import fill
from PIL import Image, ImageDraw, ImageFont


class Card:
    @staticmethod
    def crear_tarjeta(persona):
        # Colores
        blanco = (255, 255, 255)
        negro = (0, 0, 0)
        celeste = (128, 181, 215)
        # Fuentes
        data_persona = ImageFont.truetype('FiraSans-Regular.otf', 36)
        data_dosis = ImageFont.truetype('FiraSans-Regular.otf', 22)
        data_disclaimer = ImageFont.truetype('FiraSans-Regular.otf', 21)
        # Tamaños
        card_size = (600, 1050)  # Vertical
        img_size = (300, 300)
        # Coordenadas
        qr_xy = (150, 340)
        pic_xy = (150, 30, 450, 330)
        # Imagen
        card = Image.new('RGB', card_size, blanco)
        ctx = ImageDraw.Draw(card)
        # Barra celeste
        ctx.rectangle((0, 950, 600, 1050), fill=celeste, outline=None)
        disclaimer = "Esta informacion es meramente informativa.\nPara consultar su validez, escanear el codigo QR."
        w, h = ctx.textsize(disclaimer, font=data_disclaimer)
        ctx.multiline_text((img_size[0]-w/2, 972), disclaimer, fill=blanco, font=data_disclaimer)
        #Datos
        altura = 760
        delta_altura = 35
        ctx.rounded_rectangle(pic_xy, radius=15, outline=(64, 64, 64), fill=(128, 128, 128), width=2)
        qr_path = Image.open('qr.png', 'r').resize((300, 300))
        card.paste(qr_path, qr_xy)
        url = f"{persona.url}"
        w, h = ctx.textsize(url, font=data_persona)
        ctx.text((img_size[0] - w/2, 640), url, fill=negro, font=data_disclaimer)
        nombre = f"{persona.nombre}"
        w, h = ctx.textsize(nombre, font=data_persona)
        ctx.text((img_size[0] - w/2, 660), nombre, fill=negro, font=data_persona)
        cedula = persona.cedula
        w, h = ctx.textsize(cedula, font=data_persona)
        ctx.text((img_size[0] - w/2, 715), cedula, fill=negro, font=data_persona)
        for item in persona.vacunas:
            dosis = f"Dosis {item.dosis}: {item.nombre} {item.fecha}"
            w, h = ctx.textsize(dosis, font=data_dosis)
            ctx.text((img_size[0] - w/2, altura), dosis, fill=negro, font=data_dosis)
            altura += delta_altura
        card.save(f"{persona.cedula}.png")
