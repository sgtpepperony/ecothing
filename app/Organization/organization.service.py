from app import db
from app.Organization.organization.entity import Organization

class OrganizerService:
    @staticmethod
    def create_organizer(data):
        is_legal_entity = data.get('is_legal_entity', False)
        data_processing_consent = data.get('data_processing_consent', False)
        
        if is_legal_entity:
            organizer = Organization(
                is_legal_entity=True,
                organization_name=data['organization_name'],
                inn=data['inn'],
                website=data['website'],
                contact_phone=data['contact_phone'],
                data_processing_consent=data_processing_consent
            )
        else:
            organizer = Organization(
                is_legal_entity=False,
                full_name=data['full_name'],
                email=data['email'],
                social_link=data['social_link'],
                contact_phone=data['contact_phone'],
                data_processing_consent=data_processing_consent
            )
        
        db.session.add(organizer)
        db.session.commit()
        return organizer