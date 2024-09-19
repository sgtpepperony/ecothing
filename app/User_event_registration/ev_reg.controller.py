from flask import Blueprint, request, jsonify
from app.User_event_registration.ev_reg.service import UserEventRegistrationService

user_event_bp = Blueprint('user_event_bp', __name__)

@user_event_bp.route('/register', methods=['POST'])
def register_for_event():
    data = request.get_json()
    user_id = data.get('user_id')
    event_id = data.get('event_id')

    registration = UserEventRegistrationService.register_user_for_event(user_id, event_id)
    
    if registration:
        return jsonify({
            "message": "User successfully registered for event",
            "qr_code": registration.qr_code
        }), 200
    return jsonify({"message": "Registration failed"}), 400

@user_event_bp.route('/attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    user_id = data.get('user_id')
    event_id = data.get('event_id')

    registration = UserEventRegistrationService.mark_attendance(user_id, event_id)
    if registration:
        return jsonify({"message": "Attendance marked successfully"}), 200
    return jsonify({"message": "Attendance marking failed"}), 400

@user_event_bp.route('/events/upcoming/<int:user_id>', methods=['GET'])
def get_upcoming_events(user_id):
    events = UserEventRegistrationService.get_user_events(user_id, attended=False)
    events_info = []

    for registration in events:
        events_info.append({
            "event_name": registration.event.name,
            "event_location": registration.event.location,
            "event_date": registration.event.date,
            "qr_code": registration.qr_code
        })

    return jsonify(events_info), 200

@user_event_bp.route('/events/past/<int:user_id>', methods=['GET'])
def get_past_events(user_id):
    events = UserEventRegistrationService.get_user_events(user_id, attended=True)
    events_info = []

    for registration in events:
        events_info.append({
            "event_name": registration.event.name,
            "event_location": registration.event.location,
            "event_date": registration.event.date,
            "rated": registration.rated
        })

    return jsonify(events_info), 200

@user_event_bp.route('/rate_event', methods=['POST'])
def rate_event():
    data = request.get_json()
    user_id = data.get('user_id')
    event_id = data.get('event_id')
    rating = data.get('rating')

    registration = UserEventRegistrationService.rate_event(user_id, event_id, rating)
    
    if registration:
        return jsonify({"message": "Event rated successfully"}), 200
    return jsonify({"message": "Rating failed"}), 400