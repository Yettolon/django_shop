from django.apps import AppConfig
from django.dispatch import Signal

from .utilities import send_activation_notification

class BboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bboard'

user_reg = Signal(providing_args=['instance'])

def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_reg.connect(user_registered_dispatcher)