from ..extensions import db

class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    # Relations
    credential_id = db.Column(db.Integer, db.ForeignKey('credentials.id'), nullable=False)
    credential = db.relationship('Credential', back_populates='urls')

    @property
    def serialize(self):
        return {
            'name': self.name
        }

    def __repr__(self):
        return f"<Url {self.name}>"
