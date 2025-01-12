from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re

class DateOfBirthPasswordValidator:
        def validate(self, password, user=None):
            # Check if the password is in the format DDMMYYYY
            if not re.match(r'^\d{2}\d{2}\d{4}$', password):
                raise ValidationError(
                    _("This password must be in the format DDMMYYYY."),
                    code='password_no_dob_format',
                )

        def get_help_text(self):
            return _("Your password must be in the format DDMMYYYY.")