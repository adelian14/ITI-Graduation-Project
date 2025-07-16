from typing import Optional, List
from models.Content import Content
from datetime import datetime

class DocumentObject:
    def __init__(self, _id, name, extension, parsed_content: Optional[Content] = None, json_representation = None, uploaded_at: Optional[datetime] = None, parent_project_id = None):
        self.id = str(_id) # generated unique id
        self.name = name # document name without extension
        self.extension = extension
        self.parsedContent = parsed_content
        self.jsonRepresentation = json_representation
        self.uploadedAt = uploaded_at or datetime.now()
        self.parentProjectId = parent_project_id
        self.error = None
        
    def get_full_name(self):
        return self.name + '_' + self.id + '.' + self.extension
    
    def get_full_path(self):
        return f"projects/{self.parentProjectId}/{self.name}_{self.id}.{self.extension}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "extension": self.extension,
            "uploadedAt": self.uploadedAt.isoformat(),
            "parsedContent": self.parsedContent.to_dict() if self.parsedContent else None,
            "jsonRepresentation": self.jsonRepresentation, 
            "parentProjectId": self.parentProjectId,
            "error":self.error
        }
        
    @classmethod
    def from_dict(cls, data):
        doc = cls(
            _id=data["id"],
            name=data["name"],
            extension=data["extension"],
            parsed_content=Content.from_dict(data["parsedContent"]) if data.get("parsedContent") else None,
            uploaded_at=datetime.fromisoformat(data["uploadedAt"]),
            json_representation=data["jsonRepresentation"],
            parent_project_id=data["parentProjectId"]
        )
        doc.error=data.get("error",None)
        return doc
    
    

