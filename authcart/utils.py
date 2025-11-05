from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  # Required for compatibility in older Django, not needed in newer versions

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)

generate_token = TokenGenerator()
