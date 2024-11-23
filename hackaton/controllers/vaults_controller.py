from flask import jsonify, request
from ..extensions import db
from ..models.vault import Vault

class VaultsController:
    @staticmethod
    def index():
        vaults = Vault.query.all()
        return jsonify([{'id': vault.id, 'name': vault.name} for vault in vaults])

    @staticmethod
    def create():
        data = request.get_json()
        if 'name' not in data:
            return jsonify({'message': 'Name is required'}), 400

        new_vault = Vault(name=data['name'])
        db.session.add(new_vault)
        db.session.commit()
        return jsonify({'id': new_vault.id, 'name': new_vault.name}), 201

    @staticmethod
    def show(vault_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404
        return jsonify({'id': vault.id, 'name': vault.name})

    @staticmethod
    def update(vault_id):
        data = request.get_json()
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404

        vault.name = data.get('name', vault.name)
        db.session.commit()
        return jsonify({'id': vault.id, 'name': vault.name})

    @staticmethod
    def destroy(vault_id):
        vault = Vault.query.get(vault_id)
        if not vault:
            return jsonify({'message': 'Vault not found'}), 404

        db.session.delete(vault)
        db.session.commit()
        return jsonify({'message': 'Vault deleted successfully'})
