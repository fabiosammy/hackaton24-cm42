from flask import Blueprint
from .controllers.vaults_controller import VaultsController
from .controllers.passwords_controller import PasswordsController

routes = Blueprint('routes', __name__)

# Vault Routes
routes.add_url_rule('/vaults', view_func=VaultsController.index, methods=['GET'])
routes.add_url_rule('/vaults', view_func=VaultsController.create, methods=['POST'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.show, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.update, methods=['PUT'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.destroy, methods=['DELETE'])

# Password Routes
routes.add_url_rule('/vaults/<int:vault_id>/passwords', view_func=PasswordsController.passwords_index, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>/passwords', view_func=PasswordsController.create_password, methods=['POST'])
routes.add_url_rule('/vaults/<int:vault_id>/passwords/<int:password_id>', view_func=PasswordsController.show_password, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>/passwords/<int:password_id>', view_func=PasswordsController.update_password, methods=['PUT'])
routes.add_url_rule('/vaults/<int:vault_id>/passwords/<int:password_id>', view_func=PasswordsController.destroy_password, methods=['DELETE'])
