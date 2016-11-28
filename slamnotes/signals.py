from django.core.signing import TimestampSigner
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def confirmation_handler(sender, instance, **kwargs):
    """Generates a confirmation code based on the user's email and current time."""
    if not instance.confirmation_code:
        signer = TimestampSigner()
        signed_email = signer.sign(instance.email)

        # Strip original string and colons
        instance.confirmation_code = signed_email.split(":", 1)[1].replace(':', '')

post_save.connect(confirmation_handler, sender=User)
