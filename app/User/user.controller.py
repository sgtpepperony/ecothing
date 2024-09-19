from flask import Blueprint, request, jsonify
from app.User.user.service import UserService

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = UserService.register_user(data)
    if user:
        return jsonify({"message": "User registered successfully", "user": str(user)}), 201
    return jsonify({"message": "Error registering user"}), 400

@user_controller.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({
            "id": user.id,
            "name": user.Name,
            "surname": user.Surname,
            "email": user.email,
            "town": user.Town
        })
    return jsonify({"message": "User not found"}), 404

@user_controller.route('/user/<int:user_id>/events', methods=['GET'])
def get_user_events(user_id):
    events = UserService.get_user_events(user_id)
    if events:
        return jsonify([{
            "event_id": e.event_id,
            "event_name": e.event.name,  # Предполагается, что есть связь между регистрацией и событием
            "status": "registered"
        } for e in events])
    return jsonify({"message": "No events found"}), 404

@user_controller.route('/user/<int:user_id>/register_event/<int:event_id>', methods=['POST'])
def register_for_event(user_id, event_id):
    registration = UserService.register_for_event(user_id, event_id)
    if registration:
        return jsonify({"message": "User registered for event", "event_id": event_id}), 200
    return jsonify({"message": "Registration failed"}), 400

@user_controller.route('/user/<int:user_id>/award_points', methods=['POST'])
def award_points(user_id):
    data = request.get_json()
    event_id = data['event_id']
    points = data['points']
    new_points = UserService.award_points(user_id, event_id, points)
    if new_points is not None:
        return jsonify({"message": "Points awarded", "total_points": new_points}), 200
    return jsonify({"message": "Error awarding points"}), 400