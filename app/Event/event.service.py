from app import db
from app.Event import Event
from app.Organization import OrganizerService
from datetime import datetime

class EventService:
    
    @staticmethod
    def create_event(data, organizer_id):
        organizer = OrganizerService.get_organizer_by_id(organizer_id)
        if not organizer:
            raise ValueError("Organizer not found")
        new_event = Event(
            name=data.get('name'),
            format=data.get('format'),
            address=data.get('address'),
            organizer=organizer,
            applicant_full_name=data.get('applicant_full_name'),
            applicant_phone=data.get('applicant_phone'),
            social_media_link=data.get('social_media_link'),
            start_date=datetime.strptime(data.get('start_date'), '%Y-%m-%d %H:%M:%S'),
            end_date=datetime.strptime(data.get('end_date'), '%Y-%m-%d %H:%M:%S'),
            description=data.get('description')
        )
        db.session.add(new_event)
        db.session.commit()
        return new_event

    @staticmethod
    def get_all_events():
        return Event.query.all()

    @staticmethod
    def get_event_by_id(event_id):
        return Event.query.filter_by(id=event_id).first()
    @staticmethod
    def get_events_by_organizer(organizer_id):
        return Event.query.filter_by(organizer_id=organizer_id).all()

    @staticmethod
    def update_event(event_id, data):
        event = Event.query.filter_by(id=event_id).first()
        if event:
            event.name = data.get('name', event.name)
            event.format = data.get('format', event.format)
            event.address = data.get('address', event.address)
            event.applicant_full_name = data.get('applicant_full_name', event.applicant_full_name)
            event.applicant_phone = data.get('applicant_phone', event.applicant_phone)
            event.social_media_link = data.get('social_media_link', event.social_media_link)
            event.start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d %H:%M:%S') if data.get('start_date') else event.start_date
            event.end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d %H:%M:%S') if data.get('end_date') else event.end_date
            event.description = data.get('description', event.description)
            db.session.commit()
            return event
        return None

    @staticmethod
    def delete_event(event_id):
        event = Event.query.filter_by(id=event_id).first()
        if event:
            db.session.delete(event)
            db.session.commit()
            return True
        return False