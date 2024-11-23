import os
import base64
from cryptography.fernet import Fernet
from ..extensions import db
from .tag import credential_tags

class Credential(db.Model):
    __tablename__ = 'credentials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password_salt = db.Column(db.String(32), nullable=False)
    password_encrypted = db.Column(db.LargeBinary, nullable=False)
    otp_key_salt = db.Column(db.String(32), nullable=True)
    otp_key_encrypted = db.Column(db.LargeBinary, nullable=True)
    description = db.Column(db.Text, nullable=True)
    
    # Relations
    vault_id = db.Column(db.Integer, db.ForeignKey('vaults.id'), nullable=False)
    vault = db.relationship('Vault', back_populates='credentials')
    tags = db.relationship('Tag', secondary=credential_tags, back_populates='credentials')
    urls = db.relationship('Url', back_populates='credential', cascade='all, delete-orphan')

    # Encryption/decryption key
    _fernet = Fernet(os.getenv('LOBO_GUARA_KEY'))

    @staticmethod
    def generate_salt():
        return base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')

    @property
    def password(self):
        password_with_salt = self._fernet.decrypt(self.password_encrypted).decode('utf-8')
        return password_with_salt[len(self.password_salt):]

    @password.setter
    def password(self, value):
        salt = self.generate_salt()
        self.password_salt = salt
        password_with_salt = f"{salt}{value}".encode('utf-8')
        self.password_encrypted = self._fernet.encrypt(password_with_salt)

    @property
    def otp_key(self):
        if not self.otp_key_encrypted or not self.otp_key_salt:
            return None
        otp_key_with_salt = self._fernet.decrypt(self.otp_key_encrypted).decode('utf-8')
        return otp_key_with_salt[len(self.otp_key_salt):]

    @otp_key.setter
    def otp_key(self, value):
        if value is not None:
            salt = self.generate_salt()
            self.otp_key_salt = salt
            otp_key_with_salt = f"{salt}{value}".encode('utf-8')
            self.otp_key_encrypted = self._fernet.encrypt(otp_key_with_salt)

    @property
    def basic_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'description': self.description,
            'urls': [url.name for url in self.urls],
            'tags': [tag.name for tag in self.tags],
            'vault_id': self.vault_id
        }

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'password': self.password,
            'otp_key': self.otp_key,
            'description': self.description,
            'urls': [url.name for url in self.urls],
            'tags': [tag.name for tag in self.tags],
            'vault_id': self.vault_id
        }

    def __repr__(self):
        return f'<Credential {self.name}>'
