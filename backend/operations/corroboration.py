from bottle_jwt.auth import BaseAuthBackend


class Corroboration(BaseAuthBackend):
    def _BaseAuthBackend_authenticate_user(self, username, password):
        return super(BaseAuthBackend, self).authenticate_user(
            self, username, password)
