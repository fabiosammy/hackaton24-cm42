from flask import jsonify, request
from ..extensions import db
from ..models.vault import Vault
from ..models.password import Password

class PasswordsController:
    @staticmethod
    def passwords_index(vault_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        return jsonify([
            password.serialize
            for password in vault.passwords
        ])

    @staticmethod
    def create_password(vault_id):
        data = request.get_json()
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404

        if 'name' not in data:
            return jsonify({'message': 'Name is required'}), 400

        new_password = Password(
            name=data['name'],
            username=data.get('username'),
            password=data.get('password'),
            otp_key=data.get('otp_key'),
            description=data.get('description'),
            vault=vault
        )

        db.session.add(new_password)
        db.session.commit()
        return jsonify(new_password.serialize), 201
