from flask import Blueprint
from .controllers.vaults_controller import VaultsController

routes = Blueprint('routes', __name__)

# Vault Routes
routes.add_url_rule('/vaults', view_func=VaultsController.index, methods=['GET'])
routes.add_url_rule('/vaults', view_func=VaultsController.create, methods=['POST'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.show, methods=['GET'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.update, methods=['PUT'])
routes.add_url_rule('/vaults/<int:vault_id>', view_func=VaultsController.destroy, methods=['DELETE'])
