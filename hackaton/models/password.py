from ..extensions import db

class Password(db.Model):
    __tablename__ = 'passwords'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    otp_key = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    
    # Relations
    vault_id = db.Column(db.Integer, db.ForeignKey('vaults.id'), nullable=False)
    vault = db.relationship('Vault', back_populates='passwords')

    @property
    def basic_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'description': self.description,
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
            'vault_id': self.vault_id
        }

    def __repr__(self):
        return f'<Password {self.name}>'
