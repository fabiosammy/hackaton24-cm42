from ..extensions import db

class Vault(db.Model):
    __tablename__ = 'vaults'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relations
    credentials = db.relationship('Credential', back_populates='vault', cascade='all, delete-orphan')
    tags = db.relationship('Tag', back_populates='vault', cascade='all, delete-orphan')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __repr__(self):
        return f'<Vault {self.name}>'
