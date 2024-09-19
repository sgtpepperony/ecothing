from flask import Blueprint, request, jsonify
from app.Organization import OrganizerService

organizer_bp = Blueprint('organizer', __name__)

@organizer_bp.route('/organizers', methods=['POST'])
def create_organizer():
    data = request.json
    if not data.get('data_processing_consent'):
        return jsonify({'error': 'You must accept data processing terms'}), 400
    
    organizer = OrganizerService.create_organizer(data)
    return jsonify({'message': 'Organizer created', 'organizer': organizer.id}), 201

@organizer_bp.route('/organizers/<int:id>/statistics', methods=['PUT'])
def update_statistics(id):
    data = request.json
    registered_count = data.get('registered_count', 0)
    visited_count = data.get('visited_count', 0)
    
    organizer = OrganizerService.update_statistics(id, registered_count, visited_count)
    
    if not organizer:
        return jsonify({'error': 'Organizer not found'}), 404
    
    return jsonify({
        'message': 'Statistics updated',
        'total_registered': organizer.total_registered,
        'total_visited': organizer.total_visited
    })