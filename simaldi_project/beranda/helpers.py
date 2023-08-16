from django.core.mail import send_mail
from django.conf import settings

def send_lupa_password_mail(email, token):
    subject = 'SIMALDI Link Ubah Password'
    message = f'Klik link untuk mereset password kamu http://127.0.0.1:8000/ganti_password//{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True