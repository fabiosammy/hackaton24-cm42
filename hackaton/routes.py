from flask import Blueprint
from .controllers.vaults_controller import VaultsController
from .controllers.credentials_controller import CredentialsController

routes = Blueprint('routes', __name__)

# Vault Routes
routes.add_url_rule('/vaults', view_func=VaultsController.index, methods=['GET'])
routes.add_url_rule('/vaults', view_func=VaultsController.create, methods=['POST'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.show, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.update, methods=['PUT'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.destroy, methods=['DELETE'])

# Credential Routes
routes.add_url_rule('/vaults/<int:vault_id>/credentials', view_func=CredentialsController.credentials_index, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>/credentials', view_func=CredentialsController.create_credential, methods=['POST'])
routes.add_url_rule('/vaults/<int:vault_id>/credentials/<int:credential_id>', view_func=CredentialsController.show_credential, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>/credentials/<int:credential_id>', view_func=CredentialsController.update_credential, methods=['PUT'])
routes.add_url_rule('/vaults/<int:vault_id>/credentials/<int:credential_id>', view_func=CredentialsController.destroy_credential, methods=['DELETE'])
