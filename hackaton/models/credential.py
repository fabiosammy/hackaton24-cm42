from ..extensions import db
from .tag import credential_tags

class Credential(db.Model):
    __tablename__ = 'credentials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    otp_key = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    
    # Relations
    vault_id = db.Column(db.Integer, db.ForeignKey('vaults.id'), nullable=False)
    vault = db.relationship('Vault', back_populates='credentials')
    tags = db.relationship('Tag', secondary=credential_tags, back_populates='credentials')

    @property
    def basic_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'description': self.description,
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
            'tags': [tag.name for tag in self.tags],
            'vault_id': self.vault_id
        }

    def __repr__(self):
        return f'<Credential {self.name}>'
