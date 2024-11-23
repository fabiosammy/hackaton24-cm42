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
            password.basic_serialize
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
        return jsonify(new_password.basic_serialize), 201

    @staticmethod
    def show_password(vault_id, password_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        password = Password.query.filter_by(vault_id=vault_id, id=password_id).first()
        if not password:
            return jsonify({'message': 'Password not found in this vault'}), 404
        return jsonify(password.serialize)

    @staticmethod
    def destroy_password(vault_id, password_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        password = Password.query.filter_by(vault_id=vault_id, id=password_id).first()
        if not password:
            return jsonify({'message': 'Password not found in this vault'}), 404
        db.session.delete(password)
        db.session.commit()
        return jsonify({'message': 'Password deleted successfully'})
