from flask import Blueprint, request, jsonify
from app.Event import EventService

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = EventService.create_event(data)
    
    return jsonify({
        'message': 'Event created successfully',
        'event': {
            'id': new_event.id,
            'name': new_event.name,
            'format': new_event.format,
            'address': new_event.address,
            'applicant_full_name': new_event.applicant_full_name,
            'applicant_phone': new_event.applicant_phone,
            'social_media_link': new_event.social_media_link,
            'start_date': new_event.start_date,
            'end_date': new_event.end_date,
            'description': new_event.description
        }
    }), 201

@event_bp.route('/events', methods=['GET'])
def get_all_events():
    events = EventService.get_all_events()
    events_list = []
    for event in events:
        events_list.append({
            'id': event.id,
            'name': event.name,
            'format': event.format,
            'address': event.address,
            'applicant_full_name': event.applicant_full_name,
            'applicant_phone': event.applicant_phone,
            'social_media_link': event.social_media_link,
            'start_date': event.start_date,
            'end_date': event.end_date,
            'description': event.description
        })
    
    return jsonify(events_list), 200

@event_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    event = EventService.get_event_by_id(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404
    
    return jsonify({
        'id': event.id,
        'name': event.name,
        'format': event.format,
        'address': event.address,
        'applicant_full_name': event.applicant_full_name,
        'applicant_phone': event.applicant_phone,
        'social_media_link': event.social_media_link,
        'start_date': event.start_date,
        'end_date': event.end_date,
        'description': event.description
    }), 200

@event_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    updated_event = EventService.update_event(event_id, data)
    
    if updated_event:
        return jsonify({
            'message': 'Event updated successfully',
            'event': {
                'id': updated_event.id,
                'name': updated_event.name,
                'format': updated_event.format,
                'address': updated_event.address,
                'applicant_full_name': updated_event.applicant_full_name,
                'applicant_phone': updated_event.applicant_phone,
                'social_media_link': updated_event.social_media_link,
                'start_date': updated_event.start_date,
                'end_date': updated_event.end_date,
                'description': updated_event.description
            }
        }), 200
    
    return jsonify({'message': 'Event not found'}), 404

@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    success = EventService.delete_event(event_id)
    
    if success:
        return jsonify({'message': 'Event deleted successfully'}), 200
    return jsonify({'message': 'Event not found'}), 404