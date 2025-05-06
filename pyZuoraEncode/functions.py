import logging
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class ZuoraEncrypt:
    def __init__(self, public_key=None):
        self.logger = logging.getLogger('ZuoraEncrypt')
        self.logger.setLevel(logging.WARNING)
        self.public_key = None
        if public_key:
            self.set_key(public_key)

    def set_key(self, public_key):
        try:
            self.public_key = RSA.import_key(
                f"-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----"
            )
            return True
        except Exception as e:
            self.logger.error(f"Error setting public key: {str(e)}")
            return False

    def encrypt(self, data):
        try:
            if not self.public_key:
                raise ValueError("Public key not set")
            
            if isinstance(data, str):
                data_parts = data.split("|")
                data_for_send = "#" + "#".join(data_parts)
                data_for_send = base64.b64encode(data_for_send.encode('utf-8'))

                cipher = PKCS1_OAEP.new(self.public_key)
                encrypted_data = cipher.encrypt(data_for_send)
                return base64.b64encode(encrypted_data).decode('utf-8')
            else:
                raise ValueError("Data must be a string")
        except Exception as e:
            self.logger.error(f"Error encrypting data: {str(e)}")
            return None

