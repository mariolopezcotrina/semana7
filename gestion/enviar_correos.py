from os import environ
from django.core.mail import send_mail

def enviar_correo_validacion(usuario_email):
    return send_mail(
        subject='Por favor verifica tu correo',
        message= 'Hola, bienvenido a la aplicaion de intercambio',
        from_email=environ.get('EMAIL_USERNAME'),
        recipient_list=[usuario_email],
        fail_silently=False
        )