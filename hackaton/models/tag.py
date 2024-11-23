from ..extensions import db

credential_tags = db.Table(
    'credential_tags',
    db.Column('credential_id', db.Integer, db.ForeignKey('credentials.id', ondelete='CASCADE'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True)
)

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relationship
    vault_id = db.Column(db.Integer, db.ForeignKey('vaults.id'), nullable=False)
    vault = db.relationship('Vault', back_populates='tags')
    credentials = db.relationship('Credential', secondary=credential_tags, back_populates='tags')

    @property
    def serialize(self):
        return {
            'name': self.name
        }

    def __repr__(self):
        return f"<Tag {self.name}>"
