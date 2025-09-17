from flask import Blueprint, request, jsonify
from app.mcp_server import mcp

routes = Blueprint('routes', __name__)

@routes.route('/mcp', methods=['POST'])
def handle_mcp():
    payload = request.get_json()
    response = mcp.handle_message(payload)
    return jsonify(response.model_dump(exclude_none=True))
