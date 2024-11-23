from flask import jsonify, request
from ..extensions import db
from ..models.vault import Vault
from ..models.credential import Credential
from ..models.tag import Tag
from ..models.url import Url

class CredentialsController:
    @staticmethod
    def credentials_index(vault_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        return jsonify([
            credential.basic_serialize
            for credential in vault.credentials
        ])

    @staticmethod
    def create_credential(vault_id):
        data = request.get_json()
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404

        if 'name' not in data:
            return jsonify({'message': 'Name is required'}), 400

        new_credential = Credential(
            name=data['name'],
            username=data.get('username'),
            password=data.get('password'),
            otp_key=data.get('otp_key'),
            description=data.get('description'),
            vault=vault
        )

        for url_value in data['urls']:
            new_url = Url(name=url_value, credential=new_credential)
            db.session.add(new_url)

        for tag_name in data['tags']:
            tag = Tag.query.filter_by(name=tag_name, vault_id=vault_id).first()
            if not tag:
                tag = Tag(name=tag_name, vault=vault)
                db.session.add(tag)
            new_credential.tags.append(tag)

        db.session.add(new_credential)
        db.session.commit()
        return jsonify(new_credential.basic_serialize), 201

    @staticmethod
    def show_credential(vault_id, credential_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        credential = Credential.query.filter_by(vault_id=vault_id, id=credential_id).first()
        if not credential:
            return jsonify({'message': 'Credential not found in this vault'}), 404
        return jsonify(credential.serialize)

    @staticmethod
    def update_credential(vault_id, credential_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        credential = Credential.query.filter_by(vault_id=vault_id, id=credential_id).first()
        if not credential:
            return jsonify({'message': 'Credential not found in this vault'}), 404

        data = request.get_json()

        credential.name = data.get('name', credential.name)
        credential.username = data.get('username', credential.username)
        credential.password = data.get('password', credential.password)
        credential.otp_key = data.get('otp_key', credential.otp_key)
        credential.description = data.get('description', credential.description)

        credential.urls.clear()
        for url_value in data['urls']:
            new_url = Url(name=url_value, credential=credential)
            db.session.add(new_url)

        credential.tags.clear()
        for tag_name in data['tags']:
            tag = Tag.query.filter_by(name=tag_name, vault_id=vault_id).first()
            if not tag:
                tag = Tag(name=tag_name, vault=vault)
                db.session.add(tag)
            credential.tags.append(tag)

        db.session.commit()
        return jsonify(credential.serialize)

    @staticmethod
    def destroy_credential(vault_id, credential_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        credential = Credential.query.filter_by(vault_id=vault_id, id=credential_id).first()
        if not credential:
            return jsonify({'message': 'Credential not found in this vault'}), 404
        db.session.delete(credential)
        db.session.commit()
        return jsonify({'message': 'Credential deleted successfully'})
