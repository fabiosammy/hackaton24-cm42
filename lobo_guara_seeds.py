import random
from faker import Faker
from hackaton import create_app
from hackaton.extensions import db
from hackaton.models.vault import Vault
from hackaton.models.credential import Credential
from hackaton.models.tag import Tag
from hackaton.models.url import Url

fake = Faker()
app = create_app()

def create_vaults_and_credentials():
    with app.app_context():
        # Clear existing data
        db.session.query(Url).delete()
        db.session.query(Credential).delete()
        db.session.query(Tag).delete()
        db.session.query(Vault).delete()
        db.session.commit()

        # Create vaults
        vaults = []
        for i in range(3):
            vault = Vault(name=f"Vault {i+1}")
            db.session.add(vault)
            vaults.append(vault)

        db.session.commit()

        # Create credentials with tags and URLs
        for i in range(15):
            vault = random.choice(vaults)

            # Create a credential
            credential = Credential(
                name=f"Account {i+1}",
                username=fake.user_name(),
                password=fake.password(),
                otp_key=fake.sha256(raw_output=False)[:16],
                description=fake.sentence(),
                vault=vault
            )

            # Add tags
            tags = []
            for _ in range(random.randint(1, 3)):  # 1-3 tags per credential
                tag_name = fake.word()
                tag = Tag.query.filter_by(name=tag_name, vault_id=vault.id).first()
                if not tag:
                    tag = Tag(name=tag_name, vault=vault)
                    db.session.add(tag)
                tags.append(tag)

            credential.tags.extend(tags)

            # Add URLs
            for _ in range(random.randint(1, 3)):  # 1-3 URLs per credential
                url = Url(name=fake.url(), credential=credential)
                db.session.add(url)

            db.session.add(credential)

        db.session.commit()

if __name__ == "__main__":
    create_vaults_and_credentials()
    print("Seed data created successfully!")